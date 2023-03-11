from django.contrib import admin
from .models import Blog, Project, Message, BlogTag, ProjectTag, ProjectImage


admin.site.register(Blog)
admin.site.register(Project)
admin.site.register(Message)
admin.site.register(BlogTag)
admin.site.register(ProjectTag)
admin.site.register(ProjectImage)
