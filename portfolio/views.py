from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

from .decorators import authenticated_user
from .models import Blog, Project, ProjectImage
from .forms import ContactForm, ProjectForm, BlogForm


def home(request):
    blogs_preview = Blog.objects.filter(active=True).order_by("-id")[:3]
    projects = Project.objects.all()
    context = {'blogs': blogs_preview, 'projects': projects}
    return render(request, 'portfolio/main.html', context)


def blog(request):
    blogs = Blog.objects.filter(active=True).order_by("-id")
    context = {'blogs': blogs}
    return render(request, 'portfolio/blog_grid.html', context=context)


def blog_single(request, id):
    blog = Blog.objects.get(id=id)
    context = {'blog': blog}
    return render(request, 'portfolio/blog_single.html', context=context)


def project_single(request, id):
    project = Project.objects.get(id=id)
    slide_show = project.projectimage_set.all()
    context = {'project': project, 'slide_show':slide_show}
    return render(request, 'portfolio/project_single.html', context=context)


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        slide_show = request.FILES.getlist('images')
        if form.is_valid():
            project = form.save()
            for image in slide_show:
                ProjectImage.objects.create(project=project, image=image)
            return redirect('control')

    context = {'form': form}
    return render(request, 'portfolio/create_project.html', context=context)


def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)
    current_slides = project.projectimage_set.all()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        slide_show = request.FILES.getlist('images')
        if form.is_valid():
            form.save()
            for image in slide_show:
                ProjectImage.objects.create(project=project, image=image)
            return redirect('control')

    context = {'form': form, "current_slides": current_slides}
    return render(request, 'portfolio/create_project.html', context=context)


def remove_image(request, id):
    project_image = ProjectImage.objects.get(id=id)
    os.remove(project_image.image.path)
    project_image.delete()

    # Get the referring page URL
    referring_url = request.META.get('HTTP_REFERER', '/')

    return redirect(referring_url)


def delete_project(request, id):
    project = Project.objects.get(id=id)
    if request.method == 'POST':
        for image_slide in project.projectimage_set.all():
            os.remove(image_slide.image.path)

        project.delete()
        os.remove(project.thumbnail.path)
        return redirect('control')

    detail = f"Are you sure you want to delete {project}"
    context = {'prompt': detail, 'project': project}
    return render(request, 'portfolio/delete_project.html', context=context)


# @receiver(post_delete, sender=ProjectImage)
# def delete_image_file(sender, instance, **kwargs):
#     if instance.image and os.path.isfile(instance.image.path):
#         os.remove(instance.image.path)


def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('control')

    context = {'form': form}
    return render(request, 'portfolio/create_blog.html', context=context)


def update_blog(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        # blog = Blog(content=request.POST['desc'])
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('control')

    context = {'form': form, 'blog':blog}
    return render(request, 'portfolio/create_blog.html', context=context)


def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('control')

    detail = f"Are you sure you want to delete {blog}"
    context = {'prompt': detail, 'blog': blog}
    return render(request, 'portfolio/delete_blog.html', context=context)


def sendMail(request):
    # form = ContactForm(request.POST)
    # if form.is_valid():
    #     form.save()

    template = render_to_string('portfolio/email_template.html', {
                                'name': request.POST['name'],
                                'message': request.POST['message'],
                                'email': request.POST['email']
                                })

    email = EmailMessage(request.POST['subject'],
                         template,
                         settings.EMAIL_HOST_USER,
                         ['ukasoanyaf@gmail.com'])

    email.fail_silently = False
    email.send()

    messages.success(request, "Thank you for reaching out, I'll respond as soon as possible")
    return redirect('/#contact')


def control_panel(request):
    projects = Project.objects.all()
    blogs = Blog.objects.all()
    context = {'projects': projects, 'blogs': blogs}

    return render(request, 'portfolio/control.html', context=context)


@authenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "You are not an authorised personnel")

    content = {}
    return render(request, 'portfolio/login.html', context=content)


def logout_user(request):
    logout(request)
    return redirect('home')

