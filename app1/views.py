from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .models import SignUp,Note
from .forms import UserDetail,CreateUserForm,UserNote
from django.contrib.auth.decorators import login_required




# from .forms import LoginForm

# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')



def userlogin(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(username=email, password=password)
        
		if user is not None:
			login(request,user)
            
			return redirect('profile')
		else:
			messages.info(request, 'Username OR password is incorrect')
			return render(request, 'login.html', {})
	return render(request, 'login.html', {})


def adminlogin(request):

    if request.method=="POST":
        u=request.POST.get("username")
        p=request.POST.get("password")
        user=authenticate(username=u,password=p)
        if user.is_staff:
            login(request,user)
            return redirect("admindashboard")

    
    return render(request,'adminlogin.html',{})

@login_required(login_url='adminlogin')
def admindashboard(request):
    return render(request,'admindashboard.html',{})


def Logout(request):
    logout(request)
    return redirect('home')

def validate(customer):
    
    if len(customer['fn'])==0:
        return 'Please Enter first name....'
    elif len(customer['ln'])==0:
        return 'Please Enter Last name....'
    elif User.objects.filter(email = customer['email']):
        return 'Email Already Registered...'
    elif len(customer['password'])<=6:
        return 'Please Enter password of lenght more tha 6 ....'
    elif 8<len(customer['mob'])>=12 and not customer['mob'].isdigit():
        return 'Please Enter valid phone number....'
    
    elif len(customer['brch'])==0:
        return 'Please Enter Branch....'
    elif len(customer['role'])==0:
        return 'Please Enter Role....'

    return None

       
    return render(request,'signup.html',{'error_message':None})
    


@login_required(login_url='login')
def changepassword(request):
    
    if request.method=="POST":
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request,"Sucessfully changed password!!!")
            return redirect('userdash')
        else:
            messages.info(request,"please give passwords correctly!!!")
            
    fm=PasswordChangeForm(user=request.user)
    return render(request,'changepassword.html',{'form':fm})

@login_required(login_url='login')
def registerPage(request):
    form=CreateUserForm()
    if request.method=="POST":
        
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
            
        else:
            return redirect('home')

    return render(request,'register.html',{'form':form})

@login_required(login_url='login')
def userdetail(request):
    try:
        task=SignUp.objects.get(user=request.user)
        form=UserDetail(instance=task)
    except:
        form=UserDetail()
    if request.method=="POST":
        try:
            form=UserDetail(request.POST,request.FILES,instance=task)
            if form.is_valid():
                form.save()
        except:
            form=UserDetail(request.POST)
            if form.is_valid():
                
                user=request.user
                contact=request.POST['contact']
                branch=request.POST['branch']
                role=request.POST['role']
                SignUp(user=user,contact=contact,branch=branch,role=role).save()
            
        return redirect('profile')
    return render(request,'userdetail.html',{'form':form})


@login_required(login_url='login')
def Profile(request):
    field1=User.objects.get(id=request.user.id)
    try:
        field2=SignUp.objects.get(user=field1)
        data={'field1':field1,'field2':field2}
    except:
        data={'field1':field1,'field2':None}
    
    
    return render(request,'profile.html',data)

@login_required(login_url='login')
def Uploadnotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form=UserNote()
    if request.method=="POST":
        form=UserNote(request.POST,request.FILES)
        if form.is_valid():
            fm=Note()
            fm.user=request.user
            fm.subject=form.cleaned_data['subject']
            fm.branch=form.cleaned_data['branch']
            fm.notesfile=form.cleaned_data['notesfile']
            fm.filetype=form.cleaned_data['filetype']
            fm.description=form.cleaned_data['description']
            fm.save()
        else:
            messages.info(request,"please give passwords correctly!!!")

    return render(request,'uploadnotes.html',{'form':form})

@login_required(login_url='login')
def viewnotes(request):
    fields=Note.objects.filter(user=request.user)
    return render(request,'viewnotes.html',{'fields':fields})

@login_required(login_url='login')
def delete(request,pk):
    try:
        item = Note.objects.get(id=pk)
        item.delete()
        if request.user.is_staff:
            return redirect('admindashboard')
        else:
           return redirect('viewnotes')
    except:
        item=SignUp.objects.get(id=pk)
        item.delete()
        return redirect('viewuser')

@login_required(login_url='adminlogin')    
def viewuser(request):
    fields=SignUp.objects.all()
    return render(request,'view_user.html',{'fields':fields})    

@login_required(login_url='adminlogin')
def pending(request,data):
    if data == 'All':
        fields=Note.objects.all()
    else:
        fields=Note.objects.filter(status=data)
   
    
    return render(request,'pendingnotes.html',{'fields':fields})

@login_required(login_url='adminlogin')
def status(request,pk,data):
    fm=Note.objects.get(id=pk)
    fm.status=data
    fm.save()
    return redirect('admindashboard') 

@login_required(login_url='login')
def viewallnotes(request):
    fields=Note.objects.filter(status='Accepted')
    return render(request,'viewallnotes.html',{'fields':fields})   