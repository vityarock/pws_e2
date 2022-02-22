from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Message
from .forms import EmailForm
from django.urls import reverse_lazy

# Create your views here.
class EmailView(ListView):
    model = Message
    paginate_by = 10
    template_name = 'mail_list.html'



class EmailCreate(CreateView):
    model = Message
    form_class = EmailForm
    template_name = 'mail_form.html'
    success_url = reverse_lazy('mail_form')    
