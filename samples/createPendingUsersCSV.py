# Requires admin role.
import csv, time, urllib, json
from agoTools.admin import Admin
 
agoAdmin = Admin('oevans') # Replace <username> with your admin username.
token = agoAdmin.user.token
 
# Requests first 100 invitations, script must be modified if >100 needed
request = 'https://www.arcgis.com/sharing/rest/portals/self/invitations?f=json&start=1&num=100&token=' + token
response = urllib.urlopen(request).read()
invites = json.loads(response)['invitations']
 
outputFile = 'c:/temp/ArcGISOnline_PendingInvitations.csv'
 
with open(outputFile, 'wb') as output:
    dataWriter = csv.writer(output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # Write header row.
    dataWriter.writerow(['Email', 'Username (if pre-defined)', 'Role', 'Invited by', 'Date Invited'])
    # Write user data.
    for invite in invites:
        dataWriter.writerow([invite['email'], invite['username'], invite['role'], invite['fromUsername'], time.strftime("%Y-%m-%d",time.gmtime(invite['created']/1000))])

