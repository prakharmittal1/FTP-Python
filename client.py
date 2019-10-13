import ftplib
import sys
import os
import getpass

while True:

	print("\nEnter Server Details:          \n")
	option=str(input())
	y=option.split(" ")

	if option=='quit':
			break
			exit()

	elif y[0]=='ftpclient':
		while True:

			ftpIP=y[1]
			if ftpIP != '172.16.105.58':
				print("Invalid Port Address \n")
				print("\nEnter Server Details:          \n")
				option1=str(input())
				y=option.split(" ")
			else:
				break
		ftp = ftplib.FTP()
		ftp.connect(ftpIP,21)
		
		while True:
			Username=input("Username: ")
			Password=getpass.getpass()
			if (Username != 'prakhar' or Password != 'mittal'):
				print("Invalid Username or Password \n")
			else:
				break
		ftp.login(Username, Password)
		print("\nConnected to Server Successfully ! \n ")

	else:
			print("Invalid Command, Please try again \n")
			continue

	while True:

		selector=str(input())
		x=selector.split(" ")
		if selector=='quit':
			break
			exit()

		elif selector=='dir':
			data = []
			ftp.dir(data.append)
			for line in data:
				print(line)
			print("END OF LIST \n")

		elif x[0]=='upload':
			filenameup=x[1]
			def upload(ftp, filenameup):
				try:
					ext = os.path.splitext(filenameup)[1]
					ftp.storbinary("STOR " + filenameup, open(filenameup, "rb"), 1024)
				except:
					print("Error")
					return
			upload(ftp, filenameup)
			print(filenameup,"\n")

		elif x[0]=='get':
			filename = x[1]
			def getFile(ftp, filename):
				try:
					ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
				except:
					print("Error")
					return
			ftp.cwd('')
			getFile(ftp,filename)
			print(filename,"\n")

		else:
			print("Invalid Command, Please try again \n")
			continue

	ftp.quit()		
ftp.quit()