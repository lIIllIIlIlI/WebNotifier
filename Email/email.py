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
        # user is logged out after some time, therefore establish
        # connection right before sending the email
        # self.setupEmailServer()

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
        self.setupEmailServer()
        DATA = 'From:%s\nTo:%s\nSubject:%s\n\n%s' % (self.email, self.email, \
                                                     subject, message)
        self.server.sendmail(self.email, self.email, DATA)
        self.server.quit()