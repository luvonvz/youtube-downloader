from pytube import YouTube
import os

def clear():
   system = os.name
   if system == "nt":
      os.system("cls")
   if system == "posix":
      os.system("clear")
   return 

if not os.path.exists(f"{os.getcwd()}/Youtube Downloads"):
    os.mkdir(f"{os.getcwd()}/Youtube Downloads")
clear()
print('Welcome to Youtube Downloader, please enter a valid youtube video link.')
link = YouTube(input('> '))
print('Downloading video, please wait...')
link.streams.get_highest_resolution().download(output_path=f"{os.getcwd()}/Youtube Downloads")
os.startfile(f"{os.getcwd()}/Youtube Downloads")
input('Press ENTER to exit')


