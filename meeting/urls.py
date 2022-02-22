from django.urls import path
from .views import MeetingsView, AgendasView, CreateMinutesView, UpdateMinutesView

app_name="meeting"
urlpatterns = [
    path('', MeetingsView.as_view(), name='meeting_list'),
    path('<str:slug>/', AgendasView.as_view(), name='agenda_list'),
    path('<str:slug>/minutes/', CreateMinutesView.as_view(), name='minutes_page'),
    path('<str:meeting>/<str:slug>/update/', UpdateMinutesView.as_view(), name='minutes_update'),
]
