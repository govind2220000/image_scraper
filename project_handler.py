from os import close
import scraper
import requests
from logger.auto_logger import autolog
import shutil
from mail import send_email

count = 1

def upload_data(email, data):

    '''
    UPLOADS DATA IN ZIP FORMAT ON ANONFILES.COM
    '''

    autolog("inside upload_data function")
    global count
    url = "https://api.anonfiles.com/upload"
    header = {'Content-type': 'application/octet-stream'}
    files = {
        'file': (f'tmp/{data}/{data}.tar', open(f'tmp/{data}/{data}.tar', 'rb')),
    }
    try:
        tmp = requests.post('https://api.anonfiles.com/upload', files=files)
        tmp = tmp.json()
        url = tmp["data"]["file"]["url"]["full"]
        autolog("Uploaded data successfully")
        send_email(email, url)
    except:
   
        autolog("Uploading Failed. Retrying "+count+" of 3",2)

        if count <= 3:
            count += 1
            upload_data(data)

        else:
            autolog("Sending failed.",3)
    finally:
        autolog("closed file")



def run_scrapper(email, data, count) -> None:
    
    '''
    SCRAPING THE IMAGES FROM CHROME USING SELENIUM
    '''

    autolog("Opening chrome")
    try:
        scrap = scraper.Webscraper()
        autolog("Chrome opened successfully")
    except:
        autolog("Failed to open chrome.")
        exit(-1)

    try:
        scrap.search_string(data)
        scrap.click_img_button()
        for x in range(count):
            screenshot_path = scrap.screenshot_image(str(x))
            scrap.click_next_button()

        scrap.close()
        autolog("Scraping completed successfully")
        autolog("Zipping data")
        shutil.make_archive(f"tmp/{data}/{data}", "tar",f"tmp/{data}")
        autolog("Done.")

        upload_data(email, data)
        
    except:
        autolog("Scraping failed.",3)
   

#run_scrapper("lirawi2547@fada55.com","qwe",10)