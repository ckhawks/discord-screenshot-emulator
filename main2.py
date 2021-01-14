from datetime import datetime

input_file = 'chatlogs/3eNAbnvJ.txt'

def format_message(date, user, message_content):
    profile_pic = ""

    author = ""
    user = user.lower()

    if user.find("stellaric") != -1:
        author = "Stellaric"
        profile_pic = "https://cdn.discordapp.com/avatars/117778632021245957/a_b83768a2eeeca66e7ff88dee740284fc.png?size=128"
    elif user.find("lordofpoop") != -1:
        author = "Lordofpoop"
        profile_pic = "https://cdn.discordapp.com/avatars/198960915616497664/21f3698f22e0d8de039b22223fea62b7.png?size=128"
    elif user.find("directive") != -1:
        author = "directive"
        profile_pic = "https://cdn.discordapp.com/avatars/213500836343578625/83bdbb8a6076d972799f4b82f96e52e4.png?size=128"
    elif user.find("manager") != -1:
        author = "Manager"
        profile_pic = "https://cdn.discordapp.com/avatars/219637673273458699/1bc8b0a74325b3d1bd5df3b1419cf118.png?size=128"

    time = date #"1:29 PM"
    
    # 02-Sep-19 12:05 AM
    datetime_object = datetime.strptime(date, '%d-%b-%y %I:%M %p') # '%b-%d %Y %I:%M%p')

    print(date)
    time = datetime_object.strftime('%I:%M %p')
    message = message_content.strip() #"he alive !!!!!!!!"

    return f"""
        <div class="message-2qnXI6 cozyMessage-3V1Y8y groupStart-23k01U wrapper-2a6GCs cozy-3raOZG zalgo-jN1Ica" role="listitem" data-list-item-id="chat-messages___chat-messages-799362128745594881" tabindex="-1" id="chat-messages-799362128745594881">
        <div class="contents-2mQqc9" role="document"><img src="{profile_pic}" aria-hidden="true" class="avatar-1BDn8e clickable-1bVtEA" alt=" ">
        <h2 class="header-23xsNx"><span class="headerText-3Uvj1Y"><span class="username-1A8OIy clickable-1bVtEA" aria-controls="popout_59" aria-expanded="false" role="button" tabindex="0">{author}</span></span><span class="timestamp-3ZCmNB"><span aria-label="Today at 1:39 PM">Today at {time}</span></span>
        </h2>
        <div class="markup-2BOw-j messageContent-2qWWxC">{message}</div>
        </div>
        <div class="container-1ov-mD"></div>
        </div>
    """

def create_html():
    with open('templates/upper.html', 'r') as file:
        upper = file.read().replace('\n', '')

    with open('templates/lower.html', 'r') as file:
        lower = file.read().replace('\n', '')
    
    messages = ""

    f = open(input_file, 'r') 
    count = 0
    date = ""
    user = ""
    message_content = ""

    while True: 
        count += 1
    
        # Get next line from file 
        line = f.readline() 
    
        # if line is empty 
        # end of file is reached 
        if not line: 
            messages = messages + format_message(date, user, message_content)
            break

        dateend = line.find(']')
        
        if dateend != -1: # found next dateend
            if count != 1:
                messages = messages + format_message(date, user, message_content)  # print previous message
            date = line[1:dateend].strip()
            user = line[dateend+2:].strip()
            message_content = ""
        else:
            message_content = message_content + line
            #print("Not dateline")

        # print("Line{}: {}".format(count, line.strip())) 
    
    f.close() 
    
    file1 = open('output.html', 'w') 

    # Writing a string to file 
    file1.write(upper + messages + lower) 
    

    # Closing file 
    file1.close() 

create_html()


