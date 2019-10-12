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
		ftpIP=y[1]
		#ftp = ftplib.FTP(input(ftpIP))
		ftp = ftplib.FTP()
		ftp.connect(ftpIP,21)
		#ftp=y[1]
		Username=input("Username: ")
		Password=getpass.getpass()
		ftp.login(Username, Password)
		print("\nConnected to Server Successfully ! \n ")

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
				ext = os.path.splitext(filenameup)[1]
				ftp.storbinary("STOR " + filenameup, open(filenameup, "rb"), 1024)
			upload(ftp, filenameup)
			print(filenameup," : Uploaded successfully. \n")

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
			print(filename," : Downloaded successfully. \n ")

		else:
			print("Invalid Command, Please choose again \n")
			continue

	ftp.quit()		

ftp.quit()