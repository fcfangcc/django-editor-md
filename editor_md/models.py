from django.db import models
from django.contrib.admin import widgets as admin_widgets
from .widgets import EditorMdWidget, AdminEditorMdWidget


# Create your models here.
class EditorMdField(models.TextField):
    def __init__(self, width=0.85,
                 height=600,
                 imagepath="editor_md_image/",
                 toolbaricons=list(),
                 default="### Hello Editor.md !",
                 **kwargs):
        """
        :param width : float or int
            width for editor.md window.
            if float:
                height = "height*100%"
            if int:
                height = height
        :param height : float or int
            height for editor.md window.
            if float:
                height = "height*100%"
            if int:
                height = height
        :param imagepath: str
            image save path.
        :param toolbaricons: list ot tuple
            editor.md  button list.
            https://pandao.github.io/editor.md/examples/custom-toolbar.html
        :param default: str
            default text in editor.
        :param kwargs:
            TextField params.
        """
        self.settings = locals().copy()
        del self.settings["self"], self.settings["kwargs"]
        super(EditorMdField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': EditorMdWidget(attrs=self.settings)}
        defaults.update(kwargs)
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = AdminEditorMdWidget(
                attrs=self.settings)
        return super(EditorMdField, self).formfield(**defaults)
