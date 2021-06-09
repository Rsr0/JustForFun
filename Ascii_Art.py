# pip install pywhatkit as kt

import pywhatkit as kt

print("ASCII...art!")

source_path = input("Enter the path of image: ")
target_path = 'ascii_art.text'

kt.image_to_ascii_art(source_path, target_path)

