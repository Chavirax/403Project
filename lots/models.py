from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class ParkingCategory(models.Model):
    description = models.CharField(max_length=20)

    def __str__(self) :
        return (self.description)

class Vehicle(models.Model) :
    l_number = models.OneToOneField(ParkingCategory, models.CASCADE)
    model = models.CharField(max_length=50)
    make = models.IntegerField(default=0)
    cost = models.DecimalField(max_digits=8, decimal_places=2) 
    is_active = models.BooleanField(default=True)
    leave_date = models.DateField(default=datetime.today, blank=True)

    def __str__ (self):
        return (self.model)

  
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)    
    phone = models.CharField(max_length=13, blank=True)
    customer_id = models.ManyToManyField(Vehicle, blank=True)

    def __str__(self):
        return (self.full_name)

    @property # this is not part of the table
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    #override the save method
    def save(self):
        self.first_name = self.first_name.upper()
        super(Customer, self).save() # Call the "real" save() method.          

class Contact_Information(models.Model):
    contact_phone = models.CharField(max_length=10)
    def __str__(self):
        phone = '(' + self.contact_phone[0:3] + ') ' + self.contact_phone[3:6] + '-' + self.contact_phone[6:10]  
        return phone        
class Skill(models.Model) :
    description = models.CharField(max_length=30)

    def __str__(self):
        return (self.description)
class Employee(models.Model):
    TITLE = (
        ('Ms.', 'MISS'),
        ('Mr.', 'MR.'),
        ('Mrs.', 'MRS.'),
        ('Mx', 'MX'),
    )

    emp_first = models.CharField(max_length=20)
    emp_last = models.CharField(max_length=20)
    emp_title = models.CharField(max_length=4, choices=TITLE, null=True, blank=True)
    emp_state = models.ForeignKey('State', null=True, blank=True, on_delete=models.SET_NULL)
    contact_information = models.OneToOneField(Contact_Information, on_delete=models.CASCADE)
    emp_skills = models.ManyToManyField('Skill', through='Skill_Level')

    def __str__(self):
        return (self.emp_first + " " + self.emp_last)   
class State(models.Model) :
    state_abbrev = models.CharField(max_length=2)
    state_description = models.CharField(max_length=30)

    def __str__(self):
    
        return (self.state_description)    

 #Add this class
class Skill_Level(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    skill_rating = models.PositiveIntegerField(default=3, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return '%s %s %s %i' %(self.employee.emp_first,self.employee.emp_last,self.skill.description,self.skill_rating)