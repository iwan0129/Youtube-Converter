from Converters.MP3Converter import *;

def is_youtubeURL(str):
   return re.findall('http[s]?://www.youtube.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
               
while True:

    url = input('Enter video url:');
      
    print('\n');

    if (is_youtubeURL(url)):
            mp3converter = MP3Converter(url);
            mp3converter.convert();
    else:
        print('\nError! Please enter valid youtube url');

    print('\n' * 2);
