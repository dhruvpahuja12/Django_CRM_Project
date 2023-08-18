from django.urls import path
from .views import home_page, LeadListView, lead_detail, LeadDetailView

app_name = "leads"
urlpatterns = [
    path('', LeadListView.as_view(), name="lead_list"),
    path('detail/<id>/', LeadDetailView.as_view(), name="lead_detail")

]