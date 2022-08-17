from django.shortcuts import render

# Create your views here.

from rest_framework.serializers import Serializer
# from customer.serializers import user_profile_serializer
from customer.models import user_profile
from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.shortcuts import render
import django.contrib.auth
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from supervisor.models import supervisor
from supervisor.serializers import supervisorserializer, supervisorserialzerupdate


class becomeSupervisor(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    def post(self, request):

        try :
            user = user_profile.objects.get(user=request.user)
            if user.is_verified and user.user_type=="customer":
                data = request.data
                s = supervisor(user=request.user,service_provider=data["service_provider"], bank_acc_no=data["bank_acc_no"], bank_name=data["bank_name"],bank_acc_name=data["bank_acc_name"],bank_ifsc=data["bank_ifsc"])
                s.save()
                s.supervisor_is_active = True
                user.user_type = "supervisor"
                user.save()
                msg = {
                    "msg":"you are now a supervisor",
                    "res": "successful"
                }
                # serializer = supervisorserialzer(s)
                serializer = supervisorserializer(s)
                msg.update(serializer.data)
                return Response(msg, status=status.HTTP_200_OK)
            else:
                msg = {
                    "msg":"You are already a supervisor or Your user id is not verified",
                    "res":"fail"
                }
                return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            msg ={
                "msg":f"{e}",
                "resp":"fail"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

class supervisorDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    def get(sel, request):
        try :
            # user = user_profile.objects.get(user=request.user)
            # if user.user_type == "supervisor":
            # print("############")
            sup = supervisor.objects.get(user=request.user)
            # print(sup)
            serializer = supervisorserializer(sup)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            # print(e)
            return Response({"msg":f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try :
            sup = supervisor.objects.get(user=request.user)
            serializer = supervisorserialzerupdate(sup, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                sup = supervisor.objects.get(user=request.user)
                se = supervisorserializer(sup)
                # return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(se.data, status=status.HTTP_200_OK)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"msg":f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

