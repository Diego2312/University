#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''It is a quiet December evening, and while it's pouring rain outside
you get a call from your friend Bart, who is not very computer
savvy. After calming him down, he tells you that he went to his PC to
look for the perfect gift, surfing on exotic and alternative
e-commerce sites, doing searches on disparate sites using an automatic
translator. He tells you he ended up on a site with the .atp domain,
thinking it had something to do with tennis, his great passion. After
following a couple of products on the strange site, he noticed that
his browser was responding more slowly and the mouse pointer was
starting to flicker. After a few seconds, a warning message appeared
informing him that he had been infected with the latest generation of
ransomware, which targets sensitive files. Panicked, he remembered
your venture with the Tarahumara sheet music and called you to help
him recover his files. The next day, you go to Bart's house and
analyze the situation: as you thought, the ransomware is the infamous
Burl1(ONE), which encrypts PC files by storing the encryption key
inside images with the .png extension, turning them into intricate
puzzles. Because Bart stores his images on an on cloud service, you
manage to retrieve the original images so you can reconstruct the
ransomware's encryption key and decrypt all his precious files. Will
you be able to find all the keys and recover all the files?
Bart is counting on you!

                    ###Rotations###
The Burl1 ransomware stores the encryption key by dividing images with
the .png extension into square tiles and performing or not performing
rotations of the individual tiles of 90, 180 or 270°, that is,
performing one, two or three rotations to the right. The key will
respectively have an 'R' (right) an 'F' (flip) or an 'L' (left),
depending on the rotation made. The absence of rotation reports the
character 'N'.


                    ###Sections###
For each image, it is necessary to reconstruct the encryption key in
the form of a list of strings: each string corresponds to the sequence
of rotations of each tile in a row. So a 100x60 image in which the
tiles are size 20 will hide an encryption key of 15 characters,
organized into three strings of five characters each. In fact, there
will be 5 tiles per row (100//20 = 5) and 3 rows (60//20 = 3). To find
out the rotations performed you have to use the image you retrieved
from the cloud to compare with the encrypted image.


                        ###Main function###
You need to write the function
jigsaw(puzzle_image:str, plain_image:str, tile_size:int, encrypted_file:str, plain_file:str) -> list[str]
that takes as input:
 - the name of the file containing the image with the rotated tiles,
 - the name of the file containing the image with the unrotated tiles,
 - an integer indicating the size of the side of the square tiles, 
 - the name of a text file to be decrypted with the encryption key, and
 - the name in which to save the decrypted file.


                        ###Summary###
The function must reconstruct and return the encryption key hidden in
the image in puzzle_image and use it to decrypt the encrypted file,
saving the plaintext in a file called plain_file. The key is the
sequence of rotations to be made to reconstruct the initial image and
decrypt the input file.


                        ###Rotation example###
For example, comparing the image in test01_in.png with test01_exp.png
and considering the 20-pixel square tiles, it can be determined that
the rotations applied were
  - 'LFR' for the tiles in the first row,
  - 'NFF' for the tiles in the second row, and
  - 'FNR' for the tiles in the third row.
So the key to be returned will be: ['LFR', 'NFF', 'FNR'].



                    ###File decryption###
Decryption of the file is achieved by implementing a transformation
depending on the character of the key in position i, modulo the length of the
key.  For example, if the key is ['LFR', 'NFF', 'FNR'], the key is 9
long, and we need to decrypt the character at position 14 of the input
file, we need to consider the character at position 14%9 = 5 of the
key, i.e., 'F'.
The transformations for decryption are as follows:

  - R = text[i] replaced by the character with following ord
  - L = text[i] replaced by the character with previous ord
  - N = remains unchanged
  - F = swap text[i] with text[i+1]. If i+1 does not exist, we consider
        the character text[0].


                        ###decryption example###
For example, if the key is LFR and the ecrypted text is BNVDCAP, the
plaintext will be AVOCADO since the decryption will be the following:

step     key      deciphering-buffer
1        LFR      BNVDCAP -> ANVDCAP
         ^        ^
2        LFR      ANVDCAP -> AVNDCAP
          ^        ^
3        LFR      AVNDCAP -> AVODCAP
           ^        ^
4        LFR      AVODCAP -> AVOCCAP
         ^           ^
5        LFR      AVOCCAP -> AVOCACP
          ^           ^
6        LFR      AVOCACP -> AVOCADP
           ^           ^
7        LFR      AVOCADP -> AVOCADO
         ^              ^

'''

# %%
import images

def image_grid(image: str, tile_size:int):
    puzzle_lis = images.load(image)
    tampuzzle_lis = len(puzzle_lis)
    tamcols = len(puzzle_lis[0])
    x = 0
    y = 0
    
    sections = []

    for i in range((tampuzzle_lis// tile_size)*(len(puzzle_lis[0])//tile_size)): 
            
        new_rows = puzzle_lis[x:x+tile_size]
        
        new_section = [i[y:y+tile_size] for i in new_rows]
        sections.append(new_section)
        
        if y == tamcols - tile_size:
            y = 0
            x += tile_size
        
        else:
            y += tile_size
    
    return sections
    
    
        
    #new section is equal to all the pixels in the coordinates of the original image
    #all the rows from x to x+ side intersected to all the collumns from y to y + side




def get_column(mat, N, tamat):
  col = []
  for i in range(tamat):
    col.append(mat[i][N])

  return col

def RotateMatrix(matrix, tamat,tamcol):
    rot_matrix = []
    for i in range(tamcol):
      rot_matrix.append(get_column(matrix, i, tamat)[::-1])
    
    return(rot_matrix)
    
      

def compare_images(puzzle_image: str, plain_image: str, tile_size:int):
    puzzle_sections = image_grid(puzzle_image, tile_size)
    plain_sections = image_grid(plain_image, tile_size)
    
    num_rows = len(puzzle_sections[0])
    num_cols = len(puzzle_sections[0][0])
    
    key_dict = {0:'N', 1:'R', 2:'F', 3:'L'}

    key = []

    for i in range(len(puzzle_sections)):
        count = 0
        if puzzle_sections[i] != plain_sections[i]: 
            while puzzle_sections[i] != plain_sections[i]:          
                puzzle_sections[i] = RotateMatrix(puzzle_sections[i], num_rows, num_cols)
                count += 1
        key.append(key_dict[count])
    
    return key
    
def jigsaw(puzzle_image: str, plain_image: str, tile_size:int, encrypted_file: str, plain_file: str) -> list[str]:
    key = compare_images(puzzle_image, plain_image, tile_size)
    tamanho_key = len(key)
    
    with open(encrypted_file, 'r', encoding='utf-8') as fr:
        encrypted_text = fr.read()
    
    encrypted_lis = list(encrypted_text)
    
    decrypted_text = []



    for i in range(len(encrypted_lis)):
        pos = i % tamanho_key
     
        if key[pos] == 'R':
            decrypted_text.append(chr(ord(encrypted_lis[i])+1))
        elif key[pos] == 'L':
            decrypted_text.append(chr(ord(encrypted_lis[i])-1))
        elif key[pos] == 'F':
            try:
                decrypted_text.append(encrypted_lis[i+1])
                encrypted_lis[i+1] = encrypted_lis[i]
            except IndexError:
                decrypted_text.append(decrypted_text[0])
                decrypted_text[0] = encrypted_lis[-1]
        elif key[pos] == 'N':
            decrypted_text.append(encrypted_lis[i])
            
    decrypted_text = ''.join(decrypted_text)
    
    key = ''.join(key)
    
    
    puzzle_lis = images.load(plain_image)
    tamcols = len(puzzle_lis[0])
    sec_row = tamcols//tile_size

    n = sec_row
    newkey = [key[i:i+n] for i in range(0, tamanho_key, n)]
        
    
    with open(plain_file, 'w', encoding='utf-8') as fw:
        fw.write(decrypted_text)

    return newkey
if __name__ == '__main__':
    print(jigsaw('tests/test10_in.png', 'tests/test10_exp.png', 60,
                                      'tests/test10_enc.txt', 'output/test10_out.txt'))
    
'''
The transformations for decryption are as follows:

  - R = text[i] replaced by the character with following ord
  - L = text[i] replaced by the character with previous ord
  - N = remains unchanged
  - F = swap text[i] with text[i+1]. If i+1 does not exist, we consider
        the character text[0].



Usinfg %:
    
The division of the position by the length of the key, the remaining of it will indicate, which position of the key to use
So if position 7 for a key of 3, the key position used will be 1 - 1

ABC SBADBHD
012 0123456

if 5%3 == 2
use 3 position




'''


'''
WHAT MUST BE DONE


Take an image which was deformed by its original, by rotating square sections of n side and find what rotations must be made to reconstruct the image.
Each type of rotation is a letter, so: R(right) - 90, F(flip) - 180, L(left) - 270. So basically either rotate once, twice or three times.
I must store what rotations must be made per row in a list. So imagining a 16grid image, I would a have a list of 4 strings, each string will contain 4 substring(the rotations)

This list of rotations will be used as a key to decrypt texts.
An iteration on both the key and the text is made, and for every Letter of the key, a change is made on the coerresponding current text letter. 


Identifying rotations.

I have two images to compare. My objctive must be to find what rotations must be made on each section to reach plain image.

First step is to divide the image in to the sections:
    If i simply draw the exact same squares on both images, when comparing, the rotations will be equivalent to the images with no squares drawn. (do I need to draw the squares?) 
    Draw squares

Second step: How do i work with each section at a time
I can split the list by the color I use to draw the grid. This way for every new list i have will be a section to rotate.

I can iterate through the blue rows. Ill start with the first row of the image which is blue.
if the pixel bellow the current pixel is blue then the section ended and a new one started.
frow the coordinates of start and end of each section I can say that for each coordinates the section is equal to pixels from the start of the section to the end and the rows from the start pixel to start pixel + section side. (better explained on notebook)


Idea:
    if the section is equal do nothing, if not rotate once, if still not rotate again. The number of ratations needed to equal the image is the type of ration done. So 0 = N, 1 = R, 2 = F, 3 = L
    

'''