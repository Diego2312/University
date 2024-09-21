
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Ajeje the librarian, recently found a hidden room
in the Keras Library (a great place located in
Umkansa, the largest village in the White Mountains).
There, she discovered several books, containing
music scores of ancient Tarahumara songs.
So, she invited over a musician friend to have a look
at them, and he informed her that the scores are
written in Tarahumara notation and need to be translated
into a notation familiar to Umkansanian musicians,
so they can play them back.

Tarahumaras used numbers instead of letters for
writing notes:
0 in place of A, 1 in place of B, and so on, until
7 in place of G. Flat (b) and sharp (#) notes
(see note 3 below, if you do not know what flat
and sharp notes are)
were followed by a - and a +, respectively (for example,
0- meant flat A). Moreover, they just repeated the
same number multiple times to represent the note's
duration. For example, 0000 would mean that the
A note had a length of 4, while 0-0-0-0- would mean
that the A flat note had a length of 4.
Pauses were written down
as spaces; for example, twelve spaces represent
a pause of 12. Both notes and pauses could span
different lines of the score (e.g., starting on line
x and continuing on line x + 1, x + 2, and so on).
Finally, music scores were written from right
to left and from top to bottom, and going to a new
line did not mean anything in terms of the music score.
Umkansanians, instead, are used to write down notes using letters,
and each note is followed by its duration (so, the example
above would be written as A4). Flat and sharp notes are
followed by a b or a #, respectively (for example, A flat
is written as Ab, so the example above would be written ad
Ab4). Pauses are written using the letter P, followed by
their duration, and no spaces are used at all.
Finally, they are used to read music from left
to right on a single row.

As Ajeje knows that you are a skilled programmer, she
provides you with a folder containing the transcription
of all the Tarahumara songs she found, organized in
multiple subfolders and files (one song per file).
Also, she prepared an index file in which each row
contains the title of a Tarahumara song (in quotes),
followed by a space and the path of the file containing
that song (in quotes, relative to the root folder).
She would like to translate all the songs listed in
the index and store them into new files, each one
named with the title of the song it contains (.txt),
in a folder structure matching the original one.
Also, she would like to store in the root folder of
the created structure, a file containing on each row
the title of a song (in quotes) and the corresponding
song length, separated by a space. Songs in the index
need to be ordered in descending length and, if the
length of some songs is the same, in ascending alphabetical
order. The length of a song is the sum of the durations
of all notes and pauses it is made of.

Would you be able to help Ajeje out in translating
the Tarahumara songs into Umkansanian ones?

Note 0: below, you are provided with a function to
Umkansanize the Tarahumara songs; after being executed,
it must return a dictionary in which each key is a song
title and the associated value is the song's duration

Note 1: the songs index file index.txt
is stored in the source_root folder

Note 2: the index of the translated songs
index.txt is in the target_root folder

Note 3: flat and sharp notes are just "altered" versions
of regular notes; for example an F# ("F sharp") is the
altered version of an F, that is, an F note which is a
half of a tone higher than a regular F; the same holds for
flat notes, which are a half of a tone lower than regular notes;
from the point of view of the homework, flat and sharp notes
must be treated the same as regular notes (except for their notation).

Note 4: to create the directory structure you can use the 'os' library functions
(e.g. os.makedirs)
'''

from os import makedirs




def translate(file_path, dic):
    fref = open(file_path, 'r', encoding='utf-8')
    
    #Reverse the song and remove the new lines (ready to be translated)
    rsong = "".join([i[::-1].strip('\n') for i in fref.readlines()])
    
    
    #Mutating the string so every not is 2 characters long
    newsongstr = []
    tamrsong = len(rsong)
    tamrsong1 = tamrsong -1 
    for i in range(tamrsong):
        if i == tamrsong1:
            if rsong[i].isdigit() or rsong[i] == " ":
                newsongstr.append(rsong[i] + '_') #Adding '_' to every normal note
            else:
                newsongstr.append(rsong[i])
            break

        if rsong[i+1] == '+' or rsong[i] == '+' or rsong[i+1] == '-' or rsong[i] == '-':
            newsongstr.append(rsong[i])
        else:
            newsongstr.append(rsong[i] + '_')

    newsongstr ="".join(newsongstr)
            
    #Transforming the mutated string in to a list of every note
    n = 2
    lisnewsong = [newsongstr[i:i+n] for i in range(0, len(newsongstr), n)]
    
    #Translation
    translatedlis =[]
    counts = 0
    tamlisnewsong = len(lisnewsong)
    tamlisnewsong1 = tamlisnewsong -1 
    for i in range(tamlisnewsong):
        if i == 0 or lisnewsong[i] != lisnewsong[i - 1]: #Check if the note should be translated
            if i == tamlisnewsong1:
                translatedlis.append(dic[lisnewsong[i]] + "1")
                counts+= 1
                break
            if lisnewsong[i + 1] == lisnewsong[i]: #Check if the note repeats
                slisong = lisnewsong[i:]
                tamslisong = len(slisong)
                tamslisong1 = tamslisong - 1
                count = 0 
                reps = 0
                # Only exists because of index out of range
                while slisong[count] == lisnewsong[i]:
                    if count == tamslisong1: # Handle index out of range
                        reps += 1
                        break
                    reps += 1
                    count += 1
                translatedlis.append(dic[lisnewsong[i]] + str(reps))
                counts += reps
            else:
                translatedlis.append(dic[lisnewsong[i]] + "1")
                counts += 1
    
    translated = "".join(translatedlis)
    return [translated, counts]


def extract_names(indfile):
    fr = open(indfile+'/index.txt', 'r', encoding='utf-8')      
    #Get every line of the index file(with no \n)
    lines = [i.strip() for i in fr.readlines()]      
    fr.close()
    
    tamlines = len(lines)
    #Get all the song file names
    inds = [lines[i].split()[-1][1:-1] for i in range(tamlines)]
    
    #Get all the song names
    names = [' '.join(lines[i].split()[:-1]) for i in range(tamlines)]
    
    
    return [inds, names]


def srt(tup):
    tamanho = tup[1]
    alph = [ord(i) for i in tup[0]]

    return -tamanho, alph
     
def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
    
    transdic = {str(i)+'_':n.upper() for i, n in enumerate(map(chr, range(ord('a'), ord('g')+1)))
                } | {str(i)+'+':n.upper()+'#' for i, n in enumerate(map(chr, range(ord('a'), ord('g')+1)))
                     } | {str(i)+'-':n.upper()+'b' for i, n in enumerate(map(chr, range(ord('a'), ord('g')+1)))
                          } |{" "+"_": "P"}
    
    file_names =  extract_names(source_root)[0]
    song_names = extract_names(source_root)[1]

    
    
    splf = ['/'.join(i.split('/')[:-1]) for i in file_names if len(i) > 1] #Make a list with a paths to songs, but without the actual song.txt files
    lens = {} 
    
    
    #Create all directories and write in files
    makedirs(target_root)
    
  
    tamsplf =len(splf)
    for i in range(tamsplf): #First creat all directories(not considering the txt files)
        tamsplfi = len(splf[i])
        if tamsplfi > 0:
            makedirs(target_root + '/' + splf[i], exist_ok=True)
        fr = open(target_root + '/' + splf[i] + '/' + song_names[i][1:-1] + '.txt', 'w', encoding='utf-8') #Open and write each song file, with their given path
        ji = [translate(source_root + '/' + file_names[i], transdic)[0], translate(source_root + '/' + file_names[i], transdic) [1]]
        fr.write(ji[0])
        lens[song_names[i][1:-1]] = ji[1]
        fr.close()
        
     
        
     
    slis = sorted(lens.items(), key=srt)
    sdic = dict(slis)   
    skeys =  [i for i in sdic]
    tamsdic = len(sdic)
    
  
    fi = open(target_root + '/index.txt', 'w', encoding='utf-8') 
    for i in range(tamsdic):
        fi.write('"'+skeys[i]+'"' + ' ' + str(sdic[skeys[i]]) + '\n')
    fi.close()
    
    return sdic

""""
Use map function to translate. Donn`t transform in to list
"""

if __name__ == "__main__":
    #print(Umkansanize("C:\\Users\\Owner\\ACSAI\\Homeworks\\HW4req\\test06", "Umkansanian"))
    #translate("C:\\Users\\Owner\\ACSAI\\Homeworks\\HW4req\\test05\\0.txt", transdic)
    pass


