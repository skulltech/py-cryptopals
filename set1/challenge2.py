def fixedxor(inp1, inp2):
	try:
		assert type(inp1) is str
		assert type(inp2) is str
	except AssertionError:
		print('The argument must be of type string (str)!')
		raise

	return bytes(a ^ b for a, b in zip(bytes.fromhex(inp1), bytes.fromhex(inp2))).hex()
	