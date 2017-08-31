#uriel shtainfeld 200956795
class Contact(object):
	"""docstring for Contact"""
	def __init__(self,name,cellphone,olderContact = None):
		if olderContact != None:	
				olderContact.name = name
				olderContact.cellphone = cellphone
				
				self.name = olderContact.name
				self.cellphone =olderContact.cellphone	
		else:
				self.name = name
				self.cellphone = cellphone

	def __lt__(self,other):
		if len(self.name)<len(other.name):
				minLen = len(self.name)
		else:
				minLen = len(other.name)		
		for i in range(0,minLen):	
			if 	ord(self.name[i]) < ord(other.name[i]):
				return True
			elif ord(self.name[i]) < ord(other.name[i]):
				return False
		if len(self.name)<len(other.name):
			return True		
		return False	
	def getName(self):
		return(self.name)
	def getCellphone(self):
		return(self.cellphone)
	def __str__(self):
		returnValue = "Name: %s \n "  % (self.name)
		if self.cellphone != "" :
			returnValue = returnValue + ("Cellphone %s \n" % (self.cellphone))
		return returnValue	
	def	Match(key):
		if self.getName().find(key, beg=0, end=len(self.getName())) !=-1 :
    			return True
		if getCellphone().find(key, beg=0, end=len(self.getName())) !=-1 :
    			return True	
		return False
class FriendContact(Contact) :
			"""docstring for FriendContact"""
			def __init__(self,name,cellphone,homePhone,personalEmail,oldeFriendContact = None):
				if oldeFriendContact != None:					
					Contact(name,cellphone,oldeFriendContact)
					oldeFriendContact.homePhone = homePhone
					oldeFriendContact.personalEmail = personalEmail
					self = oldeFriendContact
				else:
						Contact(name,cellphone)
						self.homePhone = homePhone
						self.personalEmail = personalEmail
			def gethomePhone(self):
				return(self.homePhone)		
			def getpersonalEmail(self):
				return(self.personalEmail)

def __str__(self):
		returnValue = Contact.__str__() 
		if self.home !='' :
		 	returnValue = returnValue +("\n home Phone: %s \n " % (self.homePhone))
		if self.personalEmail != '':
		  returnValue = returnValue + ("Personal Email: %s" % (self.personalEmail))
def	Match(key):
		if Contact.Match(key) == True:
    			return True
		if gethomePhone().find(key, beg=0, end=len(gethomePhone())) !=-1 :
				return True
		if getpersonalEmail().find(key, beg=0, end=len(getpersonalEmail())) !=-1 :
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
		returnValue = Contact.__str__() 
		if self.workPhone != "":
			returnValue = returnValue + (("\n work Phone: %s") % (self.workPhone))
		if self.workEmail != "":			
			returnValue = returnValue + ("\n work Email: %s" % (self.workEmail))
	def getworkPhone(self):
    		return(self.workPhone)
	def getWorkEmail(self):
    		return(self.workEmail)		
	def	Match(key):
		if Contact.Match(key) == True:
				return True
		if self.getworkPhone().find(key, beg=0, end=len(self.getworkPhone())) !=-1 :
				return True
		if self.getWorkEmail().find(key, beg=0, end=len(self.getWorkEmail())) !=-1 :
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