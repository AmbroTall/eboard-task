from django.urls import path
from .views import MeetingsView,UpdateMeetingView, UpdateAgendaView, UpdateDocumentView, AgendasView,CreateAgendaView,CreateDocumentView, CreateMinutesView, UpdateMinutesView, DeleteAgendaView,DeleteDocumentView,DeleteMeetingView, CreateMeetingView

app_name="meeting"
urlpatterns = [
    path('', MeetingsView.as_view(), name='meeting_list'),
    path('add-board/', CreateMeetingView.as_view(), name='meeting_create'),
    path('<str:slug>/', AgendasView.as_view(), name='agenda_list'),
    path('<str:slug>/update-board/', UpdateMeetingView.as_view(), name='meeting_update'),
    path('<str:slug>/delete-board/', DeleteMeetingView.as_view(), name='meeting_delete'),
    path('<str:slug>/minutes/', CreateMinutesView.as_view(), name='minutes_page'),
    path('<str:slug>/agenda/', CreateAgendaView.as_view(), name='agenda_create'),
    path('<str:slug>/document/', CreateDocumentView.as_view(), name='document_create'),
    path('<str:meeting>/<str:slug>/update-minutes/', UpdateMinutesView.as_view(), name='minutes_update'),
    path('<str:meeting>/<str:slug>/update-agenda/', UpdateAgendaView.as_view(), name='agenda_update'),
    path('<str:meeting>/<str:slug>/update-document/', UpdateDocumentView.as_view(), name='document_update'),
    path('<str:meeting>/<str:slug>/delete-agenda/', DeleteAgendaView.as_view(), name='agenda_delete'),
    path('<str:meeting>/<str:slug>/delete-document/', DeleteDocumentView.as_view(), name='document_delete'),
]
