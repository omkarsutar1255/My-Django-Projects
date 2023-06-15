from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Student(models.Model):
    Name = models.CharField(max_length=20, null=False)
    Email = models.EmailField(max_length=50, blank=False, unique=True,
                              error_messages={'required': 'Please provide your email address.',
                                              'unique': 'An account with this email exist.'}, )
    # Phone_no = models.IntegerField()
    Phone_no = PhoneNumberField(blank=False, unique=True)
    Address = models.CharField(max_length=40)

    # def save
    # validate email
    # Phone no validation
    def save(self, *args, **kwargs):
        # super().full_clean()
        # we can only allow certain domain
        if self.Email.endswith('@gmail.com'):
            print("Email name = ", self.Email)
            super().save(*args, **kwargs)
        else:
            print("else-Email name = ", self.Email)
            super().save(*args, **kwargs)


# Log in, log out, log in failed, pre save, post save, pre delete, post delete, data connection, pre init, post init.
# Main logs e.g. Who created row, updated data, main history table, notification send
@receiver(post_save, sender=Student)
def new_obj(sender, instance, **kwargs):
    print("Student Obj Created")
    print(sender, instance, kwargs)
