from django.db import models

from django.contrib import admin
# Create your models here.
#class of user
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


#list user in admin to show username and password
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

#class of article and properties of it
class Article(models.Model):
    #__table__ = 'articles'

    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    music = models.FileField('article-music',upload_to='music/article')
    content = models.TextField(max_length=1000)
    articleimage = models.FileField('article-image',upload_to='image/article')
    timestamp = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    
    def __str__(self):
        return self.name

#list article in admin to show name and timastamp
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name','timestamp')


#class of comment and properties of it
#set article as a foreignkey to it
class Comment(models.Model):
    #__table__ = 'acomment'

    timestamp = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1000)
    article = models.ForeignKey(Article)


    def __str__(self):
        return self.content

#class type pf periodical
class Ptype(models.Model):
    #__table__ = 'Ptype'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#class of periodical and properties of it
#set ptype as a foreignkey to it
class Periodical(models.Model):
    #__table__ = 'periodicals'

    name = models.CharField(max_length=200)
    ptype = models.ForeignKey(Ptype)
    content = models.TextField(max_length=1000)
    image = models.FileField('periodical-image',upload_to='image/periodical')
    timestamp = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


#class of periodical's comment and properties of it
#set periodical as a foreignkey to it
class Pcomment(models.Model):
    #__table__ = 'acomment'

    timestamp = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=1000)
    periodical = models.ForeignKey(Periodical)


    def __str__(self):
        return self.content

#class of music and properties of it
#set article as a foreignkey to it
class Music(models.Model):
    #__table__ = 'musics'

    name = models.CharField('music-title',max_length=200)
    artist = models.CharField('music-artist',max_length=200)
    album = models.CharField('music-album',max_length=200)
    musicimage = models.FileField('music-image',upload_to='image/musics',max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    periodical = models.ForeignKey(Periodical)
    music = models.FileField('musicM',upload_to='music/musics')
    
    def __str__(self):
        return self.name


#class of userinformation and properties of it
class Userinformation(models.Model):
    #__table__ = 'users'

    email = models.CharField(max_length=200,null=True)
    hobby = models.CharField(max_length=200,null=True)
    image = models.FileField('user-image',upload_to='/image/userinformation',null=True)
    user = models.OneToOneField(User)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hobby
