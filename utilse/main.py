import os
import time

print("je lance la capture vidéo")
os.system("python3 recorder.py")

print(".")
time.sleep(3)
print("je fait une vidéo timelaps")
os.system("python3 laps.py output.avi 10 end.mp4")
print("video étirer")
os.system("mv output.avi ../www/res/long.avi")
os.system("mv end.mp4 ../www/res/short.mp4")
print("fichier placer sur le serveur")
print("j'ai fini, je l'indique en ecrivant dans le fichier stat")

print("je gener les tag")
os.system("python3 tager.py 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")

f = open("../www/stat.txt", "w+")
f.write("1")
f.close()

print("fini")