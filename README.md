# MMSAlert
Send MMS alert messages to provide feedback on program execution

README

Part I: Init

	When using an MMSAlert object for the first time, you may be prompted for 
	a set of specific information to connect to an email account. Before
	entering this data, you will need to allow your email account to be 
	accessed by less secure apps. For our purposes, I recommend the 
	creation of a dummy Gmail account that exists for the sole purpose of
	communicating with the MMSAlert object.

	Step 1:
		Less secue app access
		- can be found in the Google Account Security tab. Enable to
		  allow SMTP to access your Gmail

	Step 2:
		Enter your Email Address

	Step 3:
		Enter your Email password

	Step 4:
		Enter your phone number, followed by your MMS Gateway code
		- This unique to your cell phone provider, and can ve found 
		  online
		- Ex: AT&T = mms.att.net

	Step 5:
		Enter your Email's SMTP address
		- This is unique for each email provider, and can be found online
		- Ex: Gmail's = smtp.gmail.com

	Step 6:
		Enter your Email accounts SMTP Port Number
		- This is unqiue for each email provider, and can be found online
		- Ex: Gmail has 3: 25, 465, or 587
		- Try each until one works

Part II: MMSAlert User Methods

	MMSAlert.init()
	- prompts users for personal data to establish a connection to a 
	  personal email account. Stores data locally in the form of a
	  CONFIG file. Runs automatically if no CONFIG file is detected
	  in local dir.

	MMSAlert.start()
	- Starts a server connection with your email account, using data
	  stored in a local config file

	MMSAlert.stop()
	- Terminates the server connection with your email account

	MMSAlert.sent_message(message, subject=None)
	- takes in a message as a string and an optional subject line 
	  as a string. Leave subject set to none to send no subject line

Part III: Notify Functions

	ErrorNotify(error, writelog=True, errorlog='ErrorLog.txt')
	- takes in a error message as a string, writelog request as a
	  bool, and textfile for writing errors to as a filename 
	- if writelog == True, logs error message to a local errorfile 
	- sends MMS message to set phone number with Subject='Error'
	  and Body=error 

	TerminateNotify(sendlog=True)
	- takes in writelog request as a bool
	- if sendlog == True, pulls available output logs and prepares
	  them as a single string. Concats to end of termination notice.
	- sends MMS message to set phone number with Subject='Terminate Program'
	  and Body=termination_notice + output_logs
	
