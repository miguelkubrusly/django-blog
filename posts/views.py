from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


POSTS = [
  {"id":0,
    "title": "Deserunt est et qui occaecat nisi non ullamco officia.",
  "content": "Ut eiusmod laborum culpa proident minim culpa amet esse ut culpa tempor veniam. Consequat quis occaecat voluptate laboris adipisicing nulla consequat sint ipsum. In officia amet consectetur ipsum do irure laborum labore do sint cillum amet."},
  {"id":1,
    "title": "Ullamco est duis consequat mollit voluptate aliqua.",
  "content": "Est irure sint non duis fugiat cupidatat aute enim. Dolor tempor laboris ad mollit nulla exercitation cillum elit. Commodo ea aliquip Lorem dolore dolore minim. Ullamco culpa duis ad reprehenderit labore."},
  {"id":2,
    "title": "Nisi pariatur nostrud amet fugiat ea.",
  "content": "Proident ad nisi ipsum reprehenderit ullamco excepteur cupidatat esse ex in. Cillum velit voluptate do laboris commodo ullamco minim ipsum aliquip nostrud commodo tempor laborum. Tempor do voluptate et nostrud sint non nisi. Elit nulla ipsum sint ea culpa duis. Ipsum irure sunt laboris est id enim est ea commodo id. Cillum esse voluptate ipsum culpa exercitation nostrud."}
]

# POSTS = []

# Create your views here.
def home(request):
  return render(request, "posts/home.html", {"name":"Miguel","posts":POSTS})

def post_detail (request, id):
  current_post = next((p for p in POSTS if p["id"]==id), None) 
  if current_post:
    html = f"""
    <h1>{current_post["title"]}</h1>
    <p>{current_post["content"]}</p>
    """
    return HttpResponse(html)
  else: 
    return HttpResponseNotFound("Post not available 🥲")

def redirect_id(request, id):
  url = reverse("posts", args=[id])
  print(url)
  return HttpResponseRedirect(url)