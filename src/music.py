import gtts
import playsound

text="A"
sound= gtts.gTTS(text,lang="en")
sound.save("sign.mp3") #location daaldo na yaha  C://skjsdl/djksb/sign.mp3 dave hhogi ye pehle, koi b location daaldo
playsound.playsound("C:/Users/Dell/Desktop/American Sign Language/sign.mp3")