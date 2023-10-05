from django.db import models
import uuid
from django.core.files.storage import FileSystemStorage
from django.dispatch import receiver
from back.settings import MEDIA_ROOT, MEDIA_URL
from django.db.models.signals import pre_delete

# Create your models here.

image_storage = FileSystemStorage(location = MEDIA_ROOT, base_url = MEDIA_URL)

class UserInfo(models.Model):

    class Meta:
        db_table = 'userinfo'
        verbose_name = 'userinformation'
        verbose_name_plural = 'userinformation'



    account = models.CharField(verbose_name='account',max_length=30)
    password = models.CharField(max_length=30, verbose_name='password')
    update_time = models.DateTimeField(auto_now=True, verbose_name='update_time')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='date_time')




def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.account, filename)

def test_directory_path(instance, filename):
    return 'test_{0}/{1}'.format(instance.test.account, filename)



class UserFaceImage(models.Model):
    class Meta:
        db_table = 'userfaceimage'
        verbose_name = 'userfaceimage'
        verbose_name_plural = 'userfaceimage'

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='images')
    face_image = models.ImageField(upload_to=user_directory_path, verbose_name='face_image',storage=image_storage)

@receiver(pre_delete, sender=UserFaceImage)
def userfaceimage_delete(instace, **kwargs):
    instace.face_image.delete(False)
    


class UserTesteImage(models.Model):
    class Meta:
        db_table = 'usertestimage'
        verbose_name = 'usertestimage'
        verbose_name_plural = 'usertestimage'


    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name ='test')
    test_image = models.ImageField(upload_to=test_directory_path, verbose_name='test_image',storage=image_storage)


@receiver(pre_delete, sender=UserTesteImage)
def usertestimage_delete(instace, **kwargs):
    instace.test_image.delete(False)
