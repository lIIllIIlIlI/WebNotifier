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
        self.port = None
        self.server = None

    def setupEmailServer(self, port):
        """
        Setup email server.
        """
        self.port = port
        self.server = smtplib.SMTP("smtp.gmail.com", port) 
        self.server.starttls() 
        self.server.login(self.email, self.password) 
        return 

    def sendEmail(self, message, subject):
        """
        Send given email
        """
        DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (self.email, self.email, \
                                                     subject, message)
        self.server.sendmail(self.email, self.email, DATA)