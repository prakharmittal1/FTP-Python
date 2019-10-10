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
	print("\nChoose Option :   \n")
	selector=int(input("1. List the files on the Server \n2. Upload a file to the server \n3. Download a file from the server \n4. Quit \n\nEnter your choice : "))
	if selector==4:
		break
		exit()

	elif selector==1:
		data = []
		ftp.dir(data.append)
		for line in data:
			print("-", line)
		print("List of Files displayed successfully. ")

	elif selector==2:
		filenameup=input("Enter the Name of the file you want to Upload : ")
		def upload(ftp, filenameup):
			ext = os.path.splitext(filenameup)[1]
			ftp.storbinary("STOR " + filenameup, open(filenameup, "rb"), 1024)
		upload(ftp, filenameup)
		print(filenameup," : Uploaded successfully... ")


	elif selector==3:
		filename=input("Enter the Name of the file you want to Download : ")
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