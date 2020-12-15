from Converters.MP3Converter import *;
from Tools.Utilities import *;
from pytube import YouTube;
from pytube import Playlist;

def progress_callback(stream = None, chunk = None, file_handle = None, bytes_remaining = None):
        file_size = stream.filesize;
        remaining = file_size - file_handle;
        print('\r' + '{0} [%s%s]%.2f%%'.format(current_title) 
              % ('█' * int(remaining*20/file_size), ' '*(20-int(remaining*20/file_size)), float(remaining/file_size*100)), end='');
        pass;

def complete_callback(stream, file_handle):
        print('\n'*2);
        print(file_handle);    
        pass;

while True:

    url = input('Enter video url:');
      
    print('\n');

    if (is_youtubeURL(url)):
        try:
            youtube = YouTube(url, on_progress_callback=progress_callback, on_complete_callback=complete_callback);                    
            current_title = format_title(youtube.title) if contains_invalid_chars(youtube.title) else youtube.title;
            video_stream = youtube.streams.filter().first();
            
            if (video_stream != None):
                video_path = video_stream.download(filename=current_title);
                mp3converter = MP3Converter();
                mp3converter.convert(video_path, current_title);
                os.unlink(video_path);
                pass;
            else:
                print('Unable to download video due to youtube protection.\nPlease try with other video.');
                pass;               
        except Exception as ex:
            print(ex.args);
            pass;
        pass;
    else:
        print('\nError! Please enter valid youtube url');
        pass;

    print('\n' * 2);
    pass;