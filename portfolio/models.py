from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class BlogTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProjectTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="images/")
    author = models.CharField(max_length=200, null=True, default="Ukasoanya Favour C.")
    body = RichTextUploadingField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    active = models.BooleanField(default=False)
    tags = models.ManyToManyField(BlogTag)
    # slug=

    def __str__(self):
        return self.headline


class Project(models.Model):
    CATEGORY = (
        ("Computer Vision", "Computer Vision"),
        ("NLP", "NLP"),
        ("Analysis", "Analysis"),
        ("Others", "Others"),
    )

    STATUS = (
        ("Ongoing", "Ongoing"),
        ("Complete", "Complete"),
        ("In Production", "In Production")
    )

    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(max_length=200, null=True, upload_to="images/")
    description = models.CharField(max_length=1000)
    client = models.CharField(max_length=200, null=True, default="Personal")
    link = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    tags = models.ManyToManyField(ProjectTag)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to="images/")

    def __str__(self):
        return self.project.title


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.CharField(max_length=200)
    date_sent = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
