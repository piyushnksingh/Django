from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .forms import ProfileForm
from . models import UserProfile
# import os

# Create your views here.
class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles/"
    
class ProfileView(ListView):
    model = UserProfile
    template_name = "profiles/user-profiles.html"
    context_object_name = "profiles"
    


# def store_file(file):
#     directory = "temp"
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#     with open(os.path.join(directory, "image.png"), "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)


# class CreateProfileView(View):
#     def get(self,request):
#         form = ProfileForm()
#         return render(request,"profiles/create_profile.html",{
#             "form":form
#         })
    
#     def post(self,request):
#         submitted_form = ProfileForm(request.POST,request.FILES)
#         if submitted_form.is_valid(): 
#             # store_file(request.FILES["image"])
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         return render(request,"profiles/create_profile.html",{
#             "form":submitted_form
#         })
            
    