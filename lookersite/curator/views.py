# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = ExampleModel.objects.get(pk=course_id)
            m.model_pic = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')
