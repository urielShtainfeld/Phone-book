#uriel shtainfeld 200956795
class Contact(object):
	"""docstring for Contact"""
	def __init__(self,name,cellphone,olderContact = None):
		olderContact.name = name
		if cellphone != None :
			olderContact.cellphone = cellphone
		self = olderContact	
	def __lt__():
		print("uriel")
	def __str__():
		return "Name: %s \n cellphone: %s" % (self.name,self.cellphone)
	def	Match(subString):
		print("uriel")
class FriendContact(Contact) :
			"""docstring for FriendContact"""
			def __init__(self,name,cellphone,homePhone,personalEmail,oldeFriendContact = None):
				Contact.__init__(self,name,cellphone ,oldeFriendContact)
				if homePhone != None :
					oldeFriendContact.homePhone = homePhone
				if personalEmail != None :
					oldeFriendContact.personalEmail = personalEmail
				self = oldeFriendContact

def __str__():
		return Contact.__str__ + "\n home Phone: %s \n Personal Email: %s" % (self.homePhone,self.personalEmail)

class ProfessionalContact(Contact):
	"""docstring for ClassName"""
	def __init__(self,name,cellphone,workPhone,workEmail):
				Contact.__init__(self,name,cellphone)
				if workPhone != None :
					self.workPhone = workPhone
				if workEmail != None :
					self.workEmail = workEmail
		
def __str__():
		return Contact.__str__ + "\n work Phone: %s \n work Email: %s" % (self.workPhone,self.workEmail)
		
	 	
class ProfessionalFriendContact(FriendContact,ProfessionalContact):
	def __init__(self,name,cellphone,homePhone,personalEmail,workPhone,workEmail,oldProfessionalFriendContact = None):
		FriendContact.__init__(self,name,cellphone,homePhone,personalEmail,oldProfessionalFriendContact = None)
		ProfessionalContact.__init__(self,name,cellphone,workPhone,workEmail,oldProfessionalFriendContact)
	def __str__():
		return FriendContact.__str__ + ProfessionalContact.__str__
			