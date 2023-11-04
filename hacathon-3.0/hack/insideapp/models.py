from django.db import models
GENDER_CHOICES={
                ("Male","Male"),
                ("Female","Female"),
                ("other","other")
        }
STATE_CHOICES={
        ("Punjab","Punjab"),
        ("Delhi","Delhi"),
        ("West Benagal","West Bengal")
}       
CITY_CHOICES={
        ("Patiala","Patiala"),
        ("Delhi","Delhi"),
        ("kolkota","kolkota")
}
# Create your models There.
class useraccountregister(models.Model):
        worker_id= models.AutoField(primary_key=True)
        Firstname=models.CharField( max_length=50)
        Lasttname=models.CharField( max_length=50)
        Username=models.CharField(max_length=50)
        Address=models.CharField(max_length=50)
        Gender=models.CharField(max_length=20,choices=GENDER_CHOICES,default='Male')
        State=models.CharField(max_length=20,choices=STATE_CHOICES,default="Punjab")
        city=models.CharField(max_length=20,choices=CITY_CHOICES,default="patiala")
        pincode=models.IntegerField()
        email=models.EmailField(max_length=254)
        phone=models.CharField( max_length=50,null=True)
        password=models.CharField(max_length=50,null=True)
class workeraccountregister(models.Model):
        Firstname=models.CharField( max_length=50)
        Lasttname=models.CharField( max_length=50)
        Username=models.CharField(max_length=50)
        Address=models.CharField(max_length=50)
        Gender=models.CharField(max_length=20,choices=GENDER_CHOICES,default='Male')
        State=models.CharField(max_length=20,choices=STATE_CHOICES,default="Punjab")
        city=models.CharField(max_length=20,choices=CITY_CHOICES,default="patiala")
        pincode=models.IntegerField()
        email=models.EmailField(max_length=254)
        phone=models.CharField(max_length=50,null=True)
        password=models.CharField(max_length=50,null=True)
class loginpage(models.Model):
        Username=models.CharField(max_length=50)
        password=models.CharField(max_length=50)
class order(models.Model):
        customer_name=models.CharField( max_length=50)
        order_number=models.IntegerField(primary_key=True)
        adress1=models.CharField( max_length=50)
        adress2=models.CharField( max_length=50)
        start_b=models.IntegerField()
        final_b=models.IntegerField()
        path=models.CharField( max_length=50)
        current_b=models.IntegerField(null=True)
        current_center=models.IntegerField(null=True)
        current_status=models.CharField(max_length=50)
class center1(models.Model):
        came_from=models.IntegerField()
        to_go=models.IntegerField()
class center2(models.Model):
        came_from=models.IntegerField()
        to_go=models.IntegerField()
class center3(models.Model):
        came_from=models.IntegerField()
        to_go=models.IntegerField()
class center4(models.Model):
        came_from=models.IntegerField()
        to_go=models.IntegerField()
class center5(models.Model):
        came_from=models.IntegerField()
        to_go=models.IntegerField()
class center6(models.Model):
        came_from=models.IntegerField()
        to_go=models.IntegerField()

 
      
       



        


