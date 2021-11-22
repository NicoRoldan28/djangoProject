from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt #estamos decorando este metodo para que no tenga la reestriccion del token
@csrf_exempt
def my_view(request):
    if request.method=='GET':
        return render(request,'index.html')
    elif request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...