from model.sqlite import BasePixhos

def set_config(prt_default: str, qrcode_size: int, qrcode_border: int):
	try:
		base = BasePixhos();
		base.update_config(prt_default, qrcode_size, qrcode_border)
		
		return True
	except:
		return False

def insert_config(prt_default: str, qrcode_size: int, qrcode_border: int):
	base = BasePixhos()
	base.insert_config()
	try:
		base = BasePixhos();	
		base.insert_config(prt_default, qrcode_size, qrcode_border)
		return True
	except:
		return False

def db_config():
	base = BasePixhos()

	return base.config