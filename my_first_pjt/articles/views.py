from django.shortcuts import render


# Create your views here.
# 함수형 으로 적어줌


def index(request):
    return render(request, "index.html")


def users(request):
    return render(request, "users.html")


def hello(request):
    name = "승귀"
    tags = ["python", "django", "html", "css"]
    books = ["책1", "책2", "책3", "책4", "vor5", "vor6", "vor7"]

    context = {"name": name,
               "tags": tags,
               "books": books,
               }
    return render(request, "hello.html", context)


def data_throw(request):
    return render(request, "data_throw.html")


def data_catch(request):
    message = request.GET.get("message")
    context = {"message": message}
    return render(request, "data_catch.html", context)


def profile(request, username):
    context = {"username":
               username}
    return render(request, "profile.html", context)
