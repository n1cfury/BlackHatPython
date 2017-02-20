from Crypto.PublicKey import RSA
#The functions are fluff.  The original program is commented out"
'''
new_key = RSA.generate(2048, e=65537)
public_key = new_key.publickey().exportKey("PEM")
private_key = new_key.exportKey("PEM")
'''
def banner():
	print "[***]	Key Generator p133	[***]"
	print ""

def main():
	new_key = RSA.generate(2048, e=65537)
	print "[*] Generating Public Key..."
	public_key = new_key.publickey().exportKey("PEM")
	print "[*] Generating Private Key..."
	private_key = new_key.exportKey("PEM")

if __name__ == '__main__':
	main()