from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo, UserFaceImage, UserTesteImage, userfaceimage_delete, usertestimage_delete
from .serializers import UserInfoSerializer, UserFaceImageSerializer, UserTesteImageSerializer
from django.http import Http404
import json



class User_List_api(APIView):
    """list all user or create a new user"""
    def get(self, request, format=None):
        user = UserInfo.objects.all()
        serializer = UserInfoSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
class User_Detail_api(APIView):
    """Retrieve, update or delete a user instance."""
    
    def get(self, request, account, format = None):
        try:
            user = UserInfo.objects.get(account = account)
            serializer = UserInfoSerializer(user)
            return Response(serializer.data)
        except UserInfo.DoesNotExist:
            raise Http404
        
    
    def put(self, request, account, format = None):
        user = self.get_object(account = account)
        serializer = UserInfoSerializer(user, data = request.data)
        if serializer.is_valid():
            imagelist = dict(request.data)['image']
            old_images = UserFaceImage.objects.all()
            for old_image in old_images:
                userfaceimage_delete(instance = old_image)
                old_image.delete()
                
            for image in imagelist:
                user_image = user.images.create(image = image)
                user_image.image.save(image.name, image)
                serializer.save()
            return Response(status = status.HTTP_200_OK)
        return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
    

    def post(self, request, account,format = None):
        user = UserInfo.objects.get(account)
        serializer = UserInfoSerializer(user)
        """get the account and password"""
        password = request.data.get('password')
        if serializer.is_valid():
            if user.password == password:
                return Response(request.data, status = status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, account, format = None):
        user = UserInfo.objects.get(account)
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    

