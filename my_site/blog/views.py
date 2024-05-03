from django.shortcuts import render
from datetime import date

all_posts=[
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Piyush",
        "date": date(2021,7,21),
        "title": "Mountain-hiking",
        "excerpt": "There's nothing like this view.",
        "content": """"
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
           Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
           nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
           reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
           pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
           culpa qui officia deserunt mollit anim id est laborum.
        """
    },
    {
        "slug": "PROGRAMMING-IS-FUN",
        "image": "CODING.jpg",
        "author": "Piyush",
        "date": date(2022,3,18),
        "title": "PROGRAMMING IS GREAT",
        "excerpt": "Did you ever spend hours searching that one error in your code?",
        "content": """"
           Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
           Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
           nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
           reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
           pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
           culpa qui officia deserunt mollit anim id est laborum.

           Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
           Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
           nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
           reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
           pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
           culpa qui officia deserunt mollit anim id est laborum.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Piyush",
        "date": date(2020,8,5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing!",
        "content": """"
           Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
           Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
           nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
           reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
           pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
           culpa qui officia deserunt mollit anim id est laborum.

           Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
           Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
           nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
           reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
           pariatur. Excepteur sint occaecat cupidatat non proident, sunt in 
           culpa qui officia deserunt mollit anim id est laborum.
        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts":latest_posts,
    })

def posts(request):
    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts,
    })

def post_detail(request,slug):
    identified_post=next(post for post in all_posts if post['slug'] == slug) #oneliner for finding post['slug']==slug.
    return render(request,"blog/post-detail.html",{
        "post":identified_post
    })
