from django.http import HttpResponse,JsonResponse 

def home_page(request):
    print("Home page requested")
    friends=['ankit','ravi','pradip']
    
    return HttpResponse("<h1>This is home page</h1>")