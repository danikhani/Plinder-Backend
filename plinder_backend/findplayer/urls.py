from django.urls import path
from .views import(
    ProposalsApiView
)

app_name = 'findplayer'

urlpatterns = [
    path('proposals/<user_nick>/<current_latitude>/<current_longitude>/',
         ProposalsApiView.as_view(), name='djtinder_proposals'),

]