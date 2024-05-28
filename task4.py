def extract_emails(email_list):
    unique_emails = set()
    for i in email_list:
        #assuming email addresses are enclosed in angle brackets
        if '<' in i and '>' in i:
                email = i.split('<')[1].split('>')[0]
                unique_emails.add(email)
    return list(unique_emails)

mylist = ['qwerty','keongsegg','<example@gmail.com>','what color is your Bugatti?','<xyz@gmail.com>']
extractedEmails = extract_emails(mylist)
print(extractedEmails)
