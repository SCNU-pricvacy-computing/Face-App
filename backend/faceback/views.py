from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInfo, UserFaceImage, UserTesteImage, userfaceimage_delete, usertestimage_delete
from .serializers import UserInfoSerializer, UserFaceImageSerializer, UserTesteImageSerializer
from django.http import Http404
import json
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# import fr_algorithms.siamese as siamese
# from fr_algorithms.facenet.predict import FaceNet_recognize_organization
# from fr_algorithms.deepface import DeepFace_recognize_organization



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
    
class Login_api(APIView):


    def get(self, request):
        user = UserInfo.objects.all()
        serializer = UserInfoSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        account = request.data.get('account')
        password = request.data.get('password')

        if account is None or password is None:
            return Response({'error': 'Please provide both account and password'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            user = UserInfo.objects.get(account = account)
            if password == user.password:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'account': account,
                })
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"the error is {e}")
            return Response({'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class Register_api(APIView):
    def get(self, request):
        user = UserInfo.objects.all()
        serializer = UserInfoSerializer(user, many=True)
        return Response(serializer.data)
        



    def post(self, request):
        account = request.data.get('account')
        olduser = UserInfo.objects.filter(account = account)
        if olduser:
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            serializer = UserInfoSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"success":"register success"}, status = status.HTTP_201_CREATED,data=serializer.data)
            else:
                return Response({'error': 'register false 45', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


                
    



class TestUserface(APIView):
    def get(self,request,format = None):
        imgs = UserTesteImage.objects.all()
        serializer = UserTesteImageSerializer(imgs, many=True)
        return Response(serializer.data)
    

    def post(self,request, account, format=None):
        # user post the face img
        # get user's identity
        account = request.data.get('account')
        try:
            user = UserInfo.objects.get(account = account)
        except UserInfo.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        
        test_iamge_req = request.FILES.get('test_image')
        old_iamges = user.test.all()
        for images in old_iamges:
            usertestimage_delete(instance = images)
            images.delete()

        test_image = user.test.create()
        test_image.test_image.save(test_iamge_req.name, test_iamge_req)

        # test the face img
        result = Facenet_recognition(str(account))
        if result != "can't recognize identity" and result != "can't recognize face":
            detected_user = UserInfo.objects.get(account = int(result))
            result = detected_user.account

        result = {"user":result}
        return Response(json.loads(result), status = status.HTTP_200_OK)




