import ftplib
import sys
import os
import getpass

print("\nEnter Server Details:          \n")
ftp = ftplib.FTP(input("Enter IP:"))
Username=input("Username: ")
Password=getpass.getpass()
ftp.login(Username, Password)
print("\nConnected to Server Successfully !  ")


while True:
	print("\nChoose Option :  ")
	selector=str(input("dir \nupload\ndownload \nquit \n\n>> "))
	x=selector.split(" ")
	if selector=='quit':
		break
		exit()

	elif selector=='dir':
		data = []
		ftp.dir(data.append)
		for line in data:
			print("-", line)
		print("END OF LIST ")

	elif x[0]=='upload':
		filenameup=x[1]
		#input("Enter the Name of the file you want to Upload : ")
		def upload(ftp, filenameup):
			ext = os.path.splitext(filenameup)[1]
			ftp.storbinary("STOR " + filenameup, open(filenameup, "rb"), 1024)
		upload(ftp, filenameup)
		print(filenameup," : Uploaded successfully. ")


	elif x[0]=='download':
		filename = x[1]
		#filename=input("Enter the Name of the file you want to Download : ")
		def getFile(ftp, filename):
			try:
				ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
			except:
				print("Error")
		ftp.cwd('')
		getFile(ftp,filename)
		print(filename," : Downloaded successfully... ")


	else:
		print("Invalid Choice, Please choose again")
		continue


ftp.quit()