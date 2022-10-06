#Before using this code you need to install the following library: pydub -> pip install pydub

#Import the necessary libraries
import os
import sys
from pydub import AudioSegment

#Assignign directory from parameters
wav_directory = sys.argv[1]
mp3_directory = sys.argv[2]

#Confirming WAV directory
response1 = input("You've selected " + wav_directory + " as the wav directory. Are you sure? (y/n) ")
match response1:
    #Acting in the different cases
    case "y":
        print('Wav Directory set up successfully')
    case "Y":
        print('Wav Directory set up successfully')
    case "s":
        print("Wav Directory set up successfully")
    case "S":
        print("Wav Directory set up successfully")
    #If its not the wanted directory ask for it again
    case _:
        wav_directory = input("Insert the wav directory: ")

#Confirming output directory
response2 = input("You've selected " + mp3_directory + " as the output directory. Are you sure? (y/n) ")
match response2:
    #Acting in different cases
    case "y": 
        print("Output directory set up successfully")
    case "Y":
        print("Output directory set up successfully")
    case "s":
        print("Output directory set up successfully")
    case "S":
        print("Output directory set up successfully")
    #if its not the wanted outut directory ask for it again
    case _:
        mp3_directory = input("Insert the output directory: ")

#Recovering file list (ls)
files = os.listdir(wav_directory)

#loop to pass through all the files
for file in files:

    #Creating the directory of the input file
    file_in = wav_directory + "/" + file

    #Creating the file name for the converted one
    fileName = file.replace('.wav', '.mp3')

    #Creating the directory string for the output file
    file_out = mp3_directory + "/" + fileName
    
    print("Converting", file, "to MP3...")
    #Opening and converting the file
    AudioSegment.from_wav(file_in).export(file_out, format="mp3")
    print("The file has been saved in the following directory", file_out)
    



    