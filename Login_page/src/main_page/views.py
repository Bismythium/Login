from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    return HttpResponse("This is the main page")
class LoginView(TemplateView):
    template_name = 'main_page/login.html'
class SignupView(TemplateView):
    template_name='main_page/signup.html'
    