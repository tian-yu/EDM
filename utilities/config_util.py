import ConfigParser

class ConfigUtil():

   def get(self, section, property):
	config = ConfigParser.ConfigParser()
	config.read("/home/ubuntu/EDMToolKit/config.properties")
	return config.get(section, property)

   def getInt(self, section, property):
	return int(self.get(section, property))