# -*- coding: utf-8 -*-
# __author__ = "chao.fang"
from __future__ import unicode_literals, print_function, division

from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.admin.widgets import AdminTextareaWidget
import copy
from .utils import editor_settings


class EditorMdWidget(forms.Textarea):
    def __init__(self, attrs=None):
        params = attrs.copy()
        self.context = copy.deepcopy(editor_settings)
        self.context["width"] = params.pop("width")
        if isinstance(self.context["width"], float):
            self.context["width"] = '"{}%"'.format(self.context["width"] * 100)
        self.context["height"] = params.pop("height")
        if isinstance(self.context["height"], float):
            self.context["height"] = '"{}%"'.format(self.context["height"] * 100)
        self.context["toolbaricons"] = params.pop("toolbaricons", '[]')
        self.context["default"] = params.pop("default")
        imagepath = params.pop("imagepath")
        if imagepath:
            editor_settings["imageUploadURL"][2] = imagepath
        self.context["imageUploadURL"] = ''.join(editor_settings["imageUploadURL"])

        super(EditorMdWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        # todo: set imageFormats from django.conf.setting
        if value is None:
            value = self.context["default"]
        self.context["markdown"] = value
        self.context["editor_id"] = "id_%s" % name.replace("-", "_")
        self.context["name"] = name
        for i, v in self.context.items():
            if isinstance(v, bool):
                self.context[i] = str(v).lower()
        return mark_safe(render_to_string('editor.md.html', self.context))

    class Media:
        # https://docs.djangoproject.com/en/1.11/topics/forms/media/
        js = (
            "js/jquery.min.js",
            "editor.md/lib/marked.min.js",
            "editor.md/lib/prettify.min.js",
            "editor.md/lib/raphael.min.js",
            "editor.md/lib/underscore.min.js",
            "editor.md/lib/sequence-diagram.min.js",
            "editor.md/lib/flowchart.min.js",
            "editor.md/lib/jquery.flowchart.min.js",
            "editor.md/editormd.min.js",
        )
        css = {"all": ("editor.md/css/editormd.min.css",)}


class AdminEditorMdWidget(AdminTextareaWidget, EditorMdWidget):
    def __init__(self, **kwargs):
        super(AdminEditorMdWidget, self).__init__(**kwargs)
