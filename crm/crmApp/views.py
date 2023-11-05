from django.shortcuts import render,redirect
from crmApp.models import CV
from django.contrib import messages
from .forms import CVForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

#Login
def login_page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect("/login/")
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid')
            return redirect('/login/')
        
        else:
            login(request,user)
            messages.success(request,"Successfull login!")
            return redirect('/home/')

    return render(request,"login.html")


#Logout
def logout_page(request):
    logout(request)
    return redirect('/login/')


#Register
def register_page(request):
    if request.method == "POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=User.objects.filter(username=username)
        
        if user.exists():
            messages.error(request,'Username already taken')
            return redirect('/register/')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
                    )
        
        user.set_password(password)
        user.save()
        messages.success(request,'You have successfully registered!')

        return redirect('/register/')

    return render(request,"register.html")





# <-------------------------------CRUD OPERATIONS------------------------------->


# CV Record
def record(request,id):
        cv_data=CV.objects.get(mobID=id)
        return render(request,'record.html', {'cv_data' : cv_data})


#Show
def home(request):
        cv_data = CV.objects.all()
        return render(request, 'home.html', {'cvdata' : cv_data})


#Add Cv
class add_cv(View):    
    def get(self,request):
        cv_data = CVForm()
        return render(request, 'add-cv.html', {'form' : cv_data})
    
    def post(self,request):
        cv_data = CVForm(request.POST,request.FILES)
        if cv_data.is_valid():
            cv_data.save()
            messages.success(request, 'Cv is added successfully !')
            return redirect('/home')
        else:
            return render(request, 'add-cv.html', {'cvdata' : cv_data})     

    
#Update Cv
class update_cv(View):
    def get(self,request,id):
        cv_data = CV.objects.get(mobID=id)
        form = CVForm(instance=cv_data)
        return render(request, 'update-cv.html', {'form' : form})       
    
    def post(self,request,id):
        cv_data = CV.objects.get(mobID=id)
        form = CVForm(request.POST,request.FILES,instance=cv_data)        
        if form.is_valid():
            form.save()
            messages.success(request, 'CV is updated successfully !')
            return redirect('/home')
        return render(request, 'home.html')


#Delete Cv
class delete_cv(View):
    def post(self,request):
        cvdata = request.POST
        id = cvdata.get('id')
        cv_data = CV.objects.get(mobID=id)
        messages.success(request, 'CV is deleted successfully !')
        cv_data.delete()
        return redirect('/home')