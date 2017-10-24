from bs4 import BeautifulSoup # Import BeautifulSoup (to parse what we download)
import time # Import Time (to add a delay between the times the scape runs)
import smtplib # Import smtplib (to allow us to email)
import sys # Import sys to pass system arguments to PyQt4
#PyQt4 used for acting like a client to load the page, required to scrape dynamically generated content (i.e. js rendered webpages)
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage

class Client(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):
        self.app.quit()

url = "add-url"

search = True
while search:
    client_response = Client(url)
    source = client_response.mainFrame().toHtml()

    soup = BeautifulSoup(source, "html.parser")
    # if the check returns None
    if soup.find("add-something-to-check-on-webpage") == None:
        # wait 60 seconds,
        time.sleep(60)
    # but if the check returns something
    else:
        # create an email message with just a subject line,
        msg = 'add-msg'
        # set the 'from' address,
        fromaddr = 'add-from-email'
        # set the 'to' addresses,
        toaddrs  = ['add-to-address']

        # setup the email server,
        server = smtplib.SMTP('add-host', add-port)
        server.starttls()
        # add my account login name and password,
        server.login(fromaddr, 'add-password')

        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)

        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()

        search = False
