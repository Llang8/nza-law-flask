from twilio.rest import Client


def createVerification(phoneNumber):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACf161ba86fc3153d16a3f3e32c45c077d'
    auth_token = 'd9ed4e824bb4e07416ebdebe00eb8d4d'
    client = Client(account_sid, auth_token)

    verification = client.verify \
                        .services('VA1d596c7dbac7d9ab21a6265d7bca554f') \
                        .verifications \
                        .create(to='+1' + phoneNumber, channel='sms')

    return verification.sid

def verifyVerification(phoneNumber, code):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACf161ba86fc3153d16a3f3e32c45c077d'
    auth_token = 'd9ed4e824bb4e07416ebdebe00eb8d4d'
    client = Client(account_sid, auth_token)

    verification_check = client.verify \
                            .services('VA1d596c7dbac7d9ab21a6265d7bca554f') \
                            .verification_checks \
                            .create(to='+14159373912', code='1234')

    return verification_check.sid