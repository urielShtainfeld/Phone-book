#uriel shtainfeld 200956795
import sys
import contact
contactBook = []
def CheckName(Name):
	if name != None:
    		return True
	return False		
def CheckPhone(phoneNo): 
	if str.isdigit(phoneNo):
    		return True
	return False	 
def CheckEmail(email):
	if str.__contains__('@') and str.__contains__('.'):
		return True
	return False   	
def insertContact():
	name = input("insert Name:")
	while not CheckName(name):
			print("the name must have a Value")
			name = input("insert Name:")	
	cellphone = input("insert cellphone:")
	while not CheckPhone(cellphone):
			print("the no must have only digit")
			cellphone = input("insert cellphone:")
	contactBook.append(contact.Contact(name,cellphone))		
	#contact.Contact(name,cellphone)		
def insertFriendContact():	
	insertContact()
	homePhone = input("insert home Phone:")
	while not CheckPhone(homePhone):
			print("the no must have only digit")
			homePhone = input("insert home Phone:")
	personalEmail = input("insert personal Email:")
	while (not CheckEmail(personalEmail)) or (personalEmail == None):
			print("email must contain '.' and '@'")
			personalEmail = input("insert personal Email:")
def insertProfessionalContact():
	insertContact()
	workPhone = input("insert work Phone:")
	while not CheckPhone(workPhone):
				print("the number must have only digit")
				workPhone = input("insert work Phone:")
	workEmail = input("insert work Email:")
	while (not CheckEmail(workEmail)) or (workEmail == None):
				print("email must contain '.' and '@'")
				personalEmail = input("insert Work Email:")
def insertProfessionalFriendContact():
	name = input("insert Name:")
	while not CheckName(name):
			print("the name must have a Value")
			name = input("insert Name:")	
	cellphone = input("insert cellphone:")
	while not CheckPhone(cellphone):
			print("the no must have only digit")
			cellphone = input("insert cellphone:")
	homePhone = input("insert home Phone:")
	while not CheckPhone(homePhone):
			print("the no must have only digit")
			homePhone = input("insert home Phone:")
	personalEmail = input("insert personal Email:")
	while (not CheckEmail(personalEmail)) or (personalEmail == None):
			print("email must contain '.' and '@'")
			personalEmail = input("insert personal Email:")
	workPhone = input("insert work Phone:")
	while not CheckPhone(workPhone):
				print("the number must have only digit")
				workPhone = input("insert work Phone:")
	workEmail = input("insert work Email:")
	while (not CheckEmail(workEmail)) or (workEmail == None):
				print("email must contain '.' and '@'")
				personalEmail = input("insert Work Email:")				
def input1():	
	letterAnswer = input("Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)?")
	if letterAnswer not in["S","F","P","B"]:
			print('Insert S or F or P or B only')  
			input1()	
			pass
	else:
			if letterAnswer == "S":
    				insertContact()
			elif letterAnswer == "F":
    				insertFriendContact()		
			elif letterAnswer == "P":
    				insertProfessional()
			elif letterAnswer == "B":
        			insertProfessionalFriendContact()
			
					
def Start():
	answer = 0
	while   answer != 6:
			answer = input("What would you like to do? \n"
					"1 - Add a new contact \n"
					"2 - Show all contacts \n"
					"3 - Edit a contact \n"
					"4 - Find a contact \n"
					"5 - Delete a contact \n"
					"6 - Exit \n"
					"-->")
			try:
				numAnswer = int(answer)
			except:
				print("That's not an number!")
			if numAnswer == 1:
				input1()
			elif numAnswer ==2:
				print("1")
			elif numAnswer ==3:
				print("1")
			elif numAnswer ==4:
				print("1")
			elif numAnswer ==5:
				print("1")	
			elif numAnswer ==6:
				sys.exit();	

		#else
		#	print("you must enter number between 1 and 6")				
		#print 'you must enter number between 1 and 6'
			#print x	
			#If x < 1 And x > 6 then	
	pass			
Start()			