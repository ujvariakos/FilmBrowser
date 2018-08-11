import os
import subprocess


class VLC_Handle:

    def StartVLC(self, FilePath):
        p = subprocess.Popen([os.path.join("D:/", "programs", "vlc", "program", "VLC", "vlc.exe"),
                              os.path.join(FilePath)])

        # process = subprocess.Popen(['ffmpeg',  '-i', FilePath], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # stdout, stderr = process.communicate()
        # matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()
        # process.kill()
        # duration = {'hours': matches['hours'], 'minutes' : matches['minutes'], 'seconds' : matches['seconds'], 'total_in_sec' : float(matches['seconds']) + 60 * float(matches['minutes']) + 3600 * float(matches['hours'])}
        # return duration

    # def getFilms(self, filmPath):
    #    FilmSize = 1000000
    #    folderList = os.listdir(filmPath)
    #    filmNum = 0
    #    films = list()
    #    directory_list = list()
    #    for f in folderList:
    #        newPath = filmPath+ (r"\\") + f
    #        filmList = os.listdir(newPath)
    #        for film in filmList:
    #            fullpath = newPath + r"\\" + film
    #            # film is a film?
    #            if(os.path.isfile(fullpath)):
    #                if(os.path.getsize(fullpath) > FilmSize):
    #                    filmNum += 1
    #                    films.append(fullpath)
    #            else:
    #                directory_list.append(fullpath)
    #                while directory_list:
    #                    another_full_Path = directory_list.pop()
    #                    filmList1 = os.listdir(another_full_Path)
    #                    for film1 in filmList1:
    #                        another_full_Path1 = another_full_Path + r"\\" + film1
    #                        if(os.path.isfile(another_full_Path1)):
    #                            if(os.path.getsize(another_full_Path1) > FilmSize):
    #                                filmNum += 1
    #                                films.append(another_full_Path1)
    #                        else:
    #                            directory_list.append(another_full_Path1)
    #    return films

    def getFilms(self, filmPath):
        # FilmSize = 1000000
        movie_extensions = ['avi', 'dat', 'mp4', 'mkv', 'vob']
        filmNum = 0
        films = list()
        directory_list = list()
        directory_list.append(filmPath)
        while directory_list:
            fullPath = directory_list.pop()
            filmList = os.listdir(fullPath)
            for film in filmList:
                # filePath = fullPath + r"\\" + film
                filePath = os.path.join(fullPath, film)
                if (os.path.isfile(filePath)):
                    # if(os.path.getsize(filePath) > FilmSize):
                    for movie_extension in movie_extensions:
                        if not filePath.endswith(movie_extension):
                            continue
                        filmNum += 1
                        films.append(filePath)
                else:
                    directory_list.append(filePath)
        return films