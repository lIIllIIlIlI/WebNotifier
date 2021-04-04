
import keyring
import getpass 


def getEmailPassword(emailAddress):
    # retrieve password
    password = keyring.get_password('email', emailAddress)
    if not password:
        password = getpass.getpass(prompt='Enter password for {}'.format(emailAddress)) 
        # store password in keyring
        keyring.set_password('email', emailAddress, password)
    return password