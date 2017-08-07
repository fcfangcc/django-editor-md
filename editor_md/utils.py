# -*- coding: utf-8 -*-
# __author__ = "chao.fang"
from django.conf import settings

editor_settings = {
    "width": 0,
    "hegiht": 0,
    "path": "/static/editor.md/lib/",
    "saveHTMLToTextarea": True,
    "imageUpload": True,
    "imageFormats": ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
    "dialogLockScreen": False,  # 设置弹出层对话框不锁屏，全局通用，默认为true
    "dialogShowMask": False,  # 设置弹出层对话框显示透明遮罩层，全局通用，默认为true
    "dialogDraggable": False,  # 设置弹出层对话框不可拖动，全局通用，默认为true
    "dialogMaskOpacity": 0.4,  # 设置透明遮罩层的透明度，全局通用，默认值为0.1
    "dialogMaskBgColor": "#000",  # 设置透明遮罩层的背景颜色，全局通用，默认为  # fff
    "imageUploadURL": ["/upload/image", "?path=", "editor_md_image/"],
    "readOnly": False,
    "codeFold": True,
    "toolbarAutoFixed": True,
    "syncScrolling": True
}
