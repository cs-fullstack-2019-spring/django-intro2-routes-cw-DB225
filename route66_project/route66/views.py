from django.http import HttpResponse

# Function for the default request
def index(request):
    return HttpResponse("Request?...")

# Function for the "gogetthegood" request
def thegood(request):
    return HttpResponse("Here you go! Matching Socks!)")

# Function for the "happyhappyjoyjoy" request
def happy(request):
    return HttpResponse("Ren & Stimpy FOREVER!")

# Function for the "challenge"
def string(request):
    return HttpResponse("I heard you !")