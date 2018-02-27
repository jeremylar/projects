import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
filename = 'userlist.csv' #csv list with old email,username/new email, password


office365user = 'user@email.com'# office 365 user account sending emails from
office365userpw = '' #password for office 365 account
subject = 'Email Migration to Office365'

with open(filename, 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		sendto = row[0]  # send to first column item in csv
		
		body = """User Company Staff: \n
		\n
On Thursday, 2/1/2018 at 6:30pm, We will be starting the email migration for User Company Inc. We will be completing the migration of the employee's emails over the next few days. Until then, you can access your new email from the web portal below. Old email will be migrated over the next few days. \n
Web Address: https://portal.office.com 
Username:""" + row[1] +"""
Password: """+ row[2] +"""
You will still be able to receive emails from your old User Company email address. \n
How to Setup Office 365 on Mobile Devices
How to Install Office 365 Email on an iPhone:
https://support.office.com/en-us/article/set-up-email-using-the-ios-mail-app-7e5b180f-bc8f-45cc-8da1-5cefc1e633d1 \n
How to Install Office365 Email on an Android Device:
https://support.office.com/en-us/article/set-up-email-in-android-email-app-71147974-7aca-491b-978a-ab15e360434c?ui=en-US&rs=en-US&ad=US
\n
If you are having any issues, you can give us a call at 516-403-9001 Option 2 \n
Thanks, \n
Support Tech Team"""
		#Email functions
		mailserver = smtplib.SMTP('smtp.office365.com',587)
		msg = MIMEMultipart()
		msg['From'] = office365user
		msg['To'] = sendto
		msg['Subject'] = subject 
		text = body
		part1 = MIMEText(text, 'plain')
		msg.attach(part1)
		mailserver.ehlo()
		# secure our email with tls encryption
		mailserver.starttls()
		# re-identify ourselves as an encrypted connection
		mailserver.login(office365user, office365userpw)
		mailserver.sendmail(office365user,sendto,msg.as_string())
		mailserver.quit()
		print("Sent Email to "+ row[0]+" with new email address "+row[1]+" and password "+row[2]) 
