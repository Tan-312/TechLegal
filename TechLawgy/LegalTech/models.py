from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


'''
class case(models.Model):
    

    name = models.CharField(max_length=500)
    datasource_id = models.CharField(max_length=500)
    datasource_type = models.CharField(max_length=500)

    datasource=models.ForeignKey(DataSource,blank=True,null=True,on_delete=models.CASCADE, related_name="datasource")


    def __str__(self):
        return f"{self.id} - {self.name} to {self.datasource_type}"

        '''





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)
        
    instance.profile.save()


class Cases(models.Model):
    
    user_name=models.ForeignKey(Profile,blank=True,null=True,on_delete=models.CASCADE, related_name="user_name")
    payee_name=models.CharField(max_length=100, blank=True)
    payee_address=models.CharField(max_length=500, blank=True)
    payer_name=models.CharField(max_length=100, blank=True)
    payer_address=models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"case id :{self.id} user id:{self.user_name.id} name :{self.user_name.user} - payer name :{self.payer_name}"

