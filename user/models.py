from django.db import models

# Create your models here.
class UserRegister(models.Model):
    Name = models.CharField('姓名',max_length=20)
    Email = models.EmailField('邮箱')
    Password = models.CharField('密码',max_length=20)
    Type = models.IntegerField()
    Sexy = models.CharField('性别',max_length=5)
    CreateDate = models.DateTimeField('创建时间',auto_now_add=True)
    ExpiredDate = models.DateTimeField('修改时间',auto_now=True)
    Image = models.ImageField('头像',upload_to='image',default="image/default.png",max_length=100)


