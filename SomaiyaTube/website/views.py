from django.shortcuts import render,redirect
from django.contrib import messages

from .models import User, Comment, NewVideo
from django.http import HttpResponseRedirect
from datetime import date
from django.db.models import Q

clicks={}

from django.views.generic import TemplateView,ListView

class HomePageView(TemplateView):
    template_name = 'home.html'


def homepage(request):
    #username=User.objects.filter(name=User.username)

    if request.method =='GET' and 'q' in request.GET:
        print("Search")
        query = request.GET.get('q')
        videos = NewVideo.objects.filter(Q(title__icontains=query))

    else:
        videos=NewVideo.objects.all()
    
    return render(request,'homepage.html',{'videos':videos})


def video(request,pk):
    video = NewVideo.objects.get(pk=pk)
    print(video)
    comments=Comment.objects.filter(video = video)
    count = Comment.objects.filter(video = video).count()
    if request.method=="POST":
        print(request.POST)
        if 'Addcomment' in request.POST:
            text = request.POST['Addcomment']
            user = User.objects.first()
            comment = Comment.objects.create(
                user = user,
                text = text,
                video = video
            )
        elif 'Like' in request.POST:
            video.likes= video.likes+1
            video.save()
        elif 'Dislike' in request.POST:
            video.dislikes= video.dislikes+1
            video.save()





        return redirect('ViewVideo',pk=pk)

    return render(request,'videoView.html',{'video':video,'comments':comments,'count':count})
        #Make the thumbs up and down icon a button
        #likes++ dislikes++
        #comment=request.POST["comment"]
        # add videoid=
        #commentobj=Comment(user=User.username,comment=comment) #add which video he had selected.



def upload(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    else:
        if request.method == "POST":
            title = request.POST['title']
            desc = request.POST['desc']
            thumbnail =  request.FILES['thumbnail']
            video =  request.FILES['video']

            videoobj= NewVideo(user=request.user,title=title,description=desc, date=date.today(),thumbnail=thumbnail,video=video )
            videoobj.save()
            return redirect('homepage')
        return render(request,'upload.html',{})


class SearchResultsView(ListView):
    model = NewVideo
    template_name = 'search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        global clicks
        if query in clicks:
            clicks[query]+=1
        else:
            clicks[query]=1
        return NewVideo.objects.filter(
            Q(title__icontains=query)
        )

class Trending_View(ListView):
    model = NewVideo
    template_name = 'trending_results.html'
    global clicks
    clicks1=dict(clicks)

    def get_queryset(self):
        clicks1=dict(clicks)
        a=NewVideo.objects.values_list('title')
        max_list=[]
        trend_list=[]
        print(clicks1)
        for i in range(1):
            try:
                Keymax = max(clicks1, key=clicks1.get)

                max_list.append(Keymax)
                clicks1.pop(Keymax)
            except:
                pass

        for i in a:
            for j in i:
                print(j)
                if j in max_list:

                    trend_list.append(j)
        print(trend_list)
        return NewVideo.objects.filter(
            Q(title__icontains=trend_list[0])
        )
