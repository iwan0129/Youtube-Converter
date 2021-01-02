import re;

allowed_chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$^&()_-+=,. ';
invalid_chars = '<>:"/\|?*';

def is_youtubeURL(str):
    return re.findall('http[s]?://www.youtube.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
pass;

def contains_invalid_chars(str):
    return [char for char in str if char not in allowed_chars] != None;
pass;

def format_title(title):
    return ''.join([char for char in title if char not in invalid_chars]);
pass;