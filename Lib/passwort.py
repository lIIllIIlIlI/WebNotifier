
import keyring
import getpass 


def safePasswort():
    # retrieve password
    twitterPassword = keyring.get_password('twitter', 'twitterAccount')

    if not twitterPassword:
    twitterPassword = getpass.getpass(prompt='Enter your twitter password') 
    # store password in keyring
    keyring.set_password('twitter', 'twitterAccount', 'twitterPassword')

def getPasswort():
    # retrieve password
    twitterPassword = keyring.get_password('twitter', 'twitterAccount')

    if not twitterPassword:
    twitterPassword = getpass.getpass(prompt='Enter your twitter password') 
    # store password in keyring
    keyring.set_password('twitter', 'twitterAccount', 'twitterPassword')