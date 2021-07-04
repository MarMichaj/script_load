from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import glob
import time

#TODO: CHECK IF CRDOWNLOAD FILE ENDING NOT OCCURING ANYMORE
#TODO: finish methods for scraping of all podcast base urls
#TODO: mechanism to download only new podcasts
#TODO: check requirements
#TODO: increase actual database of transcripts (perform downloads)
#TODO: remove absolute paths
#TODO: for requirements: chrome,... in rep -> relative path
#TODO: distinguish between languages
#TODO: get .gitignore working

class script_load:

    def __init__(self):
        self.list_file_of_all_podcasts_urls = ""
        self.list_of_all_podcasts_urls = []
        self.url_all_podcasts = "https://www.happyscribe.com/public/podcasts"
        self.current_base_url = None
        self.chrome_binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.chrome_driver_binary_location = "/Users/martin/Projects/script_load/chromedriver"
        self.default_download_location = "/Users/martin/Projects/script_load/testdownloads"

    #functions for scraping transcripts for an individual podcast

    def get_all_transcripts_of_this_podcast(self):
        urls = self.get_all_episode_urls_of_podcast()
        print("There are", len(urls), "podcast urls")
        print("\n")
        print("Starting to download transcripts:")
        for url in urls:
            print(url)
            self.get_episode_transcript(url)

    def get_episode_transcript(self, url):
        # button.click() rarely throws errors I don't understand. Therefore I just try it 5 times here
        for i in range(5):
            try:
                options = webdriver.ChromeOptions()
                options.binary_location = self.chrome_binary_location
                prefs = {'download.default_directory': self.default_download_location}
                options.add_experimental_option('prefs', prefs)
                options.headless = True

                driver = webdriver.Chrome(self.chrome_driver_binary_location, options=options)

                driver.get(url)
                button = driver.find_element_by_id('btn-download')
                target = driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-download")))
                download_time = time.time()

                button.click()
                i = 0
                while i >= 0:
                    if i == 30:
                        print(
                            "download of " + url + " failed")
                        break
                    list_of_files = glob.glob(
                        self.default_download_location+'/*')
                    latest_file = max(list_of_files, key=os.path.getctime)
                    latest_file_time = os.path.getmtime(latest_file)
                    if latest_file_time > download_time and latest_file[-4:]==".pdf":
                        break
                    else:
                        time.sleep(2)
                        i+=1
                driver.quit()
                break

            except Exception:
                print("Problem (probably) pressing download button for " + url)

    def get_all_episode_urls_of_podcast(self):
        """
        :param: url of first page for podcast

        :return: urls for all episodes of that podcast
        """
        pages = self.get_urls_of_episode_list_pages(self.current_base_url)
        links = []
        for page in pages:
            links = links + self.get_episode_urls_on_page(page)
        return links

    def get_episode_urls_on_page(self, page: str):
        """
        :return: list of podcast urls on page
        """
        options = webdriver.ChromeOptions()
        options.binary_location = self.chrome_binary_location
        options.headless = True

        driver = webdriver.Chrome(self.chrome_driver_binary_location, options=options)

        driver.get(page)
        links = []
        for podcast in driver.find_elements_by_class_name('hsp-card-episode'):
            link = podcast.get_attribute('href')
            links.append(link)
        driver.quit()
        return links

    def is_valid_episode_list_page(self, url: str):
        """
        checks if url leads to page with list of episode links

        :return: Boolean
        """
        options = webdriver.ChromeOptions()
        options.binary_location = self.chrome_binary_location
        options.headless = True

        driver = webdriver.Chrome(self.chrome_driver_binary_location, options=options)
        driver.get(url)
        text = "This podcast currently doesn't have any transcript"
        if text in driver.page_source:
            driver.quit()
            return False
        else:
            driver.quit()
            return True

    def get_urls_of_episode_list_pages(self, base_url: str):
        """
        :param base_url:  url of first page for podcast

        :return: list of all url's that list episode of that podcast
        """

        i = 1
        print("current page:")
        while i > 0:
            if not self.is_valid_episode_list_page(base_url + "?page=" + str(i)):
                break
            else:
                print(i)
                i += 1
        number_of_pages = i - 1
        pages = []
        for i in range(1, number_of_pages + 1):
            pages.append(base_url + "?page=" + str(i))
        return pages



    #functions for scraping base urls for all podcasts


    def is_valid_podcast_list_page(self):
        print("hello")

    def get_base_urls_for_all_podcasts(self):
        """
        writes list of base urls of all podcast into self.list_file_of_all_podcasts_urls and self.list_of_all_podcasts_urls
        :return:
        """
        i = 1
        print("current page:")
        while i > 0:
            if not self.is_valid_podcast_list_page(self.url_all_podcasts + "?page=" + str(i)):
                break
            else:
                print(i)
                i += 1
        number_of_pages = i - 1
        pages = []
        for i in range(1, number_of_pages + 1):
            pages.append(self.url_all_podcasts + "?page=" + str(i))
        return pages


    #other functions
    def set_base_url(self, base_url):
        self.current_base_url=base_url