from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)
	
	def open(self):
		self.browser.get(self.url)

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			print("NO ELEMENT @@@@@")
			return False
		return True


#print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))