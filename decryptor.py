import zlib, base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

private_key ="paste private key here"

def banner():
	print "[***]	Decryptor p134	[***]"

rsakey = RSA.importKey(private_key)
rsakey = PKCS1_OAEP.new(rsakey)
chunk_size = 256
offset = 0
decrypted = ""
encrypted = base64.b64decode(encrypted)

while offset < len(encrypted):
	decrpyted += rsakey.decrypt(encrypted([offset:offset+chunk_size])
	offset += chunk_size
plaintext = zlib.decompress(decrypted)
print plaintext