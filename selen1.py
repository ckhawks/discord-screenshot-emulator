from datetime import datetime

import time 


input_file = 'chatlogs/tJ3HJmsa.txt'
skip_lines = 0
ss_height = 900

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
    #print(f"The fucky date {date}")
    datetime_object = datetime.strptime(date, '%d-%b-%y %I:%M %p') # '%b-%d %Y %I:%M%p')

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

    for i in range(skip_lines):
        f.readline()
        count = count + 1
        #print(count)

    date = "29-Jul-19 09:05 PM"
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
                if count != skip_lines:
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
    output = upper + messages + lower
    file1.write(output) 
    

    # Closing file 
    file1.close() 

create_html()




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument(f"--window-size=600,{ss_height}") 
driver = webdriver.Chrome(options=chrome_options)
#driver.get("html.html")

# driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))

driver.get("file:///D:/Websites/discord-screenshot-emulator/output.html")  # https://stackoverflow.com/a/52498384
""" # assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source """
time.sleep(10)
driver.save_screenshot("screenshot.png")
driver.close()


# cropping image https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.crop

from PIL import Image

im = Image.open("screenshot.png")

# The crop method from the Image module takes four coordinates as input.
# The right can also be represented as (left+width)
# and lower can be represented as (upper+height).
(left, upper, right, lower) = (0, 20, 570, ss_height-132)

# Here the image "im" is cropped and assigned to new variable im_crop
im_crop = im.crop((left, upper, right, lower))

im_crop.save("screenshot_cropped.png")


