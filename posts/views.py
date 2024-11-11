from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {"title": "Deserunt est et qui occaecat nisi non ullamco officia.",
   "content": "Ut eiusmod laborum culpa proident minim culpa amet esse ut culpa tempor veniam. Consequat quis occaecat voluptate laboris adipisicing nulla consequat sint ipsum. In officia amet consectetur ipsum do irure laborum labore do sint cillum amet."},
  {"title": "Ullamco est duis consequat mollit voluptate aliqua.",
   "content": "Est irure sint non duis fugiat cupidatat aute enim. Dolor tempor laboris ad mollit nulla exercitation cillum elit. Commodo ea aliquip Lorem dolore dolore minim. Ullamco culpa duis ad reprehenderit labore."},
  {"title": "Nisi pariatur nostrud amet fugiat ea.",
   "content": "Proident ad nisi ipsum reprehenderit ullamco excepteur cupidatat esse ex in. Cillum velit voluptate do laboris commodo ullamco minim ipsum aliquip nostrud commodo tempor laborum. Tempor do voluptate et nostrud sint non nisi. Elit nulla ipsum sint ea culpa duis. Ipsum irure sunt laboris est id enim est ea commodo id. Cillum esse voluptate ipsum culpa exercitation nostrud."}
]

# Create your views here.
def home(request):
  html = ""
  for post in posts:
    html += f"""
      <h2>{post["title"]}</h2>
      <p>{post["content"]}</p> 
    """
  return HttpResponse(html)