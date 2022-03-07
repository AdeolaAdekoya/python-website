from django.shortcuts import render


def home_page(request):

    # redirect form
    if request.method == "POST":
        print(request.POST)
        return redirect("aboutpage")
    return render(request, "home.html")

def about_page(request):
    

    return render(request, "about.html")

# Create your views here.
