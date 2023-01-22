import eel
import os

eel.init("www")  

def ini_stat():
    f = open("rec_stat.txt", "w+")
    f.write("0")
    f.close()
    

    f = open("www/stat.txt", "w+")
    f.write("")
    f.close()

ini_stat()

@eel.expose
def start_rec(txt):
    
    print("démarage de l'enregistrement vidéo")
    
    f = open("rec_stat.txt", "w+")
    f.write("1")
    f.close()
    
    print("...")

    f = open("param.txt", "w+")
    f.write(txt)
    f.close()
    print(txt)
    print("j'ai sauvgarder les parametre")

@eel.expose
def stop_rec():
    print("arret de l'enregistrement")
    f = open("rec_stat.txt", "w+")
    f.write("0")
    f.close()
    os.system("cd utilse && python3 main.py &")

# Start the index.html file
eel.start("index.html", mode="google-chrome")