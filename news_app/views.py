from django.shortcuts import render,get_object_or_404,HttpResponse
from django.views.generic import TemplateView, ListView

from .models import News,Category
from .forms import contactForm
# Create your views here.
def News_list(request):
    news = News.objects.filter(status=News.Status.Published)
    categories = Category.objects.all()
    context = {
        "news_list":news,
        'categories':categories
    }

    return render(request,'news/news_list.html',context)



def News_detail(request,news):
    news = get_object_or_404(News,slug=news,status=News.Status.Published)

    context = {
        "news":news
    }
    return render(request,'news/news_detail.html',context)

def homeView(request):
    news = News.objects.filter(status=News.Status.Published).order_by('-published_time')[:10]
    category = Category.objects.all()
    local_one = News.publish.filter(category__name='mahalliy').order_by('-published_time')[:1]
    local_news = News.publish.filter(category__name='mahalliy').order_by('-published_time')[1:6]

    context = {
        "news":news,
        "category":category,
        "local_one":local_one,
        "local_news":local_news
    }

    return render(request,'news/index.html',context)


class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['news'] = News.objects.filter(status=News.Status.Published).order_by('-published_time')[:10]
        context['mahalliy'] = News.publish.filter(category__name='mahalliy').order_by('-published_time')[:6]
        context['xorij'] = News.publish.filter(category__name='xorij').order_by('-published_time')[:6]
        context['texnologiya'] = News.publish.filter(category__name='texnologiya').order_by('-published_time')[:6]
        context['sport'] = News.publish.filter(category__name='sport').order_by("-published_time")[:6]
        return context

# def contactPageView(request):
#
#     form = contactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse('<h1>Thanks bro</h1>')
#     context = {
#         "form":form
#     }
#     return render(request,'news/contact.html',context)

class contactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self,request,*args,**kwargs):
        form = contactForm()
        context = {
            "form":form
        }
        return render(request,'news/contact.html',context)
    def post(self,request):
        form = contactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('<h1>Thanks bro</h1>')

        context = {
                "form":form
            }

        return render(request,'news/contact.html',context)
def error404(request):
    return render(request,'news/404.html')



class localNews(ListView):
    model = News
    template_name = 'news/mahalliy.html'
    context_object_name = 'mahalliy_news'

    def get_queryset(self):
        news = self.model.publish.all().filter(category__name="mahalliy")
        return news


class texnoPage(ListView):
    model = News
    template_name = 'news/texno.html'
    context_object_name = 'texno_news'

    def get_queryset(self):
        news = self.model.publish.all().filter(category__name="texnologiya")
        return news

class sportPage(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.publish.all().filter(category__name="sport")
        return news

class xorijPage(ListView):
    model = News
    template_name = 'news/xorij.html'
    context_object_name = 'xorij_news'

    def get_queryset(self):
        news = self.model.publish.all().filter(category__name="xorij")
        return news
