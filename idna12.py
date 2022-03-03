import idna
idna.encode('ドメイン.テスト')
b'xn--eckwd4c7c.xn--zckzah'
print(idna.decode('xn--eckwd4c7c.xn--zckzah'))