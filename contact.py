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

	def __lt__():
		print("uriel")
	def __str__(self):
		return ("Name: %s \n cellphone: %s" % (self.name,self.cellphone))
	def	Match(subString):
		print("uriel")
	def __repr__(self):
		return self.__str__(self)		
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
    						

def __str__(self):
		return Contact.__str__ + ("\n home Phone: %s \n Personal Email: %s" % (self.homePhone,self.personalEmail))

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
		return Contact.__str__ + ("\n work Phone: %s \n work Email: %s" % (self.workPhone,self.workEmail))
		
	 	
class ProfessionalFriendContact(FriendContact,ProfessionalContact):
	def __init__(self,name,cellphone,homePhone,personalEmail,workPhone,workEmail,oldProfessionalFriendContact = None):
		FriendContact.__init__(self,name,cellphone,homePhone,personalEmail,oldProfessionalFriendContact = None)
		ProfessionalContact.__init__(self,name,cellphone,workPhone,workEmail,oldProfessionalFriendContact)
	def __str__(self):
		return FriendContact.__str__ + ProfessionalContact.__str__
			