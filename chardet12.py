import urllib.request
from chardet.universaldetector import UniversalDetector

mygithub = urllib.request.urlopen('https://github.com/newtechnology12/')
detector = UniversalDetector()
for line in mygithub.readlines():
    detector.feed(line)
    if detector.done:
        break
detector.close()
mygithub.close()
print(detector.result)
