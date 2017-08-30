#uriel shtainfeld 200956795
import sys
import contact
contactBook = []
def CheckName(NameStr):
	if NameStr == "":
		return False
	return True
def CheckPhone(phoneNo): 
	if str.isdigit(phoneNo) or phoneNo == "":
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
			print("the number must have only digit")
			cellphone = input("insert cellphone:")
	contactBook.append(contact.Contact(name,cellphone))	
def insertFriendContact():	
	name = input("insert Name:")
	while not CheckName(name):
			print("the name must have a Value")
			name = input("insert Name:")	
	cellphone = input("insert cellphone:")
	while not CheckPhone(cellphone):
			print("the number must have only digit")
			cellphone = input("insert cellphone:")
	homePhone = input("insert home Phone:")
	while not CheckPhone(homePhone):
			print("the no must have only digit")
			homePhone = input("insert home Phone:")
	personalEmail = input("insert personal Email:")
	while (not CheckEmail(personalEmail)) or (personalEmail == None):
			print("email must contain '.' and '@'")
			personalEmail = input("insert personal Email:")	
	contactBook.append(contact.FriendContact(name,cellphone,homePhone,personalEmail))		
def insertProfessionalContact():
	name = input("insert Name:")
	while not CheckName(name):
			print("the name must have a Value")
			name = input("insert Name:")	
	cellphone = input("insert cellphone:")
	while not CheckPhone(cellphone):
			print("the number must have only digit")
			cellphone = input("insert cellphone:")
	workPhone = input("insert work Phone:")
	while not CheckPhone(workPhone):
				print("the number must have only digit")
				workPhone = input("insert work Phone:")
	workEmail = input("insert work Email:")
	while (not CheckEmail(workEmail)) or (workEmail == None):
				print("email must contain '.' and '@'")
				workEmail = input("insert Work Email:")
	contactBook.append(contact.ProfessionalContact(name,cellphone,workPhone,workEmail))			
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
def input2():
	for x in range(0,len(contactBook)):
   		 print("%d %s" % (x+1,contactBook.__repr__))						
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
				input2()
			elif numAnswer ==3:
				print("need to add function")
			elif numAnswer ==4:
				print("need to add function")
			elif numAnswer ==5:
				print("need to add function")	
			elif numAnswer ==6:
				sys.exit();		
	pass			
Start()			