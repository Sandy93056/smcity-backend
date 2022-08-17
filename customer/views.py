from tracker.models import CreateUserTracker
from customer.serializers import user_profile_serializer
from customer.models import gbvariables, user_profile
from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.shortcuts import render
import django.contrib.auth
# User = django.contrib.auth.get_user_model()
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# user = User.objects.create_user('username', password='userpassword')
# user.is_superuser = False
# user.is_staff = False
# user.save()
# Create your views here.

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from charzer import settings



class user_register(APIView):

    def put(self, request):
        try:
            username = request.data.get('username')
            if User.objects.filter(username=username).exists():

                msg = {
                    "msg": "username-not-available",
                    "resp":"stop"
                }
                return Response(msg)
                pass
            else:
                msg = {
                    "msg": "username-available",
                    "resp":"proceed"
                }

                return Response(msg)

        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


    def post(self,request):
        try:
            gusername = request.data.get('username')
            if User.objects.filter(username=gusername).exists():
                msg = {
                    "msg": "not-available",
                    "resp":"username-not-available"
                }

                return Response(msg)

            else:
                username = request.data.get('username')
                password = request.data.get('password')

                try:
                    user = User.objects.create_user(username, password=password)
                    user.is_superuser = False
                    user.is_staff = False
                    user.save()
                    u = user_profile(user=user, user_name=user.username)
                    u.save()
                    u.is_verified = True
                    u.save()

                    # print(token.key)
                except Exception as e:
                    return Response({"msg":f"{e}","resp":"fail"})
                token = Token.objects.create(user=user)
                # print(token)
                # print(type(token))
                return Response({"msg":"created user successfully","resp":"successful","token": str(token)})

        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class user_profile_api(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes  = [IsAuthenticated]

    # def get(self, request):
    #     u = user_profile.objects.get(user=request.user)

    #     serializer = user_profile_serializer(u)
    #     return Response(serializer.data)

    def get(self, request):
        try :
            u = user_profile.objects.get(user=request.user)
            serializer = user_profile_serializer(u)
            dat = serializer.data
            dat["user_photo"] = settings.website_name + dat["user_photo"]
            return Response(dat)
        except Exception as e:
            return Response(serializer.errors, status=status)
    def post(self, request):
        try:
            user = user_profile.objects.get(user=request.user)
            serializer = user_profile_serializer(user,data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)


# from django.http import JsonResponse
# class user_login(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes  = [IsAuthenticated]

#     def get(self, request):
#         # username = request.data.get('username')
#         # password = request.data.get('password')
#         msg = {
#             "hello":"world"
#         }
#         # return HttpResponse('{"hello":"world"',content_ty)
#         return Response(msg)

# from rest_framework.decorators import api_view

# @api_view()
# def temp(request):
#     u = user_profile.objects.all()
#     st = user_profile_serializer(u)
#     return Response(st.data)


class UserRegisterRestricted(APIView):

    def post(self,request):
        try:
            user_mac = request.data["android_mac"]
            create_count = CreateUserTracker.objects.filter(user_mac=user_mac).count()
            limit = gbvariables.objects.all().first().no_of_allowed_registerUser
            if create_count>limit:
                msg ={
                    "resp":"fail",
                    "msg": "you are creating too much account "
                }
                return Response(msg, status=status.HTTP_429_TOO_MANY_REQUESTS)
            else:
                pass
            gusername = request.data.get('username')

            if User.objects.filter(username=gusername).exists():
                msg = {
                    "msg": "not-available",
                    "resp":"username-not-available"
                }

                return Response(msg)

            else:
                username = request.data.get('username')
                password = request.data.get('password')

                try:
                    user = User.objects.create_user(username, password=password)
                    user.is_superuser = False
                    user.is_staff = False
                    user.save()
                    u = user_profile(user=user, user_name=user.username)
                    u.save()
                    u.is_verified = True
                    u.save()
                    z = CreateUserTracker(user_mac=user_mac)
                    z.save()
                    # print(token.key)
                except Exception as e:
                    return Response({"msg":f"{e}","resp":"fail"})
                token = Token.objects.create(user=user)
                # print(token)
                # print(type(token))
                return Response({"msg":"created user successfully", "resp":"successful", "token": str(token)})

        except Exception as e:
            msg ={
                "resp":"fail",
                "msg": f"{e}"
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)