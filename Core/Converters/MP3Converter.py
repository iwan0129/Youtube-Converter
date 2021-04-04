try:
    from moviepy.editor import *;
except Exception as ex:
    print('Missing modules: {0}'.format(ex.args));      
pass;

class MP3Converter:

    def __init__(self, complete_audiofile = None):
        self.complete_audiofile = complete_audiofile;
    pass;

    def convert(self, video_path, mp3_name):
        print('\n'*2);
        video = VideoFileClip(video_path);
        video.audio.write_audiofile('{0}.mp3'.format(mp3_name));
        video.close();

        if self.complete_audiofile != None:
            mp3_path = os.path.dirname(video_path) + '\{0}.mp3'.format(mp3_name);
            self.complete_audiofile(mp3_path);
    pass;