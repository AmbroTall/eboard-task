from time import timezone
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify
from django.core import validators
from ckeditor.fields import RichTextField
from django.urls import reverse

def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cant be past")

class Meeting(models.Model):
    name = models.CharField(max_length=50)
    theme = models.CharField(max_length=500)
    dateScheduled = models.DateTimeField()
    dateCreated = models.DateTimeField(auto_now_add=True, validators=[validate_date])
    slug = models.SlugField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.name} id {self.pk} '



    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.name}-{self.dateCreated}')
        super(Meeting, self).save(*args, **kwargs)


    class Meta:
        ordering = ["dateScheduled"]


class Agenda(models.Model):
    title = models.CharField(max_length=50)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='agendas')
    dateCreated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=60, blank=True)

    def __str__(self):
        return f'Agenda of {self.meeting.name} meeting id {self.pk}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}-{self.dateCreated}')
        super(Agenda, self).save(*args, **kwargs)

    class Meta:
        ordering = ["dateCreated"]

class Document(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE , related_name='documents')
    docname = models.CharField(max_length=30)
    doc = models.FileField(upload_to='documents', max_length=50)
    dateuploaded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=60, blank=True)

    def __str__(self):
        return f'Documents of {self.meeting.name} - {self.pk}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.meeting.name}-{self.docname}-{self.dateuploaded}')
        super(Document, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-dateuploaded"]


class Minutes(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE ,related_name='minutes')
    textfield = RichTextField(null=True, blank=True)
    slug = models.SlugField(max_length=60, blank=True)

    def __str__(self):
        return f'Minutes of {self.meeting.name} meeting id {self.meeting.pk}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.meeting.name}-{self.pk}')
        super(Minutes, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('meeting:agenda_list', kwargs={'slug':self.meeting.slug})

    