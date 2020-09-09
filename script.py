import os
import json
from welcome.models import *


def m():
    filedir = "D:\\vscpython\\summer\\data\\movies_new\\"
    filenames = os.listdir(filedir)
    for filename in filenames:
        myID = filename.replace('.json', '')
        with open(filedir + filename, 'rb') as f:
            data = json.load(f)
            name = data['name']
            image = data['image']
            directors = ""
            for director in data['director']:
                directors += director['name'] + "/"
            authors = ""
            for author in data['author']:
                authors += author['name'] + "/"
            actorsShort = ""
            actorsID = []
            for actorShort in data['actor']:
                actorsShort += actorShort['name'] + "/"
                actorsID.append(actorShort['url'].replace('celebrity', '').replace('/', ''))
            profile = data['description'].replace('\u3000', ' ')
            rating = data['aggregateRating']['ratingValue']
            movie = Movie(myID=myID,
                          name=name,
                          image=image,
                          directors=directors,
                          authors=authors,
                          actorsShort=actorsShort,
                          profile=profile,
                          rating=rating)
            movie.save()
            for actorID in actorsID:
                movie.actors.add(Actor.objects.get(myID=actorID))
            for comment in data['comments']:
                movie.comment_set.create(content=comment)
    print("done")
