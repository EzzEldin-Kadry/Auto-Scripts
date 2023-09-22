import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2


#Only Change This
folder_path = 'E:\القراَن الكريم\عبدالرشيد صوفي - الدوري عن الكسائي' #Surahs
text_path = 'E:\القراَن الكريم\Quraan Surahs.txt' #Names 


lines = []
try:
    with open(text_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"The file '{text_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
try:
    files = os.listdir(folder_path)
    mp3_files = [f for f in files if f.endswith('.mp3')]
    cnt = 0
    for mp3_file in mp3_files:
        file_path = os.path.join(folder_path, mp3_file)
        audio = MP3(file_path) 
        tags = ID3()
        title = lines[cnt].strip()

        if "TIT2" in audio:
            audio["TIT2"].text[0] = title
            audio.update()
        else:
            tags["TIT2"] = TIT2(encoding=3, text=title)
            audio.update(tags)
            audio["TIT2"].text[0] = title

        cnt += 1
        audio.save()
    print('Task done successfully')

except FileNotFoundError:
    print(f"The folder '{folder_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")




