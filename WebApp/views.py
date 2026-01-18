from django.shortcuts import render,redirect
from AdminApp.models import CategoryDB,JobDB
from WebApp.models import ContactDB,SignupDB,AppliedDB
from django.contrib import messages
# Create your views here.

def Index(request):
    Categories = CategoryDB.objects.all()

    category_filter = request.GET.get('category', '')
    location_filter = request.GET.get('location', '')
    JobType_filter =  request.GET.get('job_type', '')


    jobs = JobDB.objects.all()


    if category_filter:
        jobs = jobs.filter(Category_Name=category_filter)

    if location_filter:
        jobs = jobs.filter(Job_Location=location_filter)

    if JobType_filter:
        jobs=jobs.filter(Job_Type=JobType_filter)


    categories = JobDB.objects.values_list('Category_Name', flat=True).distinct()
    locations = JobDB.objects.values_list('Job_Location', flat=True).distinct()
    jobtype = JobDB.objects.values_list('Job_Type', flat=True).distinct()


    return render(request, "Home.html", {'Categories': Categories,

                                         'jobs': jobs,
                                         'categories': categories,
                                         'locations': locations,
                                         'jobtype': jobtype,
                                         })

def about_page(request):
    Categories=CategoryDB.objects.all()
    return render(request,"About.html",{'Categories':Categories})

def jobs_page(request):
    Categories = CategoryDB.objects.all()

    category_filter = request.GET.get('category', '')
    location_filter = request.GET.get('location', '')
    JobType_filter = request.GET.get('job_type', '')

    jobs = JobDB.objects.all()


    if category_filter:
        jobs = jobs.filter(Category_Name=category_filter)

    if location_filter:
        jobs = jobs.filter(Job_Location=location_filter)

    if JobType_filter:
        jobs = jobs.filter(Job_Type=JobType_filter)

    categories = JobDB.objects.values_list('Category_Name', flat=True).distinct()
    locations = JobDB.objects.values_list('Job_Location', flat=True).distinct()
    jobtype = JobDB.objects.values_list('Job_Type', flat=True).distinct()

    return render(request, "Jobs.html", {'Categories': Categories,

                                         'jobs': jobs,
                                         'categories': categories,
                                         'locations': locations,
                                         'jobtype': jobtype,
                                         })

def contact(request):
    Categories = CategoryDB.objects.all()
    return render(request, "Contact.html" , {'Categories': Categories,})
def save_contact_details(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        obj = ContactDB(Name=name, Email=email,Subject=sub,Message=msg)
        obj.save()
        messages.success(request, "Submited Sucessfully")
        return redirect(contact)

def Filtered_items(request, cat_name):
    print(f"Category received: {cat_name}")
    Categories = CategoryDB.objects.all()

    data = JobDB.objects.filter(Category_Name=cat_name)

    return render(request, "Filtered_items.html", {'data': data, 'Categories': Categories})

def single_item(request,item_id):
    job=JobDB.objects.get(id=item_id)
    Categories = CategoryDB.objects.all()
    return render(request,"Single_item.html",{'job':job,'Categories':Categories})

from django.core.mail import send_mail
from django.conf import settings
from .models import AppliedDB


def save_applied(request):
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        education = request.POST.get('education')
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')
        resume = request.FILES.get('resume')
        company_name = request.POST.get('company_name')
        job_role = request.POST.get('job_role')
        description = request.POST.get('description')

        obj = AppliedDB(Username=username, Name=name,
                        Email=email, Mobile=mobile, Education=education, Experience=experience,
                        Skills=skills, Resume=resume, Company_name=company_name, Job_role=job_role,
                        Description=description
                        )
        obj.save()
        messages.success(request, "Application submitted successfully ✅")
        return redirect('Index')




def applied_page(request):
    Categories = CategoryDB.objects.all()

    print("Session Data:", request.session)  # Debugging purpose

    username = request.session.get('Username')  # Use .get() to prevent KeyError

    # if not username:
    #     messages.warning(request, "You must be logged in to view applied jobs.")
    #     return redirect('sign_in')  # Redirect to login page if no username in session

    data = AppliedDB.objects.filter(Username=username)
    return render(request, "Applied.html", {'data': data, 'Categories' : Categories})

def delete_applied(request, applied_id):
    try:
        applied = AppliedDB.objects.get(id=applied_id)
        applied.delete()
        messages.success(request, "Application deleted successfully!")
    except AppliedDB.DoesNotExist:
        messages.error(request, "Application not found.")

    return redirect('applied_page')

def sign_in(request):
    return render(request,"Sign_In.html")
def sign_up(request):
    return render(request,"Sign_Up.html")
def save_signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        email=request.POST.get('email')
        obj=SignupDB(Username=username,Password=pass1,Confirm_Password=pass2,Email=email)
        obj.save()
        messages.success(request,"Registered Sucessfully")
        return redirect(sign_in)
def user_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pswd=request.POST.get('pass1')
        if SignupDB.objects.filter(Username=un,Password=pswd ).exists():
            request.session['Username']=un
            request.session['Password']=pswd
            messages.success(request, "")
            return redirect(Index)
        else:
            messages.warning(request, "Failed to login")
            return redirect(sign_in)
    else:
        messages.warning(request, "")
        return redirect(sign_in)
def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(sign_in)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from AdminApp.models import JobDB, CategoryDB
from django.urls import reverse

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower()
        reply = ""


        if "how many jobs" in user_message or "jobs available" in user_message:
            total_jobs = JobDB.objects.count()
            reply = f"💼 There are currently {total_jobs} jobs available on our site."

        elif "categories" in user_message:
            categories = CategoryDB.objects.values_list('Name', flat=True)
            reply = "📂 Available categories: " + ", ".join(categories)

        elif "show" in user_message and "job" in user_message:
            categories = CategoryDB.objects.values_list('Name', flat=True)
            found = False
            for cat in categories:
                if cat.lower() in user_message:
                    jobs = JobDB.objects.filter(Category_Name=cat)
                    if jobs.exists():
                        reply = f"💼 Jobs in {cat}:<br>"
                        for j in jobs[:5]:  # top 5 jobs
                            # Generate URL using reverse
                            job_url = reverse('single_item', kwargs={'item_id': j.id})
                            reply += f"- <a href='{job_url}' target='_blank'>{j.Job_Role} at {j.Company_Name}</a><br>"
                    else:
                        reply = f"❌ No jobs found in {cat}."
                    found = True
                    break
            if not found:
                reply = "🤖 Sorry, I couldn't find jobs for that category."

        elif any(word in user_message for word in ["hello", "hi"]):
            reply = "👋 Hello! Welcome to our Job Portal. How can I assist you today?"
        elif any(word in user_message for word in ["apply", "application"]):
            reply = "📝 You can apply for jobs directly on the site. Click 'Apply Now' in the job listing."
        elif any(word in user_message for word in ["resume", "cv"]):
            reply = "📄 Upload your resume in your profile to apply faster."
        elif any(word in user_message for word in ["search", "find"]):
            reply = "🔍 Use the search bar to filter jobs by keywords, location, and type."
        elif "interview" in user_message:
            reply = "📅 Check our Resources section for interview tips and guides."
        elif any(word in user_message for word in ["contact", "support"]):
            reply = "📩 Reach support via Contact page or email support@jobportal.com."
        elif any(word in user_message for word in ["salary", "pay", "wages"]):
            reply = "💰 Salary info is shown on the job description page."
        elif any(word in user_message for word in ["thank you", "thanks"]):
            reply = "😊 You're welcome! Ask me anything about jobs."
        else:
            reply = "🤖 I can answer questions about jobs, categories, applications, and profiles. Ask me anything!"

        return JsonResponse({"reply": reply})

    return JsonResponse({"error": "Invalid request method."}, status=405)
