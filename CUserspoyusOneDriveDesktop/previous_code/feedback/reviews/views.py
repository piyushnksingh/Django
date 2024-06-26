from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView

# Create your views here.
# class ReviewView(View):
#     def get(self,request):
#         form=ReviewForm()

#         return render(request,'reviews/review.html',{
#             "form":form
#         })

#     def post(self,request):
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)
#             return HttpResponseRedirect("/thank-you")

#         return render(request,'reviews/review.html',{
#             "form":form
#         })

#using FormView
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html" 
#     success_url = "/thank-you"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

#using CreateView
#CreateView
# - creates model based on model defined in model.py
# - automatically saves mnodels in DB
class ReviewView(CreateView):
    model = Review
    fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    

    
# class ThankYouView(View):
#     def get(self,request):
#         return render(request,"reviews/thank_you.html")

#using templateView         
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works"
        return context
    
# class ReviewsListView(TemplateView):
#     template_name = "reviews/review-list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
    
# class SingleReviewView(TemplateView):
#     template_name = "reviews/single-review.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context   
    
    
# using ListView
class ReviewsListView(ListView):
    template_name = "reviews/review-list.html"
    model = Review   
    context_object_name = "reviews" 
    
    #getting all post eith rating > 4
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data
    
#using DetailView
class SingleReviewView(DetailView):
    template_name = "reviews/single-review.html"
    model = Review   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favourite_id=request.session.get("favourite_review")
        context["is_favourite"] = favourite_id == str(loaded_review.id)
        return context
        
# def review(request):
#     if request.method == 'POST':
#         form=ReviewForm(request.POST)
#         if form.is_valid():
#             # review = Review(user_name=form.cleaned_data["user_name"],
#             #                 review_text=form.cleaned_data["review_text"],
#             #                 rating=form.cleaned_data["rating"]
#             #                 )
#             # review.save()

#             # if form is made using ModelForm the to save data to DB we just need to use form.save
#             form.save()
#             print(form.cleaned_data)
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form=ReviewForm()
#         return render(request,'reviews/review.html',{
#             "form":form
#         })

# def thank_you(request):
#     return render(request,"reviews/thank_you.html")

class AddFavouriteView(View):
    def post(self,request):
        review_id = request.POST["review_id"]
        # fav_review=Review.objects.get(pk=review_id)
        request.session["favourite_review"]=review_id
        return HttpResponseRedirect("/reviews/" + review_id)
        