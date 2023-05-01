from django.db import models

class Department(models.Model):
    title=models.CharField(max_length=50)
    def __str__(self):
      return self.title
    class Meta:
        ordering=['-title']
class Record(models.Model):
    first_name=models.CharField(max_length=50, null=True, blank=True)
    last_name=models.CharField(max_length=50, null=True, blank=True)
    departments=models.ForeignKey(Department,related_name="staff", on_delete=models.SET_NULL, null=True)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=50, null=True, blank=True)
    phone=models.CharField(max_length=50, null=True, blank=True)
    city=models.CharField(max_length=50, null=True, blank=True)
    state=models.CharField(max_length=50 , null=True, blank=True)
    zipcode=models.CharField(max_length=50 , null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='Records'
        ordering=['-created_at']
    def __str__(self):
        return f'{self.first_name}{self.last_name}'