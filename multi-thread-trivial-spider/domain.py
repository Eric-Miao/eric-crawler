from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain_name(url):
    try:
        ret = get_sub_domain_name(url).split('.')
        return ret[-2] + '.' + ret[-1]
    except:
        return ''

# Get sub domain name (mail.exmaple.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
