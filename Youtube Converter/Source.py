from Converters.MP3Converter import *;
from Tools.Utilities import *;
from Tools.YoutubeVideo import *;

def progress_callback(video, file_size, remaining):
        print('\r' + '{0} [%s%s]%.2f%%'.format(video.title) 
              % ('█' * int(remaining*20/file_size), ' '*(20-int(remaining*20/file_size)), float(remaining/file_size*100)), end='');
        pass;

def complete_callback(video, file_handle):
        print('\n'*2);
        print(file_handle);    
        pass;

while True:

    url = input('Enter video url:');
      
    print('\n');

    if (is_youtubeURL(url)):
        try:
            video = YoutubeVideo(url, progress_callback, complete_callback);                    
            video_path = video.download();  
            
            if (video_path != None):
                mp3converter = MP3Converter();
                mp3converter.convert(video_path, video.title);
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