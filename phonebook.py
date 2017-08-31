#uriel shtainfeld 200956795
import sys
import contact

contactBook = []
def main():
    	Start()	
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
			#try:
			if not CheckNumber(answer)  :
					print("That's not an number!")
					Start()
					pass
			else:
				numAnswer = int(answer)			
			if numAnswer == 1:
				insertNewContact()
			elif numAnswer ==2:
				printAllContacts()
			elif numAnswer ==3:
				replaceContact()
			elif numAnswer ==4:
				searchContact()
			elif numAnswer ==5:
				deleteContact()	
			elif numAnswer ==6:
				sys.exit();		
	pass
			
def insertNewContact():	
	letterAnswer = input("Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)?")
	if letterAnswer not in["S","F","P","B"]:
			print('Insert S or F or P or B only')  
			insertNewContact()	
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
	SortArray()	
	pass					
def printAllContacts():
	for x in range(0,len(contactBook)):	
		 print("%s %s" % (x+1,contactBook[x-1].__str__()))	
	pass
def replaceContact():
	answer = input("Enter a valid number of the contact you wish to edit:")
	if not CheckNumber(answer) :
		print("That's not an number!")
		replaceContact()
		pass
	else:
		numAnswer = int(answer)
	if numAnswer >= len(contactBook)+1:
		print("that's not a valid number")
		replaceContact()
		pass
	
	letterAnswer = input("Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)?")
	while letterAnswer not in["S","F","P","B"]:
		print('Insert S or F or P or B only')	
		letterAnswer = input("Should this contact be Simple (S), Friend (F), Professional (P) or Both (B)?")
	print("For the following fields click enter if there's no change, a new value if you want to replace the field,"
			"or x if you want to delete the field (the name field cannot be deleted).")
	if letterAnswer == "S":
		replaceSimpleContact(contactBook[numAnswer-1])
	elif letterAnswer == "F":
		replaceFriendContact(contactBook[numAnswer-1])		
	elif letterAnswer == "P":
		replaceProfessional(contactBook[numAnswer-1])
	elif letterAnswer == "B":
		replaceProffesionalFriendContact(contactBook[numAnswer-1])	
	SortArray()			
	pass
				
def searchContact():
		key = input("Type contact details (name, phone, email):")
		for x in range(0,len(contactBook)):	
			if contactBook[x].Match(key) == True:
				contactBook[x].__str__()
		pass	

def deleteContact():
	answer = input("Enter a valid number of the contact you wish to delete:")
	try:
		numAnswer = int(answer)
	except:	
		print("That's not an number!")
	if numAnswer >= len(contactBook)+1:
		print("that's not a valid number")
		deleteContact()
		pass
	contactBook.Delete(contactBook[numAnswer-1])
	pass

def insertContact():
	name = input("insert Name:")
	while not CheckName(name):
			print("the name must have a Value")
			name = input("insert Name:")	
	cellphone = input("insert cellphone:")
	while not CheckNumber(cellphone):
			print("the number must have only digit")
			cellphone = input("insert cellphone:")
	contactBook.append(contact.Contact(name,cellphone))	
	pass

def insertFriendContact():	
	name = input("insert Name:")
	while not CheckName(name):
			print("the name must have a Value")
			name = input("insert Name:")	
	cellphone = input("insert cellphone:")
	while not CheckNumber(cellphone):
			print("the number must have only digit")
			cellphone = input("insert cellphone:")
	homePhone = input("insert home Phone:")
	while not CheckNumber(homePhone):
			print("the no must have only digit")
			homePhone = input("insert home Phone:")
	personalEmail = input("insert personal Email:")
	while (not CheckEmail(personalEmail)) or (personalEmail == ""):
			print("email must contain '.' and '@'")
			personalEmail = input("insert personal Email:")	
	contactBook.append(contact.FriendContact(name,cellphone,homePhone,personalEmail))	
	pass
def insertProfessionalContact():
	name = input("insert Name:")
	while not CheckName(name):
			print("the name must have a Value")
			name = input("insert Name:")	
	cellphone = input("insert cellphone:")
	while not CheckNumber(cellphone):
			print("the number must have only digit")
			cellphone = input("insert cellphone:")
	workPhone = input("insert work Phone:")
	while not CheckNumber(workPhone):
				print("the number must have only digit")
				workPhone = input("insert work Phone:")
	workEmail = input("insert work Email:")
	while (not CheckEmail(workEmail)) or (workEmail == ""):
				print("email must contain '.' and '@'")
				workEmail = input("insert Work Email:")
	contactBook.append(contact.ProfessionalContact(name,cellphone,workPhone,workEmail))
	pass
def insertProfessionalFriendContact():
	name = input("insert Name:")
	while not CheckName(name):
			print("the name must have a Value")
			name = input("insert Name:")	
	cellphone = input("insert cellphone:")
	while not CheckNumber(cellphone):
			print("the number must have only digit")
			cellphone = input("insert cellphone:")
	homePhone = input("insert home Phone:")
	while not CheckNumber(homePhone):
			print("the number must have only digit")
			homePhone = input("insert home Phone:")
	personalEmail = input("insert personal Email:")
	while (not CheckEmail(personalEmail)) or (personalEmail == ""):
			print("email must contain '.' and '@'")
			personalEmail = input("insert personal Email:")
	workPhone = input("insert work Phone:")
	while not CheckNumber(workPhone):
				print("the number must have only digit")
				workPhone = input("insert work Phone:")
	workEmail = input("insert work Email:")
	while (not CheckEmail(workEmail)) or (workEmail == ""):
				print("email must contain '.' and '@'")
				personalEmail = input("insert Work Email:")	
	contactBook.append(contact.ProfessionalFriendContact(name,cellphone,homePhone,personalEmail,workPhone,workEmail))			
	pass


def replaceSimpleContact(ReplacedContact):
	name = input("name: (%s)") % ReplacedContact.getName()
	while not CheckName(name):
			print("the name must have a Value")
			name = input("name: (%s)") % ReplacedContact.getName()
	cellphone = input("cellphone: (%s)") % ReplacedContact.getCellphone()
	while not CheckNumber(cellphone):
			if cellphone != 'x':
				print("the number must have only digit")
				cellphone = input("cellphone: (%s)") % ReplacedContact.getCellphone()
			else:
    				cellphone = ""
	contact(name,cellphone,ReplacedContact)	
	pass
def replaceFriendContact(ReplacedContact):
	name = input("name: ( %s )") % ReplacedContact.getName()
	while not CheckName(name):
			print("the name must have a Value")
			name = input(("name: ( %s )") % ReplacedContact.getName())
	cellphone = input("cellphone: (%s)") % ReplacedContact.getCellphone()
	while not CheckNumber(cellphone):
			if cellphone != 'x':
				print("the number must have only digit")
				cellphone = input("cellphone: (%s)") % ReplacedContact.getCellphone()
			else:
    				cellphone = ""	
	homePhone = input("home phone: (%s)") % ReplacedContact.gethomePhone()
	while not CheckNumber(homePhone):
			if homePhone !="x":
				print("the number must have only digit")
				homePhone = input("home phone: (%s)") % ReplacedContact.gethomePhone()
			else:
				homePhone = ""					
	personalEmail = input("personal Email (%s):") % ReplacedContact.getpersonalEmail()
	while (not CheckEmail(personalEmail)) or (personalEmail == ""):
			if personalEmail != "x":
				print("email must contain '.' and '@'")
				personalEmail = input("personal Email (%s):") % ReplacedContact.getpersonalEmail()
			else:
				personalEmail = ""
	FriendContact(name,cellphone,homePhone,personalEmail,ReplacedContact)		
	pass		
def replaceProfessional(ReplacedContact):
	name = input("name: (%s)") % ReplacedContact.getName()
	while not CheckName(name):
			print("the name must have a Value")
			name = input("name: (%s)") % ReplacedContact.getName()
	while not CheckNumber(cellphone):
			if cellphone != 'x':
				print("the number must have only digit")
				cellphone = input("cellphone: (%s)") % ReplacedContact.getCellphone()
			else:
    				cellphone = ""
	workPhone = input("Work phone: (%s)") % ReplacedContact.getworkPhone()
	while not CheckNumber(workPhone):
			if workPhone != "x":
				print("the number must have only digit")
				workPhone = input("Work phone: (%s)") % ReplacedContact.getworkPhone()	
			else:
				workPhone = ""			
	workEmail = input("Work Email (%s):") % ReplacedContact.getWorkEmail()
	while (not CheckEmail(personalEmail)) or (personalEmail == ""):
			if workEmail != "x":
				print("email must contain '.' and '@'")
				workEmail = input("Work Email (%s):") % ReplacedContact.getWorkEmail()
			else:
				workEmail = ""
	ProfessionalContact(name,cellphone,workPhone,workEmail,ReplacedContact)		
	pass
def replaceProffesionalFriendContact(ReplacedContact):
	name = input("name: (%s)") % ReplacedContact.getName()
	while not CheckName(name):
			print("the name must have a Value")
			name = input("name: (%s)") % ReplacedContact.getName()
	cellphone = input("cellphone: (%s)") % ReplacedContact.getCellphone()
	while not CheckNumber(cellphone):
			if cellphone != 'x':
				print("the number must have only digit")
				cellphone = input("cellphone: (%s)") % ReplacedContact.getCellphone()
			else:
    				cellphone = ""	
	homePhone = input("home phone: (%s)") % ReplacedContact.gethomePhone()
	while not CheckNumber(homePhone):
			if homePhone !="x":
				print("the number must have only digit")
				homePhone = input("home phone: (%s)") % ReplacedContact.gethomePhone()
			else:
				homePhone = ""					
	personalEmail = input("personal Email (%s):") % ReplacedContact.getpersonalEmail()
	while (not CheckEmail(personalEmail)) or (personalEmail == ""):
			if personalEmail != "x":
				print("email must contain '.' and '@'")
				personalEmail = input("personal Email (%s):") % ReplacedContact.getpersonalEmail()
			else:
				personalEmail = ""
	workPhone = input("Work phone: (%s)") % ReplacedContact.getworkPhone()
	while not CheckNumber(workPhone):
			if workPhone != "x":
				print("the number must have only digit")
				workPhone = input("Work phone: (%s)") % ReplacedContact.getworkPhone()	
			else:
				workPhone = ""			
	workEmail = input("Work Email (%s):") % ReplacedContact.getWorkEmail()
	while (not CheckEmail(personalEmail)) or (personalEmail == ""):
			if workEmail != "x":
				print("email must contain '.' and '@'")
				workEmail = input("Work Email (%s):") % ReplacedContact.getWorkEmail()
			else:
				workEmail = ""
	ProfessionalFriendContact(name,cellphone,homePhone,personalEmail,workPhone,workEmail,ReplacedContact)
	pass

def SortArray():
		for i in range(len(contactBook)):
			for j in range(len(contactBook)-1-i):
					if contactBook[j].__lt__(contactBook[j+1]):		
						contactBook[j], contactBook[j+1] = contactBook[j+1], contactBook[j]	
def CheckName(NameStr):
			if NameStr == "":
				return False
			return True

def CheckNumber(phoneNo): 
	if str.isdigit(phoneNo) or phoneNo == "":
    		return True
	return False	 

def CheckEmail(email):
	if str.__contains__('@') and str.__contains__('.'):
		return True
	return False  

if __name__ == '__main__':
    main()