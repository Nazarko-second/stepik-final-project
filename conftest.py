import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
	parser.addoption('--language', action='store', default='en',
                     help="Choose language: spanish ('es') or french ('fr'). Default - english")


@pytest.fixture(scope="function")
def browser(request):
	language = request.config.getoption("language")
	if language == "es":
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': language})
		print("\nstarting spanish localization for test..")
		browser = webdriver.Chrome(options=options)
	elif language == "fr":
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
		print("\nstarting french localization for test..")
		browser = webdriver.Chrome(options=options)
	else:
		options = Options()
		options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US,en'})
		print("\nstarting default english localization for test..")
		browser = webdriver.Chrome(options=options)
	#browser = webdriver.Chrome()
	# fp = webdriver.FirefoxProfile()
	# fp.set_preference("intl.accept_languages", 'en-US,en')
	# browser = webdriver.Firefox(firefox_profile=fp)
	# browser.implicitly_wait(10)
	yield browser
	print("\nquit browser..")
	browser.quit()
