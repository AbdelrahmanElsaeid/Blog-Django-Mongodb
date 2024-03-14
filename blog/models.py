from django.db import models
from accounts.models import User
from django.utils.translation import gettext as _

# Create your models here.


##################____________ Using ORM ______________################




class Post(models.Model):
    title = models.CharField(max_length=255,verbose_name=_('Title'))
    content = models.TextField(max_length=2000, verbose_name=_('Content'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post',verbose_name=_('Author'))
    created_at = models.DateTimeField(auto_now_add=True,verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True,verbose_name=_('Updated_at'))

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title
    


##################____________ Using Mongoengine ODM  ______________################



# from django.utils import timezone
# from mongoengine import Document, fields


# class Post(Document):
#     title = fields.StringField(max_length=255,verbose_name=_('Title'))
#     content = fields.StringField(max_length=1000, verbose_name=_('Content'))
#     author = fields.ReferenceField(User,verbose_name=_('Author'))
#     created_at = fields.DateTimeField(default=timezone.now,verbose_name=_('Created at'))
#     updated_at = fields.DateTimeField(default=timezone.now,verbose_name=_('Updated_at'))  

#     def __str__(self):
#         return self.title   