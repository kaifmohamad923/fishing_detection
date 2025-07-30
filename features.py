import re
import urllib.parse

def has_ip(url):
    ip_pattern = r'http[s]?://(?:\d{1,3}\.){3}\d{1,3}'
    return int(bool(re.search(ip_pattern, url)))

def has_at_symbol(url):
    return int('@' in url)

def count_dots(url):
    return url.count('.')

def uses_https(url):
    return int(url.lower().startswith('https'))

def url_length(url):
    return len(url)

def suspicious_words(url):
    words = ['login', 'verify', 'secure', 'account', 'update', 'signin', 'sighnup']
    return int(any(word in url.lower() for word in words))

def extract_features(url):
    return [
        url_length(url),
        count_dots(url),
        has_ip(url),
        has_at_symbol(url),
        uses_https(url),
        suspicious_words(url)
    ]