try:
    from pytube import YouTube;
    from pytube import Playlist;
except Exception as ex:
    print('Missing modules: {0}'.format(ex.args));
pass;
        

class YoutubeVideo:

    def __init__(self, url, progress_callback=None, complete_callback=None):
        self.youtube = YouTube(url, on_progress_callback=self.on_progress_callback, on_complete_callback=self.on_complete_callback);
        self.title = self.youtube.title;
        self.progress_callback = progress_callback;
        self.complete_callback = complete_callback;
    pass;

    def on_progress_callback(self, stream = None, chunk = None, file_handle = None, bytes_remaining = None):
        file_size = stream.filesize;
        remaining = file_size - file_handle;

        if self.progress_callback != None:
            self.progress_callback(self, file_size, remaining);
    pass;
    
    def on_complete_callback(self, stream, file_handle):
        if self.complete_callback != None:
            self.complete_callback(self, file_handle);
    pass;
       
    def download(self, subtype='mp4', progressive = False, only_audio = False, only_video = False, order_by = None):
        video_streams = self.youtube.streams.filter(subtype = subtype, progressive = progressive, only_audio = only_audio, only_video = only_video).desc();
        video_stream = video_streams.order_by(order_by).first() if order_by != None else video_streams.first();
        return video_stream.download() if video_stream != None else None;
    pass;