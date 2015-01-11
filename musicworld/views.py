from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect

from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

from django import forms
from django.forms import ModelForm 
from django.core.context_processors import csrf

from musicworld.models import User
from musicworld.models import Article
from musicworld.models import Comment
from musicworld.models import Periodical
from musicworld.models import Pcomment
from musicworld.models import Userinformation
from musicworld.models import Ptype
#form
class UserForm(forms.Form): 
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())

#homepage(befor login)
def home(request):
    latest_article_list = Article.objects.order_by('-id')[:5]
    username = request.COOKIES.get('username','')
    context = {'latest_article_list': latest_article_list,'username':username}
    return render(request, 'articles.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article_id=article.id)
    return render(request, 'singlearticle.html', {'article': article,'comments': comments})


#show article
def article(request):
    latest_article_list = Article.objects.order_by('-id')[:5]
    recommend= Article.objects.order_by('-likes')[:5]
    username = request.COOKIES.get('username','')
    context = {'latest_article_list': latest_article_list,'username':username,'recommend':recommend}
    return render(request, 'articles.html', context)


def adetail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article_id=article.id)
    return render(request, 'singlearticle.html', {'article': article,'comments': comments})

#regist
def regist(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #get date of form
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #add into database
            User.objects.create(username= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

#login
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #get data
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #compare with the database
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                #match,go into index
                response = HttpResponseRedirect('/musicworld/index/')
                #set cookie
                response.set_cookie('username',username,3600)
                return response
            else:
                #doesnt match,still login page
                return HttpResponseRedirect('/musicworld/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

#login success
def index(req):
    username = req.COOKIES.get('username','')
    latest_periodical_list = Periodical.objects.order_by('-timestamp')[:3]
    a=latest_periodical_list[0]
    b=latest_periodical_list[1]
    c=latest_periodical_list[2]
    latest_article_list = Article.objects.order_by('-timestamp')[:3]
    d = Article.objects.order_by('-likes')[:1]
    return render_to_response('index.html' ,{'username':username,'latest_article_list':latest_article_list,'a':a,'b':b,'c':c,'d':d})

#logout
def logout(req):
    response = HttpResponse('logout !!')
    #delete cookie
    response.delete_cookie('username')
    return response


#create comment
class CommentForm(forms.ModelForm):    
    class Meta:  
        model = Comment 
        fields = ['content']



def create(request,article_id):
    a = Article.objects.get(id=article_id)

    if request.method == "POST":
        form = CommentForm(request.POST) 
        
        if form.is_valid():

            c = form.save(commit=False)
            c.article = a
            c.save()


            return HttpResponseRedirect('/musicworld/%s' % article_id)
    else:
        form = CommentForm()

    args = {}
    args.update(csrf(request))

    args['article'] = a
    args['form'] = form

    return render_to_response('create_comment.html',args)

#add likes
def like_article(request,article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		count = a.likes
		count += 1
		a.likes = count
		a.save()
	return HttpResponseRedirect('/musicworld/article/%s' % article_id)

#add likes periodical
def like_periodical(request,periodical_id):
    if periodical_id:
        a = Periodical.objects.get(id=periodical_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    return HttpResponseRedirect('/musicworld/periodical/%s' % periodical_id)  	


#show peridical
def phome(request):
    latest_periodical_list = Periodical.objects.order_by('-timestamp')[:5]
    popularp = Periodical.objects.order_by('-likes')[:5]
    username = request.COOKIES.get('username','')
    context = {'latest_periodical_list': latest_periodical_list,'username':username,'popularp': popularp}
    return render(request, 'periodical.html', context)

def pdetail(request, periodical_id):
    periodical = get_object_or_404(Periodical, pk=periodical_id)
    pcomments = Pcomment.objects.filter(periodical_id=periodical.id)
    return render(request, 'singleperiodical.html', {'periodical': periodical,'pcomments': pcomments})


#create article
class ArticleForm(forms.ModelForm):    
    class Meta:  
        model = Article 
        fields = ['name','content','articleimage','music']


def create_article(request):
    
    if request.method == "POST":
        
        form = ArticleForm(request.POST, request.FILES)
        username = request.COOKIES.get('username','')
        
        if form.is_valid():
            
            form.articleimage = Article(articleimage = request.FILES['articleimage'])
            form.music = Article(music = request.FILES['music'])
            form.author = username
            form.save()

            return HttpResponseRedirect('/musicworld/article')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_article.html',args)



def video(request):
    return render(request, 'video.html')

def user(request):

    info = Userinformation.objects.order_by('-timestamp')[:1]
    return render(request, 'user.html', {'info': info})

def contact(request):
    return render(request, 'contact.html')


#create pcomment
class PcommentForm(forms.ModelForm):    
    class Meta:  
        model = Pcomment 
        fields = ['content']


def pcreate(request,periodical_id):
    a = Periodical.objects.get(id=periodical_id)

    if request.method == "POST":
        form = PcommentForm(request.POST) 
        
        if form.is_valid():

            c = form.save(commit=False)
            c.periodical = a
            c.save()


            return HttpResponseRedirect('/musicworld/periodical/%s' % periodical_id)
    else:
        form = PcommentForm()

    args = {}
    args.update(csrf(request))

    args['periodical'] = a
    args['form'] = form

    return render_to_response('create_pcomment.html',args)
