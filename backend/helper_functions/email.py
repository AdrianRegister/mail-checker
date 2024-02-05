# returns an email dictionary which can then be added to an array and exported

def create_email_dict(email):
    creation_time = email.CreationTime
    subject = email.Subject
    body = email.body
    email = {
        'creation_time': creation_time,
        'subject': subject,
        'body': body
    }
    return email