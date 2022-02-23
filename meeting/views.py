from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Meeting,Minutes,Document,Agenda
from .filters import MeetingFilter
from.forms import Minuteform, Meetingform, AgendaForm, DocumentForm

# View for meeting lists
class MeetingsView(ListView):
    model = Meeting
    template_name = 'meeting/meeting_list.html'

    def get_queryset(self):
        qs=self.model.objects.all()
        meetings = MeetingFilter(self.request.GET, queryset=qs)
        return meetings.qs

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['meetings']=MeetingFilter(self.request.GET, queryset=self.get_queryset())
        return context

# view for displaying agendas and documents
class AgendasView(DetailView):
    model = Meeting
    context_object_name = 'meetings'
    template_name = 'meeting/agenda_docs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agenda_count'] = Agenda.objects.filter(meeting=context['meetings']).count()
        context['doc_count'] = Document.objects.filter(meeting=context['meetings']).count()
        context['mint'] = Minutes.objects.filter(meeting=context['meetings'])
        return context


# View for Creating Agendas in a meeting in the UI
class CreateAgendaView(CreateView):
    form_class = AgendaForm
    model = Meeting
    template_name = 'meeting/agenda_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('meeting:agenda_list', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.meeting = self.object
        fm.save()
        return super(CreateAgendaView, self).form_valid(form)

# View for Creating Documents in a meeting in the UI
class CreateDocumentView(CreateView):
    form_class = DocumentForm
    model = Meeting
    template_name = 'meeting/document_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('meeting:agenda_list', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.meeting = self.object
        fm.save()
        return super(CreateDocumentView, self).form_valid(form)


#view for updating agenda
class UpdateAgendaView(UpdateView):
    model = Agenda
    template_name = 'meeting/edit_agenda.html'
    fields = ['title',]


class UpdateDocumentView(UpdateView):
    model = Document
    template_name = 'meeting/edit_document.html'
    fields = ['docname','doc',]

# view for deleting agendas in the ui
class DeleteAgendaView(DeleteView):
    model = Agenda
    template_name = 'meeting/agenda_delete.html'
    success_url = reverse_lazy('meeting:agenda_list')

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('meeting:agenda_list', kwargs={'slug': self.object.meeting.slug})

# view for deleting in the ui
class DeleteDocumentView(DeleteView):
    model = Document
    template_name = 'meeting/document_delete.html'
    success_url = reverse_lazy('meeting:agenda_list')

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('meeting:agenda_list', kwargs={'slug': self.object.meeting.slug})


# view for creating minutes
class CreateMinutesView(CreateView):
    form_class = Minuteform
    model = Meeting
    template_name = 'meeting/minutes_view.html'

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('meeting:agenda_list',kwargs={'slug':self.object.slug})


    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.meeting = self.object
        fm.save()
        return super(CreateMinutesView, self).form_valid(form)

# view for updating minutes
class UpdateMinutesView(UpdateView):
    model = Minutes
    template_name = 'meeting/edit_minutes.html'
    fields = ['textfield',]
    # success_url = reverse_lazy('meeting:agenda_list')


# View for Creating meetings in the UI
class CreateMeetingView(CreateView):
    form_class = Meetingform
    model = Meeting
    template_name = 'meeting/meeting_create.html'
    success_url = reverse_lazy('meeting:meeting_list')

# View for Creating meetings in the UI
class UpdateMeetingView(UpdateView):
    fields = ['name','theme', 'dateScheduled']
    model = Meeting
    template_name = 'meeting/meeting_update.html'
    success_url = reverse_lazy('meeting:meeting_list')


# View for deleting meetings in the UI
class DeleteMeetingView(DeleteView):
    model = Meeting
    template_name = 'meeting/meeting_delete.html'
    success_url = reverse_lazy('meeting:meeting_list')
