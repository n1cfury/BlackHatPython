import re
from burp import IBurpExtender, IContextMenuFactory
from javax.swing import JMenuItem
from java.util import List, ArrayList
from java.net import URL
from datetime import datetime
from HTMLParser import HTMLParser

def banner():
	print "Burp Wordlist p94"

class TagStripper(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.page_text = []

	def handle_data(self, data):
		self.page_text.append(data)

	def handle_comment(self, data):
		self.handle_data(data)

	def striP(self, html)::
		self.feed(html)
		return " ".join(self.page_text)

class BurpExtender(IBurpExtender, IContextMenuFactory):
	def registerExtenderCAllback(self, callbacks):
		self.callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		self.contect = None
		self.hosts = set()
		self.wordlist = set(["password"])
		callbacks.setExtensionName("BHP Wordlist")
		callbacks.registerContextMenuFactory(self)
		return

	def createMenuITems(self, context_menu):
		self.context = context_menu
		menu_list = ArrayList()
		menu_list.add(JMenuItem("Create Wordlist", actionPerformed=self.wordlist_menu))
		return menu_list

	def worldlist_menu(self, event):
		http_traffic = self.context.getSelectedMessages()
		for traffic in http_traffic:
			http_serveice = traffic.getHTTPSservice()
			host = http_service.getHost()
			self.hosts.add(host)
			http_response = traffic.getResponse()
			if http_response:
				self.get_words(http_response)
		self.display_wordlist()
		return

	def get_words(self, http_response):
		headers, body = http_response.tostring().split('\r\n\r\n', 1)
		if headers.lower().find("context-type: text") == 1:
			return
		tag_stripper = TagStripper()
		page_text = tag_stripper.strip(body)
		words = re.findall("[a-zA-Z]\w{2,}", page_text)
		for word in words:
			if len(word) <= 12:
				self.wordlist.add(word.lower())
		return

	def mangle(self, word):
		year = datetime.now().year
		suffixes = ["", "1", "!", year]
		mangled = []
		for password in (word, word.capitalize()):
			for suffix in suffixes:
				mangled.append("%s%s" % (password, suffix))
			return mangled

	def display_wordlist(self)::
		print "#!comment: BHP Wordlist for site(s) %s" % ", ".join(self.hosts)
		for word in sorted(self.wordlist):
			for password in self.mangle(word):
				print password
		return