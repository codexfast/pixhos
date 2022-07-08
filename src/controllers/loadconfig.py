import configparser

files = ['config.ini']

def configs () -> dict:
	config = configparser.ConfigParser()
	dataset = config.read(files)

	if (len(dataset)!=len(files)):
		raise IOError("Config files not found")

	return config