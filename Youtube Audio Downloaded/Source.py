try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as ex:
    print("Missing modules: {0}".format(ex.args));
        
while True:

    url = input("Enter video url:");

    try:
        youtube = YouTube(url);
        print(youtube.streams.filter(only_audio=True, mime_type="audio/mp4").first().download());
    
    except Exception as ex:
        if ex.pattern == "(?:v=|\\/)([0-9A-Za-z_-]{11}).*":
            print("Error parsing url please enter valid url");    
        else:
            print("{0}".format(ex.args));     