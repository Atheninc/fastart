Présentation
Fastart est une solution automatisée pour la création de timelapse. Il permet de capturer des images à intervalles réguliers et de les assembler en une vidéo accélérée en un seul clic.

Fonctionnalités
Interface graphique pour une utilisation simplifiée
Possibilité de spécifier les tâches à effectuer
Possibilité de générer des tags et des descriptions pour les réseaux sociaux
Automatisation de l'étirement de la vidéo
Utilisation
Fastart est basé sur Python3, il nécessite donc d'avoir Python3 installé sur votre ordinateur. Il utilise les bibliothèques suivantes:

pyscreenshot
numpy
openCV
moviepy
eel
openai
Il faut installer ces dépendances avant de lancer le programme.

Une fois les dépendances installées, vous pouvez lancer le programme en utilisant la commande suivante:

Copy code
python3 fastart.py
Une fois lancé, une interface graphique s'affichera dans votre navigateur web. Il vous suffit de remplir le formulaire pour spécifier les tâches à effectuer et de cliquer sur "Start" pour démarrer l'enregistrement. Vous pouvez ensuite cliquer sur "Stop" pour arrêter l'enregistrement et générer automatiquement la timelapse et les tags et descriptions pour les réseaux sociaux.

Remarque
Il est important de noter que pour utiliser la fonctionnalité de génération de tags et de descriptions, vous devez avoir une clé API OpenAI valide. Il faut la renseigner dans le fichier "tags.py"

N'hésitez pas à nous faire part de tout bug ou demande de fonctionnalité supplémentaire sur la page Github du projet. Nous nous efforcerons de les intégrer dans les versions futures.
