from locale import strxfrm
from pyexpat import model
# import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )
    # ROLE = (
    #     ('User','User')
    #     ('doctor','doctor')

    # )
    gender=models.CharField(max_length=30,choices=GENDER)
    phone=models.IntegerField(null=True,blank=False)
    # role=models.CharField(max_length=30,choices=ROLE)


class PredictionTable(models.Model):
    
    # #
    # # id = models.AutoField(primary_key=True)
    # id = models.AutoField(primary_key=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Age = models.CharField(max_length=100)
    Sex = models.CharField(max_length=100)
    Excessive_urine = models.CharField(max_length=100)
    Excessive_thirst = models.CharField(max_length=100)
    Sudden_Weight_loss = models.CharField(max_length=100)
    Weakness= models.CharField(max_length=100)
    Excessive_eating = models.CharField(max_length=100)
    Yeast_infection = models.CharField(max_length=100)
    Visual_blurring = models.CharField(max_length=100)
    Itching = models.CharField(max_length=100)
    Irritability = models.CharField(max_length=100)
    Delaed_healing = models.CharField(max_length=100)
    Partial_paresis = models.CharField(max_length=100)
    Muscle_stiffiness = models.CharField(max_length=100)
    Hair_loss = models.CharField(max_length=100)
    Obesity = models.CharField(max_length=100)
    


    def __str__(self):
        return self.Age

    

#     class PredictionTable(models.Model):
#     Age = models.CharField(max_length=100)
#     Sex = models.CharField(max_length=100)
#     Excessive_urine = models.CharField(max_length=100)
#     Excessive_thirst = models.CharField(max_length=100)
#     Sudden_Weight_loss = models.CharField(max_length=100)
#     Weakness= models.CharField(max_length=100)
#     Excessive_eating = models.CharField(max_length=100)
#     Yeast_infection = models.CharField(max_length=100)
#     Visual_blurring = models.CharField(max_length=100)
#     Itching = models.CharField(max_length=100)
#     Irritability = models.CharField(max_length=100)
#     Delaed_healing = models.CharField(max_length=100)
#     Partial_paresis = models.CharField(max_length=100)
#     Muscle_stiffiness = models.CharField(max_length=100)
#     Hair_loss = models.CharField(max_length=100)
#     Obesity = models.CharField(max_length=100)


#     def __str__(self):
#         return self.n1

# class DoctorTable(models.Model):
#     n1 = models.CharField(max_length=100)
#     n2 = models.CharField(max_length=100)



#     def __str__(self):
#         return self.n1      
# class UserInput(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80))
#     email = db.Column(db.String(120))
#     message = db.Column(db.String(120))
    

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)   