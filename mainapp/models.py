from django.db import models


#contact us form model
class ContactUs(models.Model):
    name = models.CharField (max_length=32, blank=True, null=True)
    email = models.CharField (max_length=32, blank=True, null=True)
    message = models.TextField ()
    created_at = models.DateTimeField (auto_now_add=True)
    updated_at = models.DateTimeField (auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

#Booking models for saving user bookings information
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    person_name = models.CharField(max_length=32, default="Anon person")
    person_number = models.CharField(max_length=32, default=000)
    person_email = models.EmailField(blank=True, null=True)
    guest_count = models.CharField(max_length=32)
    guest_table = models.CharField(max_length=32)
    requested_date = models.DateField()
    requested_time = models.TimeField()


    def __str__(self):
        return f"{self.user} - {self.person_name} - {self.requested_date} - {self.requested_time}" 

