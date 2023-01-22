from moviepy.video.io.VideoFileClip import VideoFileClip
import sys
from moviepy.video.fx.speedx import speedx

# récupération des arguments passés lors de l'exécution du script
input_video = sys.argv[1]
stretch_duration = float(sys.argv[2])
output_video = sys.argv[3]

# ouverture de la vidéo d'entrée
clip = VideoFileClip(input_video)


# récupération de la durée de la vidéo initiale
original_duration = clip.duration

# calcul du stretch_factor
stretch_factor = stretch_duration / original_duration


# calcul du stretch_duration
stretch_duration = original_duration * stretch_factor




# étirement de la vidéo
#stretch_factor = 2
stretch_clip = speedx(clip, factor=1/stretch_factor)

# augmenter le framerate de la vidéo de sortie à 20fps
stretch_clip = stretch_clip.set_fps(int(20))

# écriture de la vidéo étirée dans le fichier de sortie
stretch_clip.write_videofile(output_video, codec='libx264')
