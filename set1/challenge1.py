import base64

def hextobase64(inp):
	try:
		assert type(inp) is str
	except AssertionError:
		print('The argument must be of type string (str)!')
		raise

	return base64.b64encode(bytes.fromhex(inp)).hex()
	