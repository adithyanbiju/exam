# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/














#settings
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles','blogs','accounts','rest_framework.authtoken','rest_framework'
# ]
# AUTH_USER_MODEL="accounts.CustomUser"
#
# import os
# MEDIA_ROOT=os.path.join(BASE_DIR,'media')
# MEDIA_URL="/media/"

# models of accounts abstract class

# from django.db import models
#
# from django.contrib.auth.models import AbstractUser
# class CustomUser(AbstractUser):
#     phone=models.CharField(max_length=20)
#     bio=models.TextField()
#
#     def __str__(self):
#         return self.email


# serializer

# from rest_framework import serializers
# from accounts.models import CustomUser
#
# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=CustomUser
#         fields = ['username','password','email','phone','bio']
#     def create(self, validated_data):
#         u=CustomUser.objects.create_user(**validated_data)
#         u.save()
#         return u

# views of accounts


from django.shortcuts import render
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.response import Response
#
# from accounts import serializers
# from accounts.serializers import CustomUserSerializer
# from rest_framework import status
# from rest_framework.views import APIView


# Create your views here.

# class RegisterAPI(APIView):
#     def post(self,request):
#         serializer_instance = CustomUserSerializer(data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#              return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class LogoutAPI(APIView):
#     authentication_classes = [TokenAuthentication]
#     def get(self,request):
#         request.user.auth_token.delete()
#         return Response({"message":"Logout successfully"},status=status.HTTP_201_CREATED)

# signals

# from django.dispatch import receiver
#
# from accounts.models import CustomUser
# from django.db.models.signals import post_save
#
#
# @receiver(post_save,sender=CustomUser)
# def show_message(sender,instance,created,**kwargs):
#     if created:
#         print("welcome")

# app.py

# from django.apps import AppConfig
#
#
# class AccountsConfig(AppConfig):
#     name = 'accounts'
#     def ready(self):
#         import accounts.signals

# urls

# from django.contrib import admin
# from django.urls import path,include
#
# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('accounts/',include('accounts.urls')),
#     path('blogs/',include('blogs.urls')),
# ]

# # main urls
# from django.contrib import admin
# from django.urls import path,include
#
# urlpatterns = [
#     path('admin/',admin.site.urls),
#     path('accounts/',include('accounts.urls')),
#     path('blogs/',include('blogs.urls')),
#
# ]

# models of blogs

# from django.db import models
#
# from accounts.models import CustomUser
#
#
# # Create your models here.
# class Post(models.Model):
#     title=models.CharField(max_length=20)
#     content=models.TextField()
#     created=models.DateTimeField(auto_now_add=True)
#     author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

# serializers of blogs

# from rest_framework import serializers
# from blogs.models import Post
#
#
# class PostSerializer(serializers.ModelSerializer):
#     author=serializers.StringRelatedField()
#     class Meta:
#         model = Post
#         fields = "__all__"
#
#         read_only_fields=['id','created','author']
#
# permissions of blogs

# from rest_framework.permissions import BasePermission
#
#
# class IsAuthorReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method == "GET":
#
#             return True
#
#         return request.user.is_authenticated
#
#     def has_object_permission(self, request, view, obj):
#         return obj.author==request.user

# app of blogs
# from django.apps import AppConfig
#
#
# class BlogsConfig(AppConfig):
#     name = 'blogs'

# views of blogs

# from django.db.models import Model
# from django.shortcuts import render, get_object_or_404
# from rest_framework import status
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from blogs.permissions import IsAuthorReadOnly
# from blogs.serializers import PostSerializer
# from blogs.models import Post
#
#
# # Create your views here.
# class BlogListCreate(APIView):
#     authentication_classes = {TokenAuthentication}
#     permission_classes = [IsAuthorReadOnly]
#     def get(self,request):
#         p=Post.objects.all()
#         serializer_instance=PostSerializer(p,many=True)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer_instance=PostSerializer(data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save(author=request.user)
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)
# class BlogRetrieveUpdateDelete(APIView):
#     authentication_classes = {TokenAuthentication}
#     permission_classes = [IsAuthorReadOnly]
#     def get(self,request,pk):
#         p=get_object_or_404(Post,id=pk)
#         serializer_instance=PostSerializer(p)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         p = get_object_or_404(Post, id=pk)
#         serializer_instance=PostSerializer(instance=p,data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save(author=request.user)
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         p = get_object_or_404(Post,id=pk)
#         p.delete()
#         return Response({"message":"deleted successfuly"},status=status.HTTP_204_NO_CONTENT)

# urls of blogs

# from django.urls import path
#
# from blogs import views
#
# urlpatterns = [
#     path('posts',views.BlogListCreate.as_view()),
#     path('posts/<int:pk>',views.BlogRetrieveUpdateDelete.as_view()),
#
# ]

# admin
# admin.site.register(Post)u = User.objects.create_user(**validated_data)
#         u.save()
#         return ufrom django.contrib.auth.models import User