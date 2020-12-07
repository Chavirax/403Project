from django.contrib import admin

# Register your models here.
from .models import Customer, Vehicle, ParkingCategory, Contact_Information, Employee, State, Skill,Skill_Level

# Register your models here.
admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(ParkingCategory)  
admin.site.register(Contact_Information)
admin.site.register(Employee)  
admin.site.register(State)  
admin.site.register(Skill)
admin.site.register(Skill_Level)

