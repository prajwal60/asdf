from website.models import AboutUs,AboutTeam, Company, DomainHosting, Faq, GraphicDesign, MobileDevelopment, SoftwareDevelopment, Testimonial, VideoEditing, WebDevelopment,team,ContactUs
from django.shortcuts import render

# Create your views here.
def index(request):
    about = AboutUs.objects.all()
    faq = Faq.objects.all() 
    teams = team.objects.all()  
    testimonial = Testimonial.objects.all()
    company = Company.objects.all()
    context={
        "about":about,
        "faq":faq,
        "teams":teams,
        "testimonial":testimonial,
        "company":company
     }
    contact(request) 
     
    

    return render(request,'index.html',context)

def aboutus(request):
    company = AboutUs.objects.all()
    team = AboutTeam.objects.all()
   
    context= {
        "company":company,
        "team":team,
        
    }
    contact(request) 
   
    return render(request,'aboutus.html', context)

def services(request):  
    contact(request)   
    return render(request,'services.html')

def software(request): 

    software = SoftwareDevelopment.objects.all() 
    context = {
        "software": software
    }
    contact(request) 
    return render(request,'software.html',context)

def school(request):  
    contact(request) 
    return render(request,'school.html')

def bulkSms(request): 
    contact(request)   
    return render(request,'bulksms.html')

def webapp(request):  
    webapplication = WebDevelopment.objects.all() 
    context = {
        "webapplication": webapplication
    }
    contact(request) 
    return render(request,'webApplication.html',context)

def mobile(request):  
    mobile = MobileDevelopment.objects.all() 
    context = {
        "mobile": mobile 
    }
    contact(request) 
    return render(request,'mobile.html',context)

def domain(request): 
    domain = DomainHosting.objects.all() 
    context = {
        "domain": domain 
    }  
    contact(request)   
    return render(request,'domainWebHost.html',context)

def video(request): 
    video = VideoEditing.objects.all()
    context={
        "video" : video
    } 
    contact(request) 
    return render(request,'video.html',context)

def graphic(request):  
    design = GraphicDesign.objects.all() 
    context = {
        "design": design 
    } 
    contact(request) 
    return render(request,'graphic.html',context)

def terms(request):  
    contact(request) 
    return render(request,'terms.html')


def contact(request):
    if request.method =="POST":
        contact = ContactUs()
        contact.name=request.POST['name']
        contact.email=request.POST['email']
        contact.phone=request.POST['phone']
        contact.subject=request.POST['subject']
        contact.message=request.POST['message']
        contact.save()
