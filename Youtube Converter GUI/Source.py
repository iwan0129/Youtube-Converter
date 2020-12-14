from Converters.MP3Converter import *;
from Tools.Utilities import *;
from threading import Thread;

import time;
import PySimpleGUI as sg;
import win32gui;
import win32.lib.win32con as win32con;

win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_HIDE)

sg.theme('dark grey 9');

layout = [[sg.Text('                             Youtube Url', font='Courier, 16')],
          [sg.Input(size=(42, 1), key='-URL-', font='Courier, 14')],
          [sg.ProgressBar(1, orientation='h', size=(42, 20), key='progress')],
          [sg.Multiline(size=(50, 10), key='-OUTPUT-', font='Courier, 12', background_color='white', text_color='black')],
          [sg.Button(size=(42, 1), button_text='Convert', font='Courier, 14', key='Convert')]];

window = sg.Window('Youtube Converter', layout);

download_notified = False;

def progress_callback(stream = None, chunk = None, file_handle = None, bytes_remaining = None):
    global download_notified;

    file_size = stream.filesize;
    remaining = file_size - file_handle;
    downloaded = float(remaining/file_size*100);
    progress_bar = window['progress'];
    progress_bar.UpdateBar(downloaded, 100);
    
    if not download_notified:
        textbox = window['-OUTPUT-'];
        textbox.update('Downloading {0}'.format(mp3converter.current_title));
        download_notified = True;
        pass;

    if downloaded == 100:
        download_notified = False;
        pass;

def complete_callback(stream, file_handle):
    textbox = window['-OUTPUT-'];
    textbox.update(textbox.get() + '\nWriting Audio File...\n');

def complete_audiofile(path):
    textbox = window['-OUTPUT-'];
    textbox.update(textbox.get() + '{0}\n\nDone.\n'.format(path));
    progress_bar = window['progress'];
    progress_bar.UpdateBar(0, 100)

while True:
    event, values = window.read();

    if event == 'Convert':
        mp3converter = MP3Converter(values['-URL-'], progress_callback, complete_callback, complete_audiofile);
        Thread(target = mp3converter.convert, daemon=True).start();
        pass;

    elif event == sg.WINDOW_CLOSED:
        window.close();
        break;
        
        pass;