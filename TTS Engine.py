from gtts import gTTS
from pygame import mixer
blabla="Ye bolke dikha"
#blabla=input()
blabla=str(input())
tts=gTTS(text=blabla,lang='hi')
tts.save("test2.mp3")
mixer.init()
mixer.music.load('test2.mp3')
mixer.music.play()
