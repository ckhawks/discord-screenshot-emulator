from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

with open('chatlogs/3eNAbnvJ - Copy.txt', 'r') as f:
    # Further file processing goes here
    lines = f.readlines()

""" for line in lines:
    print(line) """

date = ""
user = ""
message_content = ""

for i in range(len(lines)):
    line = lines[i]
    # print(line.strip())
    dateend = line.find(']')
    
    if dateend != -1:
        date = line[1:dateend].strip()
        user = line[dateend+2:].strip()
        message_content = ""
    else:
        message_content = message_content + line
        #print("Not dateline")

    print(f"Date: {date}, User: {user}, Message: {message_content}")