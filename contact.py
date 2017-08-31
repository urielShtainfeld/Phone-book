#uriel shtainfeld 200956795
class Contact(object):
	"""docstring for Contact"""
	def __init__(self,name,cellphone,olderContact = None):
		if olderContact != None:	
				olderContact.name = name
				if cellphone != "" :
					olderContact.cellphone = cellphone
				self = olderContact	
		else:
				self.name = name
				if cellphone != "" :
    					self.cellphone = cellphone

	def __lt__(ContactB):
		if len(self.getName())<len(ContactB.getName):
				minLen = len(self.getName())
		else:
				minLen = len(ContactB.getName())		
		for i in range(0,minLen):	
			if 	ord(self.getName()[i]) < ord(contactB.getName()[i]):
				return True
			elif ord(self.getName()[i]) < ord(contactB.getName()[i]):
				return False
		if len(self.getName())<len(ContactB.getName):
			return True		
		return False	
	def getName():
		return(self.name)
	def getCellphone():
		return(self.cellphone)
	def __str__(self):
		return ("Name: %s \n cellphone: %s" % (self.name,self.cellphone))
	def	Match(key):
		if getName().find(key, beg=0, end=len(getName())) !=-1 :
    			return True
		if getCellphone().find(key, beg=0, end=len(getName())) !=-1 :
    			return True	
		return False
class FriendContact(Contact) :
			"""docstring for FriendContact"""
			def __init__(self,name,cellphone,homePhone,personalEmail,oldeFriendContact = None):
				if oldeFriendContact != None:					
					Contact(name,cellphone,oldeFriendContact)
					if homePhone != "" :
    						oldeFriendContact.homePhone = homePhone
					if personalEmail != "" :
						oldeFriendContact.personalEmail = personalEmail
					self = oldeFriendContact
				else:
						Contact(name,cellphone)
						if homePhone != "":
							self.homePhone = homePhone
						if personalEmail != "" :
							self.personalEmail = personalEmail
			def gethomePhone():
				return(self.homePhone)		
			def getpersonalEmail():
				return(self.personalEmail)

def __str__(self):
		return Contact.__str__() + ("\n home Phone: %s \n Personal Email: %s" % (self.homePhone,self.personalEmail))
def	Match(key):
		if Contact.Match(key) == True:
    			return True
		if gethomePhone().find(key, beg=0, end=len(getName())) !=-1 :
				return True
		if getpersonalEmail().find(key, beg=0, end=len(getName())) !=-1 :
				return True	
		return False
class ProfessionalContact(Contact):
	"""docstring for ClassName"""
	def __init__(self,name,cellphone,workPhone,workEmail,oldProffesionContact = None):
				if oldProffesionContact !=None :
						Contact(name,cellphone,oldProffesionContact)
						if workPhone != "" :
							oldProffesionContact.workPhone = workPhone
						if workEmail != "" :
							oldProffesionContact.workEmail = workEmail
						self = oldProffesionContact	
				else:										
						Contact(name,cellphone)
						if workPhone != "" :
							self.workPhone = workPhone
						if workEmail != "" :
							self.workEmail = workEmail
		
	def __str__(self):
		return Contact.__str__() + ("\n work Phone: %s \n work Email: %s" % (self.workPhone,self.workEmail))
	def getworkPhone():
    		return(self.workPhone)
	def getWorkEmail():
    		return(self.workEmail)		
	def	Match(key):
		if Contact.Match(key) == True:
				return True
		if getworkPhone().find(key, beg=0, end=len(getName())) !=-1 :
				return True
		if getWorkEmail().find(key, beg=0, end=len(getName())) !=-1 :
				return True	
		return False 	
class ProfessionalFriendContact(FriendContact,ProfessionalContact):
	def __init__(self,name,cellphone,homePhone,personalEmail,workPhone,workEmail,oldProfessionalFriendContact = None):
		FriendContact.__init__(self,name,cellphone,homePhone,personalEmail,oldProfessionalFriendContact = None)
		ProfessionalContact.__init__(self,name,cellphone,workPhone,workEmail,oldProfessionalFriendContact)
	def __str__(self):
		return FriendContact.__str__() + ProfessionalContact.__str__()
	def	Match(key):
		if FriendContact.Match(key) == True:
				return True
		if ProfessionalContact.Match(key) == True:
				return True
		return False 		