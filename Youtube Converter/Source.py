from Converters.MP3Converter import *;
from Tools.Utilities import *;

while True:

    url = input('Enter video url:');
      
    print('\n');

    if (is_youtubeURL(url)):
            mp3converter = MP3Converter(url);
            mp3converter.convert();
    else:
        print('\nError! Please enter valid youtube url');

    print('\n' * 2);
