# -*- coding: utf-8 -*-
# __author__ = "chao.fang"
from __future__ import unicode_literals, print_function, division
from django import forms
from .models import Blog


class EditorTestForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "content")