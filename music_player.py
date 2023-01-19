from pygame import mixer
mixer.init()
mixer.music.load("D:\\js+python ultimate\\day2\python\\2pac - Careless Whisper ( 128kbps ).mp3")
x=float(input("set the volume between 0 to 1.0 "))
setvolume=mixer.music.set_volume(x)
while True:
    print("enter p to play pa to pause r to resume and e to exit ")
    query=input(" ")
    if query=='p':
        mixer.music.play()
    elif query=='pa':
        mixer.music.pause()
    elif query=='r':
        mixer.music.unpause()
    elif query=='e':
        mixer.music.stop()
        break