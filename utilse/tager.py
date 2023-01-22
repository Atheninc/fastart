import openai
import sys
import os

openai.api_key = sys.argv[1]

def getRep(txt, stop = "=========="):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=txt,
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response["choices"][0]["text"]


def index(tmp, ocu):
    try:
        return tmp.index(ocu)
    except:
        return -1

def imp_param():
    f = open("param.txt", "r")
    txt = f.read()
    f.close()
    return txt

def gen_desc_tag(nom, act, desc = ""):
    
    f = open("template.txt", "r")
    txt = f.read()
    f.close()

    tmp = ""
    tmp += "nom: " + str(nom) + "\n"
    tmp += "domaine: " + str(act) + "\n"
    if (desc != ""):
        tmp += "description: " + str(desc) + "\n"
    tmp += "tag: "

    tmp = imp_param()

    txt += tmp
    print(txt)
    t = "."
    rep = ""
    while (index(t, "==========") == -1):
        t = getRep(txt + rep)
        rep += t
        print(t)
        if (t == ""):
            rep += "\n"
    os.system("clear")
    print(rep.split("==========")[0])
    
    f = open("../www/res/tag.txt", "w+")
    f.write(rep)
    f.close()
    return rep

gen_desc_tag("scene de combat", "composition", "je produit une scene 3d bataille sur unity pour une cinematique de jeux vidéo")