from rest_framework.serializers import ModelSerializer
from .models import UserInfo, UserFaceImage, UserTesteImage



class UserInfoListSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class UserFaceImageSerializer(ModelSerializer):
    class Meta:
        model = UserFaceImage
        fields = '__all__'



class UserTesteImageSerializer(ModelSerializer):
    class Meta:
        model = UserTesteImage
        fields = '__all__'



class UserInfoSerializer(ModelSerializer):
    image = UserFaceImageSerializer(many=True, read_only=True)

    class Meta:
        model = UserInfo
        fields = '__all__'
    extra_kwargs = {
        'password': {'required': False},
        'account': {'required': False},
        'phone': {'required': False},
        'email': {'required': False},
        'update_time': {'required': False},
        'date_time': {'required': False}
    }


