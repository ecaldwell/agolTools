# Requires admin role.
import csv, time
from agoTools.admin import Admin

agoAdmin = Admin(<username>) # Replace <username> with your admin username.
users = agoAdmin.getUsers()

outputFile = 'c:/temp/users.csv'

with open(outputFile, 'wb') as output:
    dataWriter = csv.writer(output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # Write header row.
    dataWriter.writerow(['Full Name', 'Email', 'Username', 'Role', 'Date Created'])
    # Write user data.
    for user in users:
        if user:
        # examples of how to filter users in various ways...
        # if user['disabled'] == True:
        # if user['username'] == '<username>':
        # if 'Mark' in user['fullName']:
        # if '@agencyX.gov' in user['email']:
            dataWriter.writerow([user['fullName'], user['email'], user['username'], user['role'], time.strftime("%Y-%m-%d",time.gmtime(user['created']/1000))])
