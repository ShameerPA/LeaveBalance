import urllib3

def check_url():
    import urllib3
    http = urllib3.PoolManager()
    try:
        r = http.request('GET', 'www.google.co.in')
        return True
    except:
        return False