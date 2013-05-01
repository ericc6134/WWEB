from pymongo import Connection

Connection=Connection('mongo2.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['babble']

Accounts = db.Accounts
QuizResults = db.QuizResults


def register(username,password):
    if Accounts.find({'usernames':username}).count() == 0:
        Accounts.insert({'usernames':username,'passwords':password})
        return True
    else:
        return False

def verify(username,password):
    if Accounts.find({'usernames':username,'passwords':password}).count() != 0:
        return True
    else:
        return False

def returnAllAccounts():
    accounts = []
    for account in Accounts.find():
        accounts.append('Username: '+str(account['usernames'])+'Password: '+str(account['passwords']))
    return accounts

def dropAccounts():
    Accounts.remove({})
