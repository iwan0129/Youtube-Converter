import re

try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as ex:
    print("Missing modules: {0}".format(ex.args));
        
def is_youtubeURL(str):
   return re.findall('http[s]?://www.youtube.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)

while True:

    url = input("Enter video url:");

    if (is_youtubeURL(url)):
        try:

            print(YouTube(url).streams.filter(only_audio=True, mime_type="audio/mp4").first().download());

        except Exception as ex:
            print("{0}".format(ex.args));       
    else:
        print("Please enter valid youtube url");