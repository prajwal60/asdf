from django.db import models

# Create your models here.

class AboutUs(models.Model):
    welcome = models.CharField(max_length=100)
    description1 = models.CharField(max_length=500, null=True)
    description2 = models.CharField(max_length=1000, null=True)
    feature1 = models.CharField(max_length=300, null=True, blank=True, default=' ')
    feature2 = models.CharField(max_length=300, null=True, blank=True, default=' ')
    feature3 = models.CharField(max_length=300, null=True, blank=True, default=' ')
    feature4 = models.CharField(max_length=300, null=True, blank=True, default=' ')

    def __str__(self):
        return self.welcome
    
class AboutTeam(models.Model):
    welcome = models.CharField(max_length=100)
    description1 = models.CharField(max_length=500)
    description2 = models.CharField(max_length=1000)
    feature1 = models.CharField(max_length=300, null=True, blank=True, default=' ')
    feature2 = models.CharField(max_length=300, null=True, blank=True, default=' ')
    feature3 = models.CharField(max_length=300, null=True, blank=True, default=' ')
    feature4 = models.CharField(max_length=300, null=True, blank=True, default=' ')

    def __str__(self):
        return self.welcome

class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question    

class team(models.Model):
    full_name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='static/img/team/')
    post = models.CharField(max_length=200,blank=True, null=True, default='#')
    facebook = models.CharField(max_length=1000,blank=True, null=True, default='#')
    twitter = models.CharField(max_length=1000,blank=True, null=True, default='#')
    instagram = models.CharField(max_length=1000,blank=True, null=True, default='#')
    linkedin = models.CharField(max_length=1000,blank=True, null=True, default='#')

    def __str__(self):
        return self.full_name

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/img/testimonial/')
    post = models.CharField(max_length=100)
    quote = models.TextField()

    def __str__(self):
        return self.name

class Company(models.Model):
    description1 = models.CharField(max_length=500)
    description2 = models.TextField()
    topic1 = models.CharField(max_length=150)
    answer1 = models.TextField()
    topic2 = models.CharField(max_length=150)
    answer2 = models.TextField()
    topic3 = models.CharField(max_length=150)
    answer3 = models.TextField()
    def __str__(self):
        return self.topic1

class DigitalMarketing(models.Model):
    topic = models.CharField(max_length=100,default="Digital Marketing")
    description1 = models.CharField(max_length=200)
    description2 = models.TextField()

    def __str__(self):
        return self.topic


    
    
    
    