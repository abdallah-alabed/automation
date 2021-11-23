import re

##### reading the text file
with open('./assets/potential-contacts.txt', 'r') as f:
    text=f.read()

##### finding phones 
phone_finder =r"[0-9-+()]{7,}"
find_phone=re.findall(phone_finder,text)
find_phone=list(dict.fromkeys(find_phone)) # to remove duplicates

##### moving phone numbers to a new file
with open('phone_numbers.txt','w') as file:
    phones=''
    for i in find_phone:
        phones+= f"{i} \n"
    file.write(f"{phones}")

##### finding emails
email_finder= r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
find_email=re.findall(email_finder,text)
find_email=list(dict.fromkeys(find_email)) # to remove duplicates

##### moving email to a new file
with open('emails.txt','w') as file:
    emails=''
    for i in find_email:
        emails+= f"{i} \n"
    file.write(f"{emails}")




