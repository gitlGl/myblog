
from django.shortcuts import render, get_object_or_404
from blog1.models import Post,Category
import time
def index(request):#hjfhjfkljhlfkgn lgbnl

    return render(request,'blog1/index.html')


def bowen(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog1/bowen.html',
                  context={'post_list': post_list})


def detail(request, pk):

    post = get_object_or_404(Post, pk=pk,)

    return render(request, 'blog1/detail.html', context={'post': post})


def time_list_conment(request):
    '''
    postlist =  Post.objects.filter(
    created_time__range=(["2019-07-01", "2019-07-31"]))
    start = datetime.date(2018, 7, 12)
    end = datetime.date(2018, 7, 13)

    model.objects.filter(date_time_filed__range=(start, end))

    '''
    post_list1 = []
    for i in range(2019,int(time.localtime()[0])+1):
        for i2 in range(12):
            postlist =  Post.objects.filter(created_time__year = i,
                                                created_time__month = i2)
            if postlist is not None :
                post_list1.append(postlist)
    return render(request, 'blog1/title.html',
                  context={'post_list1': post_list1 })

def Category_page(request,category1):
    post1 = Post.objects.all().order_by('-created_time')

    post_list = post1.filter(category = category1)


    #post_list = Post.objects.all().order_by('-created_time', category1)
    title = get_object_or_404(Category, pk=category1)
    return render(request, 'blog1/Category_page.html',
             context={'post_list': post_list,'title':title})




def trys(request):
    return render(request, 'blog1/try.html')