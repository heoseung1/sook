from django.shortcuts import render


def profile(request, username):
    context = {"username":
               username}
    return render(request, "profile.html", context)
# Create your views here.
