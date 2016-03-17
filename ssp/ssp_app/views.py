from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    # import pdb; pdb.set_trace();
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user.password = password
            if user.username == 'admin':
                return render(request, 'admin.html', {'user': user.username})
            else:
                return render(request, 'other_users.html', {'user': user.username})
        except:
            print "Invalid login details: {0}, {1}".format(username, password)
            return render_to_response("error.html",)

    else:
        return render(request, 'home.html')

def home_page(request):
    return render(request, 'admin.html',)


def create_user(request):
    return render(request, 'create_user.html')

def register(request):
    import pdb; pdb.set_trace();
    if request.method == 'POST':
        user = User()
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.save()
        return render_to_response('success.html',)
    else:
        return render(request, 'create_user.html')

def update_user(request):
    pass

def delete_user(request):
    pass

def list_users(request):
    pass

def logout(request):
    return HttpResponseRedirect("/")