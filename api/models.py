from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify
from django.db.models.signals import post_save
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='users/iamges/',blank=True,null=True)
    email=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)
    def __str__(self):
        return self.slug
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.Case,blank=True,null=True)
    content=models.TextField()
    image=models.ImageField(upload_to='post/iamges/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.Case,blank=True,null=True)
    content=models.TextField()
    image=models.ImageField(upload_to='comment/iamges/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Follow(models.Model):
    user=models.ForeignKey(User,on_delete=models.Case,blank=True,null=True)
    profile=models.ForeignKey(Profile,on_delete=models.PROTECT,blank=True,null=True)
    follow=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    def __str__(self):
        return str(self.user.username)
    class Meta:
        unique_together=(('user','profile'))
        index_together=(('user','profile'))

class Like(models.Model):
     user=models.ForeignKey(User,on_delete=models.Case,blank=True,null=True)
     comment=models.ForeignKey(Comment,on_delete=models.PROTECT,blank=True,null=True)
     post=models.ForeignKey(Post,on_delete=models.PROTECT,blank=True,null=True)
     like=models.IntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(1)])
     def __str__(self):
        return str(self.user.username)
     class Meta:
        unique_together=(('user','comment','post'))
        index_together=(('user','comment','post'))





