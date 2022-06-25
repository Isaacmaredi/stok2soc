from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from soc_members.models import Member


@receiver(post_save, sender=User)
def create_member_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
        
    
@receiver(post_save, sender=User)
def save_member_profile(sender, instance, **kwargs):
    instance.member.save()