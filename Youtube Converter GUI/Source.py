from Converters.MP3Converter import *;
from Tools.Utilities import *;
from Tools.YoutubeVideo import *;
from threading import Thread;

import time;
import PySimpleGUI as sg;

sg.theme('dark grey 9');

layout = [[sg.Text('                             Youtube Url', font='Courier, 16')],
          [sg.Input(size=(42, 1), key='Url', font='Courier, 14')],
          [sg.ProgressBar(1, orientation='h', size=(42, 20), key='Progress')],
          [sg.Multiline(size=(50, 10), key='Output', font='Courier, 12', background_color='white', text_color='black')],
          [sg.Button(size=(42, 1), button_text='Convert', font='Courier, 14', key='Convert')]];

window = sg.Window('Youtube Converter', layout);

download_notified = False;
downloading = False;

def progress_callback(video, file_size, remaining):
    global download_notified;

    downloaded = float(remaining/file_size*100);
    progress_bar = window['Progress'];
    progress_bar.UpdateBar(downloaded, 100);
    
    if not download_notified:
        textbox = window['Output'];
        textbox.update('Downloading {0}'.format(video.title));
        download_notified = True;
        pass;

    if downloaded == 100:
        download_notified = False;
        pass;
pass;

def complete_callback(video, file_handle):
    textbox = window['Output'];
    textbox.update(textbox.get() + '\nWriting Audio File...\n');
pass;

def complete_audiofile(path):
    global downloading;

    textbox = window['Output'];
    progress_bar = window['Progress'];
    textbox.update(textbox.get() + '{0}\n\nDone.\n'.format(path));
    progress_bar.UpdateBar(0, 100);

    downloading = False;
pass;

def download_video(url):
    try:
        video = YoutubeVideo(url, progress_callback, complete_callback);

        if contains_invalid_chars(video.title):
            video.title = format_title(video.title);
            pass;

        video_path = video.download();

        if (video_path != None):
            mp3_converter = MP3Converter(complete_audiofile);
            mp3_converter.convert(video_path, video.title);
            os.unlink(video_path);
            pass;
    except Exception as ex:
        print(ex.args);
        pass;
pass;           

while True:
    event, values = window.read();

    if event == 'Convert' and is_youtubeURL(values['Url']) and not downloading:
        Thread(target = download_video, args=(values['Url'],), daemon=True).start();
        downloading = True;
        pass;
    elif event == sg.WINDOW_CLOSED:
        window.close();
        break;     
pass;