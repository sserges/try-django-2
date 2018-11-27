from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
	return render(request, 'home.html', {})


def contact_view(request):
	return render(request, 'contact.html', {})


def about_view(request):
	my_context = {
		"my_text": "This is about us",
		'my_number': 123,
		'my_list': [123, 789, 69, 56]
	}
	return render(request, 'about.html', my_context)

