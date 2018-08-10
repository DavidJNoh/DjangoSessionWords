from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "words/index.html")

def process(request):
    if request.method == "POST":
        if "words" not in request.session:
            request.session["words"] = []
            print("words is now in session")
        temp = request.session["words"]
        temp.append(request.POST)
        request.session["words"]=temp
        print(request.session["words"])
    return redirect("/")
   

def clear(request):
    request.session.clear()
    return redirect ("/")