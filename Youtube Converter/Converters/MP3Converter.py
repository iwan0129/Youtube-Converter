try:
    import re;
    import os;
    from pytube import YouTube;
    from pytube import Playlist;
    from moviepy.editor import *;
except Exception as ex:
        print('Missing modules: {0}'.format(ex.args));

class MP3Converter:

    def __init__(self, url):
        self.url = url;

    def progress_callback(self, stream = None, chunk = None, file_handle = None, bytes_remaining = None):
        file_size = stream.filesize;
        remaining = file_size - file_handle;
        print('\r' + '{0} [%s%s]%.2f%%'.format(stream.title) 
              % ('█' * int(remaining*20/file_size), ' '*(20-int(remaining*20/file_size)), float(remaining/file_size*100)), end='')

    def complete_callback(self, stream, file_handle):
        print('\n'*2);
        print(file_handle);
    

    def make_mp3(self, video_path, mp3_name):
        print('\n'*2);
        video = VideoFileClip(video_path);
        video.audio.write_audiofile('{0}.mp3'.format(mp3_name));
        video.close();
    
    def convert(self):
        try:
            youtube = YouTube(self.url, on_progress_callback=self.progress_callback, on_complete_callback=self.complete_callback);          
            video_path = youtube.streams.filter().first().download();
            self.make_mp3(video_path, youtube.title);
            os.unlink(video_path);
        except Exception as ex:
            print(ex.args);