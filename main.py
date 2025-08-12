#!/usr/bin/env python3

from py7zr import unpack_7zarchive
import shutil
import os

folder = os.getcwd()
shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)

if not os.path.exists('decompressed/'):
   os.mkdir('decompressed')

for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    infile= open(infilename, 'r')
    newname = infilename.replace('.tar', '.7z')
    output = os.rename(infilename, newname)

for file in os.listdir(folder):
    if file.endswith(".7z"):
        shutil.unpack_archive(file, 'decompressed/')
        print(f'Deleting file: {file}')
        os.remove(file)

decompressedFolder = folder + '/decompressed'

for folders in os.listdir(decompressedFolder):
    currentArtist = folders.split('-')[0].strip()
    for file in os.listdir('decompressed/' + folders):
        if file.endswith(".url"):
            os.remove(decompressedFolder + '/' + folders + '/' + file)

    newFolder = 'decompressed/' + currentArtist
    if not os.path.exists(newFolder):
        os.mkdir(newFolder)

    print(f'Updated: {folders} - > {newFolder} ')
    shutil.move(decompressedFolder + '/' + folders, newFolder)

print("Process completed")