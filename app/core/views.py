from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from inventory.models import Sneaker, Location, Collection




# Create your views here.

def index(request):
	sneaker_count = Sneaker.objects.count()
	location = Location.objects.count()
	collection = Collection.objects.count()
	sneaker = Sneaker.objects.all()
	content = {
		'sneaker_count': sneaker_count,
		'location': location,
		'collection': collection,
		'sneaker': sneaker
	}
	return render(request, 'core/home.html', content)


#login
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('core:index')
		else:
			messages.info(request, 'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})

