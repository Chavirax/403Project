
from django.shortcuts import render
from django.http  import HttpResponse
from lots.models import Employee
from lots.models import State
from lots.models import Contact_Information

# Create your views here.

def showLotsPageView(request):
    return render(request, 'lots/showLots.html')

def showULotsPageView(request):
    context = {
        "area": "Undergraduate students may park in 'U' Lots, at no charge, if their vehicle is registered."
    }
    return render(request, 'lots/displayLots.html', context)

def showYLotsPageView(request):
    context = {
        "area": "Undergraduate students may choose to pay $60 per semester to park in Y Lots."
    }
    return render(request, 'lots/displayLots.html', context)

    
def showALotsPageView(request):
    context = {
        "area": "Students should never park in A Lots."
    }
    return render(request, 'lots/displayLots.html', context)


    
def showBLotsPageView(request):
    context = {
        "area": "If you have contracted to live on campus, your parking privilege will change automatically on the first day of that contract to B Lot for Heritage"
    }
    return render(request, 'lots/displayLots.html', context)


def showCLotsPageView(request):
    context = {
        "area": "If you have contracted to live on campus, your parking privilege will change automatically on the first day of that contract to B Lot for Helaman Halls "
    }
    return render(request, 'lots/displayLots.html', context)


def displayLotsPageView(request):
    context = {
        "area" : "Lots!"
    }
    return render(request, 'lots/displayLots.html', context)

def findEmpPageView(request) :
    return render(request, 'lots/searchEmps.html')

def searchEmpPageView(request) :
    sFirst = request.GET['emp_first']
    sLast = request.GET['emp_last']
    data = Employee.objects.filter(emp_first=sFirst, emp_last=sLast)

    if data.count() > 0:
        context = {
            "our_emps" : data
        }
        return render(request, 'lots/displayEmps.html', context)
    else:
        return HttpResponse("Not found")


def empPageView(request) :
    data = Employee.objects.all()

    context = {
        "our_emps" : data
    }
    return render(request, 'lots/displayEmps.html', context)

def addEmpPageView(request):
    states = State.objects.all() 
    context = {
        "states": states,
        "titles" : [
                    ('Ms.', 'MISS'),
                    ('Mr.', 'MR.'),
                    ('Mrs.', 'MRS.'),
                    ('Mx', 'MX')
                    ]
    }    

    return render(request, 'lots/addEmps.html', context)   

def storeEmpPageView(request):
#Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new employee object from the model (like a new record)
        new_employee = Employee()

        #Store the data from the form to the new object's attributes (like columns)
        new_employee.emp_first = request.POST.get('emp_first')
        new_employee.emp_last = request.POST.get('emp_last')
        new_employee.emp_title = request.POST.get('emp_title')

        #Get all of the State objects (record or records) for the current employee state
        new_state = State.objects.get(state_abbrev = request.POST.get('emp_state'))

        #Create a new Contact Information object (record)
        new_contact = Contact_Information()

        #Store the data from the form to the contact phone attribute (column) 
        new_contact.contact_phone = request.POST.get('contact_info')

        #Save the contact information record which will generate the autoincremented id
        new_contact.save()

        #Store the newly created contact information id (object or record reference) to the employee record
        new_employee.contact_information = new_contact

        #Store the State reference found to the employee state
        new_employee.emp_state = new_state

        #Save the employee record
        new_employee.save()

        #Make a list of all of the employee records and store it to the variable
        data = Employee.objects.all()

        #Assign the list of employee records to the dictionary key "our_emps"
        context = {
            "our_emps" : data
        }
    return render(request, 'lots/displayEmps.html', context) 

def updateEmpPageView(request):
    sFirst = request.GET['emp_first']
    sLast = request.GET['emp_last']
    sNewLast = request.GET['new_last_name']

    #Find the employee record
    emp = Employee.objects.get(emp_first=sFirst, emp_last=sLast)  
    emp.emp_last = sNewLast  
    emp.save()  
    data = Employee.objects.all()

    #Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "our_emps" : data
    }
    return render(request, 'lots/displayEmps.html', context )


def deleteEmpPageView(request):
    emp = Employee.objects.filter(emp_first=request.GET['emp_first'], emp_last=request.GET['emp_last']).delete()
    data = Employee.objects.all()

    #Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "our_emps" : data
    }
    return render(request, 'lots/displayEmps.html', context) 

