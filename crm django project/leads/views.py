from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .models import Lead, Agent
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return render(request, "home.html")

# def landing_page(request):
#     return render(request, "landing.html")


class LandingPageView(TemplateView):
    template_name = "landing.html"


class LeadListView(ListView):
    template_name = "leads.html"
    queryset = Lead.objects.all()

class LeadDetailView(DetailView):
    model = Lead
    template_name = "details.html"
    # context_object_name = "lead"
    pk_url_kwarg = "id"
    
def lead_detail(request, id):
    lead = Lead.objects.filter(id= id)
    
    return render(request, "details.html", {"lead":lead})
