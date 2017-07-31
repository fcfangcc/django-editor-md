# -*- coding: utf-8 -*-
# __author__ = "chao.fang"
from __future__ import unicode_literals, print_function, division
from django.db import models

from editor_md.models import EditorMdField


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题", blank=True)
    content = EditorMdField(verbose_name="文章内容", blank=True)
