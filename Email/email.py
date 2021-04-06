import logging
logger = logging.getLogger(__name__)

try:
    import smtplib
except:
    logger.error("could not import smtplib")
    pass

class email():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.port = 587
        self.setupEmailServer()

    def setupEmailServer(self):
        """
        Setup email server.
        """
        self.server = smtplib.SMTP("smtp.gmail.com", self.port)
        self.server.starttls()
        self.server.login(self.email, self.password)
        return

    def sendEmail(self, message, subject):
        """
        Send given email
        """
        DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (self.email, self.email, \
                                                     subject, message.encode('UTF-8'))
        self.server.sendmail(self.email, self.email, DATA)