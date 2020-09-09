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
            data['profile'] = data['profile'].replace('\u3000', ' ')
            info = "`".join(data['info'])
            Actor.objects.create(myID="1000004",
                                 name=data['name'],
                                 info=info,
                                 profile=data['profile'],
                                 jpg=data['jpg'])
    print("done")
