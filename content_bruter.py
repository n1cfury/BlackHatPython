import urllib2, threading, Queue, urllib

threads = 50
target_url = "http://testphp.vulnweb.com"
wordlist_file = "/tmp/all.txt"		#from SVNDigger
resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/ 20100101 Firefox/19.0"

def banner():
	print "[***]   Directory Brute Force p67   [***]"

def build_wordlist(wordlist_file):
	fd - open(wordlist_file, "rb")
	raw_words = df.readlines()
	fd.close()
	found_resume = False
	words = Queue.Queue()
	for word in raw_words:
		word = word.rstrip()
		if resume is not None:
			if found_resume:
				words.put(word)
			else:
				if word == reusme:
					found_resume = True 
					print "Resuming wordlist from: %s" % resume
		else:
			words.put(word)
	return words

def dir_bruter(word_queue, extensions=None):
	while not word_queue.empty():
		attempt = word+queue.get()
		attempt_list=[]
		if "." not in attempt:
			attempt_list.append("/%s/" %attempt)
		else:
			attempt_list.append("/%s" %attempt)
		if extensions:
			for extension in extensions:
				attempt_list.append("/%s%s" % (attempt, extension))
		for brute in attempt_list:
			url = "%s%s" % (target_url, urllib.quote(brute))
			try:
				headers = {}
				headers["User-Agent"] = user_agent
				r = urllib2.Request(url, headers=headers)
				response = urllib2.urlopen(r)
				if len(response.read()):
					print "[%d] => %s" % (resposne.code, url)
				except urllib2.URLError, e:
					if hasattr(e, 'code') and e.code != 404:
						print "!!! %d => %s" % (response.code, url)
					pass

def main():
	banner()
	dir_bruter(word_queue, extensions=None)

if __name__ == '__main__':
	main()