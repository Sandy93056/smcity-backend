from customer.models import gbvariables, user_profile
from tracker.models import AddDeviceTracker
from rest_framework.fields import MISSING_ERROR_MESSAGE
from device.models import device, dustbin, smarttoilet, washroom, waterpoint
from agent.models import agent
# from django.shortcuts import render
from rest_framework.views import APIView
from agent.models import agent
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from device.serializers import deviceserializer, dustbinserializer, smarttoiletserializer, washroomserializer, waterpointserializer, updatedeviceserializer, updatedustbinserializer, updatewashroomserializer, updatewaterpointserializer
# Create your views here.
import math


class deviceapi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]

    def put(self, request):
        try :
            ndevice = device.objects.get(device_mac = request.data["device_mac"])
            ser = deviceserializer(ndevice)
            dat = ser.data
            if ndevice.device_type == "dustbin":
                ndustbin = dustbin.objects.get(device=ndevice)
                dustserializer = dustbinserializer(ndustbin)
                dat.update(dustserializer.data)
            elif ndevice.device_type == "waterpoint":
                nwaterpoint = waterpoint.objects.get(device=ndevice)
                waterserializer =waterpointserializer(nwaterpoint)
                dat.update(waterserializer.data)
            
            elif ndevice.device_type == "smarttoilet":
                ntoilet = smarttoilet.objects.get(device=ndevice)
                smtser = smarttoiletserializer(ntoilet)
                dat.update(smtser.data)


            return Response(dat, status=status.HTTP_200_OK)

        except Exception as e:
            msg = {
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try :
            data = request.data
            device_mac = data["device_mac"]
            if device.objects.filter(device_mac=device_mac).exists():
                return Response({"resp":"fail", "msg":"device already connected to another agent"})
            else:
                nagent = agent.objects.get(user = request.user)

                device_lat = data["device_lat"]
                device_long = data["device_long"]
                device_type = data["device_type"]
                ndevice = device(agent=nagent, device_lat=device_lat, device_long=device_long, device_type=device_type, device_mac=device_mac)
                ndevice.save()
                print(device_type)
                if device_type == "dustbin":
                    z = dustbin(device = ndevice, bin_total_volume=data["bin_total_volume"], bin_total_height=data["bin_total_height"], bin_avai_volume=data["bin_avai_volume"])
                    z.save()
                    ds = dustbinserializer(z)
                    dat = ds.data
                elif device_type == "waterpoint":
                    z = waterpoint(device=ndevice, total_water_capacity=data["total_water_capacity"], water_available=data["water_available"])
                    z.save()
                    ws = waterpointserializer(z)
                    dat = ws.data

                elif device_type == "smarttoilet":
                    z = smarttoilet(device=ndevice, waterlevel=data["waterlevel"], description = data["description"])
                    z.save()
                    ws = smarttoiletserializer(z)
                    dat = ws.data                    
                else:
                    msg = {
                        "resp":"fail",
                        "msg":"invalid device type"
                    }
                    ndevice.delete()
                    return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                s = deviceserializer(ndevice)
                dat.update(s.data)
                return Response(dat, status=status.HTTP_200_OK)


        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request):

        try :
            nagent = agent.objects.get(user=request.user)
            ndevice = device.objects.get(device_mac=request.data["device_mac"])
            if ndevice.agent == nagent:
                devserializer = updatedeviceserializer(ndevice, data=request.data, partial=True)
                if devserializer.is_valid():
                    devserializer.save()
                    ndevice = device.objects.get(device_mac=request.data["device_mac"])
                    devserializer = deviceserializer(ndevice)
                    dat = devserializer.data
                else:
                    msg = {
                        "resp":"fail",
                        "msg":f"{devserializer.errors}"
                    }
                    return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                if ndevice.device_type == "dustbin":
                    ndustbin = dustbin.objects.get(device=ndevice)
                    dustserializer = updatedustbinserializer(ndustbin, data=request.data, partial=True)
                    if dustserializer.is_valid():
                        dustserializer.save()
                        ndustbin = dustbin.objects.get(device=ndevice)
                        dustserializer = dustbinserializer(ndustbin)
                        dat.update(dustserializer.data)
                    else:
                        msg = {
                        "resp":"fail",
                        "msg":f"{dustserializer.errors}"
                        }
                        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

                elif ndevice.device_type == "waterpoint":
                    nwaterpoint = waterpoint.objects.get(device=ndevice)
                    waterserializer = updatewaterpointserializer(nwaterpoint, data=request.data, partial=True)
                    if waterserializer.is_valid():
                        waterserializer.save()
                        nwaterpoint = waterpoint.objects.get(device=ndevice)
                        waterserializer = waterpointserializer(nwaterpoint)
                        dat.update(waterserializer.data)
                    else:
                        msg = {
                        "resp":"fail",
                        "msg":f"{waterserializer.errors}"
                        }
                        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                elif ndevice.device_type == "smarttoilet":
                    ntoilet = smarttoilet.objects.get(device=ndevice)
                    toiletserializer = smarttoiletserializer(ntoilet, data=request.data, partial=True)
                    if toiletserializer.is_valid():
                        toiletserializer.save()
                        ntoilet = smarttoilet.objects.get(device=ndevice)
                        toiletserializer = smarttoiletserializer(ntoilet)
                        dat.update(toiletserializer.data)
                    else:
                        msg = {
                        "resp":"fail",
                        "msg":f"{toiletserializer.errors}"
                        }
                        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                return Response(dat, status=status.HTTP_200_OK)


        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class near(APIView):
    def post(self, request):
        try:
            lat = request.data["user_lat"]
            lon = request.data["user_long"]
            lat = math.radians(float(lat))
            lon = math.radians(float(lon))
            range = int(request.data["range"]) + 10
            near_device_obj = device.objects.raw(f'SELECT device_id, 6371.01 * acos(sin({lat})*sin(radians(device_lat)) + cos({lat})*cos(radians(device_lat))*cos({lon} - radians(device_long))) AS distance FROM DEVICE_DEVICE GROUP BY device_id HAVING distance < {range}')
            # near_device_obj = device.objects.raw(f'SELECT device_id, ROUND (6371.01 * acos(sin({lat})*sin(radians(device_lat)) + cos({lat})*cos(radians(device_lat))*cos({lon} - radians(device_long)))) AS distance FROM DEVICE_DEVICE GROUP BY device_id HAVING distance <11')
            ser = deviceserializer(near_device_obj, many=True)
            # devlist = device.objects.all()
            # li =[]
            # for dev in devlist:
            #     dist = 6371.01 * acos(sin(lat)*sin(dev.device_lat) + cos(lat)*cos(dev.device_lat)*cos(lon - dev.device_long))
            #     li.append(dist)
            # dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
            msg = {
                "resp": "success",
                "device_list" : ser.data
            }
            return Response(msg, status= status.HTTP_200_OK)

        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        lat = request.data["user_lat"]
        lon = request.data["user_long"]
        lat = math.radians(float(lat))
        lon = math.radians(float(lon))
        range = int(request.data["range"]) 
        near_device_obj = device.objects.raw(f'SELECT device_id, 6371.01 * acos(sin({lat})*sin(radians(device_lat)) + cos({lat})*cos(radians(device_lat))*cos({lon} - radians(device_long))) AS distance FROM DEVICE_DEVICE GROUP BY device_id HAVING distance < {range}')
        ser = deviceserializer(near_device_obj, many=True)
        msg = {
            "resp": "success",
            "device_list" : ser.data
        }
        # f = SELECT device_id, 6371.01 * acos(sin({lat})*sin(radians(device_lat)) + cos({lat})*cos(radians(device_lat))*cos({lon} - radians(device_long))) AS distance FROM DEVICE_DEVICE GROUP BY device_id HAVING distance < range
        # print(ser.data)
        for s in ser.data:
            # print(s)
            for z in s:
                if z == "device_mac":
                    print(z)
                pass
        return Response(msg, status= status.HTTP_200_OK)        
        

class AddDeviceRestricted(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]
    def post(self, request):
        try :
            # up = user_profile.objects.get(user=request.user)
            user_mac = request.data["android_mac"]
            nagent = agent.objects.get(user = request.user)
            addDeviceCount = AddDeviceTracker.objects.filter(agent=nagent).count()
            limit = gbvariables.objects.all().first().no_of_allowed_addDevice
            if addDeviceCount>limit:
                msg ={
                    "resp":"fail",
                    "msg": "you are adding too much devices"
                }
                return Response(msg, status=status.HTTP_429_TOO_MANY_REQUESTS)
            data = request.data
            device_mac = data["device_mac"]
            
            if device.objects.filter(device_mac=device_mac).exists():
                return Response({"resp":"fail", "msg":"device already connected to another agent"}, status=status.HTTP_400_BAD_REQUEST)
            else:

                device_lat = data["device_lat"]
                device_long = data["device_long"]
                device_type = data["device_type"]
                ndevice = device(agent=nagent, device_lat=device_lat, device_long=device_long, device_type=device_type, device_mac=device_mac)
                ndevice.save()
                
                z = AddDeviceTracker(user_mac=user_mac, agent=nagent)
                z.save()
                if device_type == "dustbin":
                    # bav = 1000
                    # z = dustbin(device = ndevice, bin_total_volume=data["bin_total_volume"], bin_total_height=data["bin_total_height"], bin_avai_volume=bav)
                    z = dustbin(device = ndevice, bin_total_volume=data["bin_total_volume"], bin_total_height=data["bin_total_height"], bin_avai_volume=data["bin_avai_volume"])
                    z.save()
                    ds = dustbinserializer(z)
                    dat = ds.data
                elif device_type == "waterpoint":
                    z = waterpoint(device=ndevice, total_water_capacity=data["total_water_capacity"], water_available=data["water_available"])
                    z.save()
                    ws = waterpointserializer(z)
                    dat = ws.data

                elif device_type == "smarttoilet":
                    z = smarttoilet(device=ndevice, waterlevel=data["waterlevel"], description = data["description"])
                    z.save()
                    ws = smarttoiletserializer(z)
                    dat = ws.data                  
                    print(dat)
                    print("printing")
                else:
                    msg = {
                        "resp":"fail",
                        "msg":"invalid device type"
                    }
                    ndevice.delete()
                    z.delete()
                    return Response(msg, status=status.HTTP_400_BAD_REQUEST)
                s = deviceserializer(ndevice)
                dat.update(s.data)
                return Response(dat, status=status.HTTP_200_OK)
            
        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

def alldeviceweb(request):
    d = device.objects.all()
    d = device.objects.all()
    return render(request, "device/alldevice.html", {
        "device":reversed(d)
    })

