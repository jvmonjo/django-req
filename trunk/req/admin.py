from django.contrib import admin
from models import *

class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date', 'user')
admin.site.register(Version, VersionAdmin)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('date', 'node', 'download_file',)
    list_filters = ('node',)
admin.site.register(Document, DocumentAdmin)

class TypeEnumAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
admin.site.register(TypeEnum, TypeEnumAdmin)

class NodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'index', 'type', 'parent', 'version')
    list_filter = ('type',)
    order_by = ('index',)
    save_as = True
admin.site.register(Node, NodeAdmin)

class ColumnHeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'node', 'content_type')
    list_filter = ('content_type',)
    save_as = True
admin.site.register(ColumnHeader, ColumnHeaderAdmin)

class FilterInline(admin.TabularInline):
    model = Filter

class ViewAdmin(admin.ModelAdmin):
    list_display = ('title', 'node',)
    inlines = [FilterInline,]
    save_as = True
admin.site.register(View, ViewAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('node', 'index', 'version')
    order_by = ('index',)
admin.site.register(Item, ItemAdmin)

class LinkAdmin(admin.ModelAdmin):
    list_display = ('type', 'source', 'version')
    list_filter = ('type',)
admin.site.register(Link, LinkAdmin)

class KeyAttrAdmin(admin.ModelAdmin):
    list_display = ('column', 'item', 'text', 'version')
admin.site.register(KeyAttr, KeyAttrAdmin)

class ShortTextAttrAdmin(admin.ModelAdmin):
    list_display = ('column', 'item', 'text', 'version')
admin.site.register(ShortTextAttr, ShortTextAttrAdmin)

class IntAttrAdmin(admin.ModelAdmin):
    list_display = ('column', 'item', 'value', 'version')
admin.site.register(IntAttr, IntAttrAdmin)

class EnumAttrAdmin(admin.ModelAdmin):
    list_display = ('column', 'item', 'value', 'version')
admin.site.register(EnumAttr, EnumAttrAdmin)

class ArticleAttrAdmin(admin.ModelAdmin):
    list_display = ('column', 'item', 'article', 'version')
admin.site.register(ArticleAttr, ArticleAttrAdmin)

