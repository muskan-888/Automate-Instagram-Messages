# Automate-Instagram-Messages
Can send a single message to any number of people on instagram.

**Tech-stack used:**

1. SELENIUM: An open-source tool that automates web-browsers.It provides a single interface to write scripts in any programming language. 

2. Webdriver-manager: For automatically managing drivers for the browsers. It automatically downloads the latest version of the browser you want to use.

3. ChromeDriver: Used so that selenium web-driver can control Chrome.

4. Google Chrome

**Important Terms:**

1. Xpath: XPath can be used to navigate through elements and attributes in an XML document.XPath expressions can be used in JavaScript,Java,XML Schema, PHP, Python, C and C++,    and lots of other languages. 
 To find Xpath of an element in google chrome, right click on it, click on Inspect, then right click on selected text and select 'Copy Xpath' from 'Copy' drop down list.

2. How webdriver-manager is helpful?

  Before: We had to download binary chromedriver, unzip it and set path to this driver like this:
  webdriver.Chrome('/home/user/drivers/chromedriver')
  ChromeDriverManager(path=custom_path).install()
  It is boring.Moreover every time the new version of driver released, we have to repeat all steps again.
  With webdriver manager, only two simple steps:

   (i) Install manager:
    pip install webdriver-manager

   (ii)Use with Chrome:
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install())
 




