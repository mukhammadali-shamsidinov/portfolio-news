from .models import News

def lastest(request):
    context = {
        'lastest_news':News.publish.all().order_by('-published_time')[:10]
    }
    return context