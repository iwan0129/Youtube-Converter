import os;
from Converters.MP3Converter import *;
from Tools.Utilities import *;
from Tools.YoutubeVideo import *;

def progress_callback(video, file_size, remaining):
    print('\r{0} [%s%s]%.2f%%'.format(video.title) % ('█' * int(remaining * 20 / file_size), ' ' * (20 - int(remaining * 20 / file_size)),  float(remaining / file_size * 100)), end='');
pass;

def complete_callback(video, file_handle):
    print('\n\n\n{0}'.format(file_handle));              
pass;

while True:
    url = input('Enter video url:');
      
    print('\n');

    if (is_youtubeURL(url)):
        try:
            video = YoutubeVideo(url, progress_callback, complete_callback);

            if contains_invalid_chars(video.title):
                video.title = format_title(video.title);
            pass;              

            video_path = video.download(progressive = True, order_by = 'abr');  
            
            if (video_path != None):
                mp3converter = MP3Converter();
                mp3converter.convert(video_path, video.title);
                os.unlink(video_path);
            else:
                print('Unable to download video due to youtube protection.\nPlease try with other video.');

        except Exception as ex:
            print(ex.args);
        pass;
    else:
        print('\nError! Please enter valid youtube url');

    print('\n\n\n');
pass;