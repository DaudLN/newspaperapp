from django.urls import reverse_lazy
from django.views.generic import CreateView
from crispy_forms.layout import Row, Fieldset
from .forms import CustomUserCreationForm
from .forms_style import *
# Create your views here.

Fieldset.template = 'signup.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    template = 'signup.html'
