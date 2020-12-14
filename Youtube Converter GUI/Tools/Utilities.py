import re;

allowed_chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$^&()_-+=,. ';

def is_youtubeURL(str):
   return re.findall('http[s]?://www.youtube.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)

def contains_invalid_chars(str):
    return [char for char in str if char not in allowed_chars] != None;

def format_title(title):
    return ''.join([char for char in title if char in allowed_chars]);