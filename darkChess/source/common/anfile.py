import sys

def hello():
	print "Hello World"

def decor_parseLine(func):
	def wrap_func(line, dic):
		if line == "":
			return 
		if line.startswith("#"):
			return
		return func(line, dic)
	return wrap_func

@decor_parseLine
def parseLine2Dic(line, dic):
	[key, value] = line.split("=", 1)
	dic[key] = value if dic.has_key(key) == False else (dic[key] + ("," + value))

def read_dcfg(f):
	dic = {}
	with open(f, "r") as fr:
		[parseLine2Dic(line.strip(), dic) for line in fr]
		
	return dic

def test_read_dcfg():
	print read_dcfg("chess.cfg")

def main():
	func = getattr(sys.modules[__name__], sys.argv[1])	
	func()

if __name__ == "__main__":
	main()
