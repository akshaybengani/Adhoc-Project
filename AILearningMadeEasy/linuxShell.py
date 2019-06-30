import cgi
import cgitb
import os

cgitb.enable()
print("Content-type=text/html")
print("")

'''
We need to install openssl and shell in a box in the docker container.
Set a username and password to docker container for shell in a box.
Start the service of shellinabox in docker container.
'''
os.system("sudo ")