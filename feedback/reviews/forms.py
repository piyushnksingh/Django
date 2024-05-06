from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label="Your Name",required=True,max_length=100,error_messages={
#         "required":"Your Name must not be empty",
#     })
#     review_text=forms.CharField(label="Your Feedback",widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(label="Your rating",min_value=1,max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__" # We can also give list of fields which we want to include and We can use "exclude" to exclude certain fields.
        labels = {
            "user_name" : "Your Name",
            "review_text" : "Your Review",
            "rating" : "Your rating"
        }
        error_messages = {
            "user_name" : {
                "required" : "Your Name must not be empty.",
                "max_length" : "Please enter shorter name."
            }
        }