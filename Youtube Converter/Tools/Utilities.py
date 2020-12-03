import re;

allowed_chars = 'qwertyuiopasdfghjklzxcvbnm0123456789!@#$^&()_-+=,.';
illegal_chars = '[:?*\/"<>|%]';

def is_youtubeURL(str):
   return re.findall('http[s]?://www.youtube.com/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)

def contains_invalid_chars(str):
    return 1 in [char in str for char in allowed_chars];

def format_title(title):
    return re.sub(illegal_chars, '', title);