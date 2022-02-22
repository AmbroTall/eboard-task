from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Meeting,Minutes,Document,Agenda
from .filters import MeetingFilter
from.forms import Minuteform

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


# class DeleteMeetingView(DeleteView):
#     model = Meeting
#     template_name = 'meeting/delete_meeting.html'
#     success_url = reverse_lazy('')
