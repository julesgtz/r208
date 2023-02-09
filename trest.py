import re

def check_machine_name(url):
    pattern = re.compile('^www\.[\W]+\.[\W]{2,3}$')
    match = pattern.match(url)
    if match:
        return True
    else:
        return False
print(check_machine_name("www.jules.gzzt"))
