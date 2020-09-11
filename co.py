from welcome.models import *


def s(d):
    n = min(10, d.__len__())
    L = sorted(d.items(), key=lambda item: item[1], reverse=True)
    L = L[:n]
    d2 = {}
    for l in L:
        d2[l[0]] = l[1]
    return d2


def c():
    for actor in Actor.objects.all():
        cos = {}
        for movie in actor.movie_set.all():
            for co in movie.actors.all():
                if co.myID != actor.myID:
                    if co.myID in cos.keys():
                        cos[co.myID] += 1
                    else:
                        cos[co.myID] = 1
        ordered = s(cos)
        for key, value in ordered.items():
            actor.coworker_set.create(myID=key, times=value)
    print("done")


def re():
    for movie in Movie.objects.all():
        movie.name = movie.name.replace('#39;s ', '')
        movie.save()
    print("done")


def ac():
    for actor in Actor.objects.all():
        for movie in actor.movie_set.all():
            actor.short = actor.short + movie.name
            actor.save()
    print("done")


def sh():
    for comment in Comment.objects.all():
        comment.short = comment.movie.name
        comment.save()
    print("done")
