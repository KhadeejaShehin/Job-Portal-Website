from django.shortcuts import render,redirect
from AdminApp.models import CategoryDB,CompanyDB,JobDB
from WebApp.models import ContactDB,AppliedDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
def index_page(request):
    return render(request,"index.html")

def category_page(request):
    return render(request,"AddCategory.html")

def save_category(request):
    if request.method=="POST":
        name=request.POST.get('name')
        des=request.POST.get('description')
        loc=request.POST.get('location')
        img=request.FILES ['image']
        obj=CategoryDB(Name=name,Description=des,Image=img,Location=loc)
        obj.save()
        return redirect(category_page)


def display_category(request):
    data = CategoryDB.objects.all()
    return render(request, "DisplayCategory.html", {'data': data})

def edit_category(request,c_id):
    data = CategoryDB.objects.get(id=c_id)
    return render(request,"EditCategory.html",{'data':data})

def delete_category(request,c_id):
    category=CategoryDB.objects.filter(id=c_id)
    category.delete()
    return redirect(display_category)

def update_category(request,c_id):
    if request.method=="POST":
        name=request.POST.get('name')
        des=request.POST.get('description')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=CategoryDB.objects.get(id=c_id).Image
        CategoryDB.objects.filter(id=c_id).update(Name=name,Description=des,Image=file)
        return redirect(display_category)

def company_page(request):
    cat = CategoryDB.objects.all()
    return render(request, "AddCompany.html", {'categories': cat})

def save_company(request):
    if request.method=="POST":
        cname=request.POST.get('category_name')
        compname=request.POST.get('company_name')
        des=request.POST.get('description')
        obj=CompanyDB(Category_Name=cname, Company_Name=compname,Description=des)
        obj.save()
        return redirect(company_page)

def display_company(request):
    comp = CompanyDB.objects.all()
    return render(request, "DisplayCompany.html", {'comp': comp})

def edit_company(request,comp_id):
    cat=CategoryDB.objects.all()
    comp=CompanyDB.objects.get(id=comp_id)
    return render(request,"EditCompany.html",{'comp':comp,'cat':cat})

def update_company(request,comp_id):
    if request.method=="POST":
        cname = request.POST.get('category_name')
        compname = request.POST.get('company_name')
        des = request.POST.get('description')
        CompanyDB.objects.filter(id=comp_id).update(
            Category_Name=cname,Company_Name=compname,Description=des)
        messages.success(request, "Company updated Successfulyy...!")
        return redirect(display_company)

def delete_company(request,comp_id):
        company = CompanyDB.objects.filter(id=comp_id)
        messages.error(request, "Company Deleted Successfulyy...!")
        company.delete()

        return redirect(display_company)

def job_page(request):
    cat = CategoryDB.objects.all()
    comp=CompanyDB.objects.all()
    return render(request,"AddJob.html" ,{'categories':cat,'company':comp} )

def save_job(request):
    if request.method=="POST":
        cname=request.POST.get('category_name')
        compname=request.POST.get('company_name')
        job_loc=request.POST.get('job_location')
        role=request.POST.get('job_role')
        des=request.POST.get('description')
        type=request.POST.get('job_type')
        date=request.POST.get('job_date')
        img= request.FILES['logo']
        obj=JobDB(Category_Name=cname, Company_Name=compname,Job_Location=job_loc,Job_Role=role,Description=des,Job_Type=type,Logo=img,
                  Job_Date=date)
        obj.save()
        return redirect(job_page)

def display_job(request):
        job = JobDB.objects.all()
        return render(request, "DisplayJob.html", {'job': job})


def edit_job(request,job_id):
    cat = CategoryDB.objects.all()
    comp = CompanyDB.objects.all()
    job=JobDB.objects.get(id=job_id)
    return render(request,"EditJob.html",{'cat':cat,'company':comp,'job':job})

def update_job(request,job_id):
    if request.method=="POST":
        cname = request.POST.get('category_name')
        compname = request.POST.get('company_name')
        job_loc = request.POST.get('job_location')
        role = request.POST.get('job_role')
        des = request.POST.get('description')
        type = request.POST.get('job_type')
        date = request.POST.get('job_date')
        try:
            img = request.FILES['logo']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=JobDB.objects.get(id=job_id).Logo
        JobDB.objects.filter(id=job_id).update(
            Category_Name=cname, Company_Name=compname,Job_Location=job_loc,Job_Role=role,Description=des,Job_Type=type,Logo=file,
        Job_Date=date)
        return redirect(display_job)
def delete_job(request,job_id):
    job=JobDB.objects.filter(id=job_id)
    job.delete()
    return redirect(display_job)


def adminLogins(request):
    return render(request,"AdminLoginPage.html")

def AdminLoginPage(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pswd)
            if user is not None:
                request.session['username'] = un
                request.session['password'] = pswd

                login(request, user)
                return redirect(index_page)
            else:
                return redirect(adminLogins)
        else:
            return redirect(adminLogins)


def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminLogins)

def contact_data(request):
    data=ContactDB.objects.all()
    return render(request,"ContactData.html",{'data':data})
def delete_contact_data(request,cnt_id):
    contact=ContactDB.objects.filter(id=cnt_id)
    contact.delete()
    return redirect(contact_data)

def display_applied(request):
    Categories = CategoryDB.objects.all()

    print("Session Data:", request.session)

    username = request.session.get('Username')

    if not username:
        messages.warning(request, "You must be logged in to view applied jobs.")
        return redirect('Sign_In')

    applied = AppliedDB.objects.all()
    return render(request, "DisplayApplied.html", {'applied': applied , 'Categories' : Categories})