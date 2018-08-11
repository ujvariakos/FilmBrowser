import subprocess
import os
from VLC_Handle import VLC_Handle

vlcStarter = VLC_Handle()
filmRootPath = r"d:\\filmek"
films = vlcStarter.getFilms(filmRootPath)
i = 0
for chose in films:
    print(i," ",chose)
    i +=1
user_input = input("give the film number: ")
vlcStarter.StartVLC(films[int(user_input)])


