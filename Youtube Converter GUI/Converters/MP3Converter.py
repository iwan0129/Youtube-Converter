try:
    from pytube import YouTube;
    from pytube import Playlist;
    from Tools.Utilities import *;
    from moviepy.editor import *;
except Exception as ex:
        print('Missing modules: {0}'.format(ex.args));

class MP3Converter:

    def __init__(self, url, progress_callback = None, complete_callback = None, complete_audiofile = None):
        self.url = url;
        self.current_title = '';
        self.progress_callback = progress_callback;
        self.complete_callback = complete_callback;
        self.complete_audiofile = complete_audiofile;

    def make_mp3(self, video_path, mp3_name):
        print('\n'*2);
        video = VideoFileClip(video_path);
        video.audio.write_audiofile('{0}.mp3'.format(mp3_name), verbose=False, logger=None);
        video.close();
        mp3_path = os.path.dirname(video_path) + '\{0}.mp3'.format(mp3_name);
        self.complete_audiofile(mp3_path);
    
    def convert(self):
        try:
            youtube = YouTube(self.url, on_progress_callback=self.progress_callback, on_complete_callback=self.complete_callback);                    
            self.current_title = format_title(youtube.title) if contains_invalid_chars(youtube.title) else youtube.title;
            video_stream = youtube.streams.filter().first();
            
            if (video_stream != None):
                video_path = video_stream.download(filename=self.current_title);
                self.make_mp3(video_path, self.current_title);
                self.current_title = '';
                os.unlink(video_path);
            else:
                print('Unable to download video due to youtube protection.\nPlease try with other video.');
                
        except Exception as ex:
            print(ex.args);
            pass;