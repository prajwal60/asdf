from website.models import AboutUs,AboutTeam, Company, Faq, SoftwareDevelopment, Testimonial, VideoEditing,team,ContactUs
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

    contact = ContactUs.objects.all()
    print(request.POST)

    return render(request,'index.html',context)

def aboutus(request):
    company = AboutUs.objects.all()
    team = AboutTeam.objects.all()
   
    context= {
        "company":company,
        "team":team,
        
    }
    return render(request,'aboutus.html', context)

def services(request):   
    return render(request,'services.html')

def software(request): 

    software = SoftwareDevelopment.objects.all() 
    context = {
        "software": software
    }

    return render(request,'software.html',context)

def school(request):   
    return render(request,'school.html')

def bulkSms(request):   
    return render(request,'bulksms.html')

def webapp(request):   
    return render(request,'webApplication.html')

def mobile(request):   
    return render(request,'mobile.html')

def domain(request):   
    return render(request,'domainWebHost.html')

def video(request): 
    video = VideoEditing.objects.all()
    context={
        "video" : video
    }  
    return render(request,'video.html',context)

def graphic(request):   
    return render(request,'graphic.html')

def terms(request):   
    return render(request,'terms.html')
