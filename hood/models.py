from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.fields import related
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create models here.
class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # save location
    def save_location(self):
        self.save()
    def __str__(self):
        return self.name

class NeighbourHood(models.Model):
    hood_image = CloudinaryField("hood_image", null=True)
    name = models.CharField(max_length=50)
    hood_description = models.TextField(max_length=1000, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def create_neighborhood(self):
        self.save()
    @classmethod
    def delete_neighbourhood(cls, id):
        cls.objects.filter(id=id).delete()
    @classmethod
    def update_neighbourhood(cls, id):
        cls.objects.filter(id=id).update()
    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood
    
    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = CloudinaryField('image')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True , related_name='members')
    bio = models.TextField(max_length=500,  null=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} profile'
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    post_image = CloudinaryField('post_image', null=True)
    post_description = models.TextField(max_length=1000)
    hood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True, related_name='hood_post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-pk']
    def __str__(self):
        return f'{self.title} Post'
    def delete_post(self):
        self.delete()
    def create_post(self):
        self.save()
    def update_post(self):
        self.update()

class Business(models.Model):
    business_photo = CloudinaryField("image",null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']
    def __str__(self):
        return f'{self.name} Business'
    def create_business(self):
        self.save()
    def delete_business(self):
        self.delete()
    def update_business(self):
        self.update()
    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business
    @classmethod
    def find_business(cls, id):
        business = cls.objects.get(id=id)
        return business





