from django.shortcuts import render
from django.http import HttpResponse
from welcome.models import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime


# Create your views here.
def index(request, page=1):
    moviesAll = Movie.objects.all()[(page - 1) * 20:page * 20]
    return render(request, "welcome/index.html", {
        "moviesAll": moviesAll,
        "page": page,
        "max": 52
    })


def index_(request, page):
    moviesAll = Movie.objects.all()[(page - 1) * 20:page * 20]
    return render(request, "welcome/index.html", {
        "moviesAll": moviesAll,
        "page": page,
        "max": 52
    })


def index_j(request):
    page = int(request.GET['page'])
    moviesAll = Movie.objects.all()[(page - 1) * 20:page * 20]
    return render(request, "welcome/index.html", {
        "moviesAll": moviesAll,
        "page": page,
        "max": 52
    })


def actor_list(request, page=1):
    actorsAll = Actor.objects.all()[(page - 1) * 20:page * 20]
    return render(request, "welcome/actor_list.html", {
        "actorsAll": actorsAll,
        "page": page,
        "max": 733
    })


def actor_list_(request, page):
    actorsAll = Actor.objects.all()[(page - 1) * 20:page * 20]
    return render(request, "welcome/actor_list.html", {
        "actorsAll": actorsAll,
        "page": page,
        "max": 733
    })


def actor_list_j(request):
    page = int(request.GET['page'])
    actorsAll = Actor.objects.all()[(page - 1) * 20:page * 20]
    return render(request, "welcome/actor_list.html", {
        "actorsAll": actorsAll,
        "page": page,
        "max": 733
    })


def movie(request, my_id):
    detail = Movie.objects.get(myID=my_id)
    detail.actorsShort = detail.actorsShort[0:700] + '...'
    if detail.actors.all().__len__() >= 12:
        actors = detail.actors.all()[0:12]
    else:
        actors = detail.actors.all()
    comments = detail.comment_set.all()
    return render(request, "welcome/movie.html", {
        "movie": detail,
        "actors": actors,
        "comments": comments
    })


def actor(request, my_id):
    detail = Actor.objects.get(myID=my_id)
    if detail.profile == '':
        detail.profile = "暂无"
    info = detail.info.replace('`', '\n')
    movies = detail.movie_set.all()
    coworkers = []
    times_set = []
    for coworker in detail.coworker_set.all():
        coworkers.append(Actor.objects.get(myID=coworker.myID))
        times_set.append(coworker.times)
    arr = zip(coworkers, times_set)
    return render(request, "welcome/actor.html", {
        "actor": detail,
        "info": info,
        "movies": movies,
        "arr": arr
    })


results = []
cost = [0]


def s_m(keyword):
    results.clear()
    begin = datetime.now()
    for result in Movie.objects.filter(Q(name__contains=keyword) | Q(actorsShort__contains=keyword)):
        results.append(result)
    end = datetime.now()
    tot = (end - begin).total_seconds()
    return tot


def s_a(keyword):
    results.clear()
    begin = datetime.now()
    for result in Actor.objects.filter(Q(name__contains=keyword) | Q(short__contains=keyword)):
        results.append(result)
    end = datetime.now()
    tot = (end - begin).total_seconds()
    return tot


def search(request):
    if request.GET['inlineRadioOptions'] == "option1":
        cost[0] = s_m(request.GET['keyword'])
        return render(request, "welcome/m_s.html", {
            "moviesAll": results[0:20],
            "page": 1,
            "max": len(results) // 20 + 1,
            "cost": cost[0],
            "len": len(results)
        })
    elif request.GET['inlineRadioOptions'] == "option2":
        cost[0] = s_a(request.GET['keyword'])
        return render(request, "welcome/a_s.html", {
            "actorsAll": results[0:20],
            "page": 1,
            "max": len(results) // 20 + 1,
            "cost": cost[0],
            "len": len(results)
        })


def s_m_(request, page):
    moviesAll = results[(page - 1) * 20:page * 20]
    return render(request, "welcome/m_s.html", {
        "moviesAll": moviesAll,
        "page": page,
        "max": len(results) // 20 + 1,
        "cost": cost[0],
        "len": len(results)
    })


def s_m_j(request):
    page = int(request.GET['page'])
    moviesAll = results[(page - 1) * 20:page * 20]
    return render(request, "welcome/m_s.html", {
        "moviesAll": moviesAll,
        "page": page,
        "max": len(results) // 20 + 1,
        "cost": cost[0],
        "len": len(results)
    })


def s_a_(request, page):
    actorsAll = results[(page - 1) * 20:page * 20]
    return render(request, "welcome/a_s.html", {
        "actorsAll": actorsAll,
        "page": page,
        "max": len(results) // 20 + 1,
        "cost": cost[0],
        "len": len(results)
    })


def a_m_j(request):
    page = int(request.GET['page'])
    actorsAll = results[(page - 1) * 20:page * 20]
    return render(request, "welcome/a_s.html", {
        "actorsAll": actorsAll,
        "page": page,
        "max": len(results) // 20 + 1,
        "cost": cost[0],
        "len": len(results)
    })
