from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from tagging.fields import TagField
from wiki.models import Article


class Version(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

ENUM_TYPE_CHOICES = (('link','Link'),
                     ('attr','Enum Attribute'),
                     )
class TypeEnum(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=ENUM_TYPE_CHOICES)
    
    def __unicode__(self):
        return self.name
    
    class meta:
        unique_together = ('name', 'type')

NODE_TYPE_CHOICES = (('project','Project'),
                     ('folder','Folder'),
                     ('module','Module'),
                     ('module-title','Title'),
                     )
class Node(models.Model):
    version = models.ForeignKey(Version, null=True, blank=True)
    title = models.CharField(max_length=200)
    index = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=20, choices=NODE_TYPE_CHOICES)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    
    tags = TagField()
    
    def __unicode__(self):
        return self.title

class ColumnHeader(models.Model):
    title = models.CharField(max_length=100)
    node = models.ForeignKey(Node, limit_choices_to={'type':'module'})
    
    content_type = models.ForeignKey(ContentType, limit_choices_to={'name__endswith':'attr'})
    
    def __unicode__(self):
        return self.title

class View(models.Model):
    title = models.CharField(max_length=100)
    node = models.ForeignKey(Node, limit_choices_to = {'type':'module'})
    
    headers = models.ManyToManyField(ColumnHeader)
    def __unicode__(self):
        return self.title
   
class Item(models.Model):
    version = models.ForeignKey(Version, null=True, blank=True)
    node = models.ForeignKey(Node, limit_choices_to = {'type_startswith':'module'})
    index = models.IntegerField(null=True, blank=True)
    
    tags = TagField()

class Link(models.Model):
    version = models.ForeignKey(Version, null=True, blank=True)
    type = models.ForeignKey(TypeEnum, limit_choices_to = {'type':'link'})
    source = models.ForeignKey(Item, related_name='source_links')
    target = models.ForeignKey(Item, related_name='target_links')
    
    tags = TagField()

class Document(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    node = models.ForeignKey(Node)
    file = models.FileField(upload_to='ooo_files')
    
    def download_file(self):
        return '<a href=%s>%s</a>' % (self.file.url, self.file)
    download_file.allow_tags=True
    
    def __unicode__(self):
        return self.file.name

class Attribute(models.Model):
    version = models.ForeignKey(Version, null=True, blank=True)
    item = models.ForeignKey(Item)
    column = models.ForeignKey(ColumnHeader)
    class Meta:
        abstract = True


class KeyAttr(Attribute):
    slug = models.SlugField()
    def __unicode__(self):
        return self.slug

class ShortTextAttr(Attribute):
    text = models.CharField(max_length=100)
    def __unicode__(self):
        return self.text

class IntAttr(Attribute):
    value = models.IntegerField()
    def __unicode__(self):
        return self.value

class EnumAttr(Attribute):
    value = models.ForeignKey(TypeEnum, limit_choices_to = {'type':'attr'})
    
    def __unicode__(self):
        return self.slug
    
    tags = TagField()
    
    def __unicode__(self):
        return self.value.name

class ArticleAttr(Attribute):
    article = models.ForeignKey(Article)
    
    def __unicode__(self):
        return self.article.title
