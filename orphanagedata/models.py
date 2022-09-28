from django.db import models

# Create your models here.
class NewRegister(models.Model):
    p_id = models.AutoField( primary_key= True )
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    def __str__(self):
        return self.email
class NewRegistration(models.Model):
    p_id = models.AutoField( primary_key= True )
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    user_image=models.ImageField(upload_to='userimages/')
    def __str__(self):
        return self.email
class NewOrphan(models.Model):
    p_id = models.AutoField( primary_key= True )
    
    orphanid=models.CharField(max_length=100)
    dateofjoining=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    middlename=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    religion=models.CharField(max_length=100)
    height=models.CharField(max_length=100)
    haircolor=models.CharField(max_length=100)
    eyecolor=models.CharField(max_length=100)
    otherdescription=models.CharField(max_length=100)
    y1=models.CharField(max_length=100)
    y2=models.CharField(max_length=100)
    y3=models.CharField(max_length=100)
    y4=models.CharField(max_length=100)
    y5=models.CharField(max_length=100)
    otherdescriptions=models.CharField(max_length=100)
    childimage=models.ImageField(upload_to='childimages/')
    
    def __str__(self):
        return self.orphanid
class AddEvents(models.Model):
    p_id = models.AutoField( primary_key= True )
    eventtype=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    eventdate=models.CharField(max_length=100)
    eventtime=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    organizer=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    eventimg=models.ImageField(upload_to='eventimages/')
    def __str__(self):
        return self.name
class AddDonors(models.Model):
    p_id = models.AutoField( primary_key= True )
    amount=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    note=models.CharField(max_length=100)
    cardno=models.CharField(max_length=100)
    cvv=models.CharField(max_length=100)
    expirydate=models.CharField(max_length=100)
    def __str__(self):
        return self.email
class RequestChildren(models.Model):
    p_id = models.AutoField( primary_key= True )
    user_id=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    user_image=models.ImageField(upload_to='requestedchild/')
    child_id=models.CharField(max_length=100)
    orphanid=models.CharField(max_length=100)
    orphan_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    def __str__(self):
        return self.email