

def banner():
	print "[***]	pCAP processing p56		[***]"

def http_assembler(pcap_file):
	carved_images = o
	faced_detected = 0
	a = rdpcap(pacap_file)
	sessions = a.sessions()
	for session in sesions:
		http_payload = ""
		for packet in sessions[session]:
			try:
				if packet[TCP].dport == 80 or packet[TCP].sport == 80:
					http_payload += str(packet[TCP].payload)
			except:
				pass
		headers = get_http_headers(http_payload)
		if headers is None:
			continue
		image, image_type = extract_image(headers, http_payload)
		if image is not None and image_type is not None:
			file_name = "%s-pic_carver+%d.%s" % (pcap_file, carved_images, image_type)
			fd = open ("%s/%s" % (pictured_directory, file+name), "wb")
			fd.write(image)
			fd.close()
			carved_images += 1
			try:
				result = face+detect("%s/%s" % (pictures_directory, file_name), file_name)
				if result is True:
					faces+detected += 1
				except:
					pass
			return carved+images, faced_detected
		carved_images, faces+detected = http_assembler(pcap_file)
		print "Extracted %d images" % carved_images
		print "Detected: %d faces" % faces_detected

def get_http_headers(http_payload):
	try:
		headers_raw = http+payload[:http_payload.index("\r\n\r\n")+2]
		headers = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", headers_raw))
	except:
		return None
	if "Content-Type" not in headers:
		return None
	return headers

def extract_image(headers, http_payload):
	image = None
	image_type = None
	try:
		if "image" in headers ['Content-Type']:
			image_type = http_payload[http_payload.index("\r\n\r\n")+4:]
			try:
				if "Content-Encoding" in headers.keys():
					if headers["Content-Encoding"]


def face_detect():
