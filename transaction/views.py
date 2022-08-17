from charzer import settings
from customer.models import user_profile
from transaction.models import transaction_model, addmoney_model
from device.models import device
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from transaction.serializers import transactionserializer
from rest_framework.response import Response
from rest_framework import status
from customer.serializers import user_profile_serializer
import uuid, requests, json
# Create your views here.

class transactionapi(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes  = [IsAuthenticated]

    def post(self, request):
        try:
            ndevice = device.objects.get(device_id=request.data["device_id"])
            txn_amount = int(request.data["txn_amount"])
            desc = request.data["description"]
            uid = str(uuid.uuid4())
            txn = transaction_model(txn_id=uid, customer=request.user, device=ndevice, txn_amt=txn_amount, description=desc)
            txn.save()
            customer = user_profile.objects.get(user=request.user)
            if customer.wallet_amt < txn_amount:
                msg = {
                    "resp": "fail",
                    "msg":"insufficient balance"
                }
                return Response(msg, status=status.HTTP_402_PAYMENT_REQUIRED)
            print(customer.wallet_amt)
            customer.wallet_amt = customer.wallet_amt - txn_amount
            customer.save()
            print(customer.wallet_amt)
            nagent = ndevice.agent
            nagent.balance_amount = nagent.balance_amount + txn_amount
            nagent.save()
            txn.txn_status = "completed"
            txn.save()
            ser = transactionserializer(txn)
            serc = user_profile_serializer(customer)
            dat = ser.data
            dat.update(serc.data)
            # dat.user_photo = settings.website_name + dat.user_photo
            dat["user_photo"] = settings.website_name + dat["user_photo"]
            return Response(dat, status=status.HTTP_200_OK)

        except Exception as e:
            msg = {
                "resp":"fail",
                "msg":f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)





class addmoney(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes  = [IsAuthenticated]
    def post(self, request):
        uid = uuid.uuid4()
        # adm = addmoney(addmoney_id=uid, customer=request.user )
        adm = addmoney_model(addmoney_id=uid, customer=request.user, order_amount=request.data["order_amount"],order_currency=request.data["currency"])
        adm.save()
        print("one")
        dat = {
            "orderId":adm.addmoney_id,
            "orderAmount":adm.order_amount,
            "orderCurrency":adm.order_currency
        }

        url = "https://test.cashfree.com/api/v2/cftoken/order"
        headers = {'x-client-id': '83488cf107b44fbaf54461cd388438',"Content-Type":"application/json", "x-client-secret":"70418e3b9c135089c4713933e8339b140ab994a9"}
        print("two")
        r = requests.post(url, headers=headers, data=json.dumps(dat))
        print("three")
        # print(r.json())
        # d = json.loads(r.json)
        # print(d)
        # return HttpResponse(r.json(), content_type='application/json')
        return Response(r.json())


    def get(self, request):
        url = "https://test.cashfree.com/api/v2/cftoken/order"
        # headers = {'x-client-id': f"{request.user}","Content-Type":"application/json", "x-client-secret":"70418e3b9c135089c4713933e8339b140ab994a9"}

        headers = {'x-client-id': '83488cf107b44fbaf54461cd388438',"Content-Type":"application/json", "x-client-secret":"70418e3b9c135089c4713933e8339b140ab994a9"}
        print("two")
        dat = {
            # "orderId":adm.addmoney_id,
            "orderId":"o-12",
            "orderAmount":100,
            "orderCurrency":"INR"
        }
        r = requests.post(url, headers=headers, data=json.dumps(dat))
        return Response(r.json())