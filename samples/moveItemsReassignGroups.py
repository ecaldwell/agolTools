#### Move all items from one account to another, reassign ownership of all groups, or add user to another user's groups

# Requires admin role
# If you want to do all three tasks at once, see migrateAccount or migrateAccounts functions

from agoTools.admin import Admin
agoAdmin = Admin(<username>)  # Replace <username> with your admin username

agoAdmin.reassignAllUser1ItemsToUser2(agoAdmin, <userFrom>, <userTo>)  #Replace with your current and new account usernames
agoAdmin.reassignAllGroupOwnership(agoAdmin, <userFrom>, <userTo>)
agoAdmin.addUser2ToAllUser1Groups(agoAdmin, <userFrom>, <userTo>)


#### Migrate person to a new account within the same Org

# Requires admin role
# Useful when migrating to Enterprise Logins.
# Reassigns all items/groups to new owner and
# adds userTo to all groups which userFrom is a member.'''

from agoTools.admin import Admin
myAgol = Admin('<username>')  # Replace <username> your ADMIN account

# for migrating a single account...
myAgol.migrateAccount(myAgol, '<userFrom>', '<userTo>')   # Replace with usernames between which you are moving items

# for migrating a batch of accounts
myAgol.migrateAccounts(myAgol, <path to user mapping CSV>)   # Replace with path to CSV file with col1=userFrom, col2=userTo