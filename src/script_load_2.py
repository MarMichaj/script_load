from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import glob
import time

# TODO: download directories structed by podcasts
# TODO: download all transcripts
# TODO: set up separate file containing last information (urls) and write parsers
# TODO: remove personal locations, everything relative, except for chrome

# TODO: mechanism to download only new podcasts
# TODO: check requirements
# TODO: remove absolute paths
# TODO: for requirements: chrome,... in rep -> relative path
# TODO: distinguish between languages
# TODO: get .gitignore working
# TODO: Automatic Updating (urls ,...)
# TODO: CHECK IF CRDOWNLOAD FILE ENDING NOT OCCURING ANYMORE

class script_load:

    def __init__(self):
        self.list_file_of_all_podcasts_urls = ""
        self.list_of_all_podcasts_urls = []
        self.url_all_podcasts = "https://www.happyscribe.com/public/podcasts"
        self.current_base_url = None
        self.chrome_binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        self.chrome_driver_binary_location = "/Users/martin/Projects/script_load/chromedriver"
        self.default_download_location = "/Users/martin/Projects/script_load/testdownloads"
        self.all_podcast_base_urls_location = ""
        self.all_podcast_urls=['https://www.happyscribe.com/public/2-bears-1-cave-with-tom-segura-bert-kreischer', 'https://www.happyscribe.com/public/30-minuten-rauw-door-ruud-de-wild', 'https://www.happyscribe.com/public/5-minuten-harry-podcast-von-coldmirror', 'https://www.happyscribe.com/public/6-minute-vocabulary', 'https://www.happyscribe.com/public/a-bit-of-optimism', 'https://www.happyscribe.com/public/all-ears-english', 'https://www.happyscribe.com/public/alle-wege-fuhren-nach-ruhm-awfnr', 'https://www.happyscribe.com/public/american-scandal', 'https://www.happyscribe.com/public/american-shadows', 'https://www.happyscribe.com/public/and-that-s-why-we-drink', 'https://www.happyscribe.com/public/anna-faris-is-unqualified', 'https://www.happyscribe.com/public/anything-goes-with-emma-chamberlain', 'https://www.happyscribe.com/public/a-players-the-top-startups-recipes-to-build-teams-of-top-performers', 'https://www.happyscribe.com/public/aqui-hay-dragones', 'https://www.happyscribe.com/public/armchair-expert-with-dax-shepard', 'https://www.happyscribe.com/public/bachelor-happy-hour', 'https://www.happyscribe.com/public/bad-faith', 'https://www.happyscribe.com/public/baywatch-berlin', 'https://www.happyscribe.com/public/bent', 'https://www.happyscribe.com/public/bffs-featuring-josh-richards-and-dave-portnoy', 'https://www.happyscribe.com/public/biggerpockets-real-estate-podcast', 'https://www.happyscribe.com/public/bliss-stories', 'https://www.happyscribe.com/public/boss-uncaged', 'https://www.happyscribe.com/public/brave-new-planet', 'https://www.happyscribe.com/public/brendan-o-connor', 'https://www.happyscribe.com/public/brown-pundits', 'https://www.happyscribe.com/public/busy-philipps-is-doing-her-best', 'https://www.happyscribe.com/public/california-city', 'https://www.happyscribe.com/public/call-her-daddy', 'https://www.happyscribe.com/public/c-dans-l-air', 'https://www.happyscribe.com/public/charlemos-de-cine', 'https://www.happyscribe.com/public/choses-a-savoir', 'https://www.happyscribe.com/public/click-bait-with-bachelor-nation', 'https://www.happyscribe.com/public/cold', 'https://www.happyscribe.com/public/conan-o-brien-needs-a-friend', 'https://www.happyscribe.com/public/conspiracy-theories', 'https://www.happyscribe.com/public/conversations-with-coleman', 'https://www.happyscribe.com/public/crime-countdown', 'https://www.happyscribe.com/public/criminal', 'https://www.happyscribe.com/public/criminalia', 'https://www.happyscribe.com/public/crims', 'https://www.happyscribe.com/public/cualquier-tiempo-pasado-fue-anterior', 'https://www.happyscribe.com/public/cuarto-milenio-oficial', 'https://www.happyscribe.com/public/curiosidades-de-la-historia-national-geographic', 'https://www.happyscribe.com/public/daders', 'https://www.happyscribe.com/public/dan-carlin-s-hardcore-history', 'https://www.happyscribe.com/public/dan-snow-s-history-hit', 'https://www.happyscribe.com/public/das-coronavirus-update-mit-christian-drosten', 'https://www.happyscribe.com/public/dateline-nbc', 'https://www.happyscribe.com/public/david-tennant-does-a-podcast-with', 'https://www.happyscribe.com/public/death-becomes-him', 'https://www.happyscribe.com/public/de-correspondent', 'https://www.happyscribe.com/public/de-dag', 'https://www.happyscribe.com/public/deep-cover-the-drug-wars', 'https://www.happyscribe.com/public/de-jortcast', 'https://www.happyscribe.com/public/de-krokante-leesmap', 'https://www.happyscribe.com/public/de-rode-lantaarn', 'https://www.happyscribe.com/public/der-tagesschau-zukunfts-podcast-mal-angenommen', 'https://www.happyscribe.com/public/desert-island-discs', 'https://www.happyscribe.com/public/dessine-moi-un-produit', 'https://www.happyscribe.com/public/de-stemming-van-vullings-en-van-der-wulp', 'https://www.happyscribe.com/public/de-tribune', 'https://www.happyscribe.com/public/de-willem-podcast', 'https://www.happyscribe.com/public/de-zelfhulpboekenclub', 'https://www.happyscribe.com/public/dick-voormekaar-podcast', 'https://www.happyscribe.com/public/die-johnsons', 'https://www.happyscribe.com/public/dirty-diana', 'https://www.happyscribe.com/public/documentary-on-one-podcast', 'https://www.happyscribe.com/public/dolly-parton-s-america', 'https://www.happyscribe.com/public/do-no-harm', 'https://www.happyscribe.com/public/don-t-ask-tig', 'https://www.happyscribe.com/public/down-the-hill-the-delphi-murders', 'https://www.happyscribe.com/public/echt-gebeurd', 'https://www.happyscribe.com/public/een-podcast-over-media', 'https://www.happyscribe.com/public/einfach-mal-luppen', 'https://www.happyscribe.com/public/el-larguero', 'https://www.happyscribe.com/public/el-partidazo-de-cope', 'https://www.happyscribe.com/public/el-transistor', 'https://www.happyscribe.com/public/espacio-en-blanco', 'https://www.happyscribe.com/public/even-the-rich', 'https://www.happyscribe.com/public/everymum', 'https://www.happyscribe.com/public/ex', 'https://www.happyscribe.com/public/fantasy-footballers-fantasy-football-podcast', 'https://www.happyscribe.com/public/film-on-the-rocks', 'https://www.happyscribe.com/public/finshots-daily', 'https://www.happyscribe.com/public/fivethirtyeight-politics', 'https://www.happyscribe.com/public/football-weekly', 'https://www.happyscribe.com/public/forgotten-women-of-juarez', 'https://www.happyscribe.com/public/franck-ferrand-raconte', 'https://www.happyscribe.com/public/freakonomics-radio', 'https://www.happyscribe.com/public/geheimakte', 'https://www.happyscribe.com/public/geld-ganz-einfach-der-podcast-mit-saidi-von-finanztip', 'https://www.happyscribe.com/public/gemischtes-hack', 'https://www.happyscribe.com/public/get-sleepy-sleep-meditation-and-stories', 'https://www.happyscribe.com/public/get-together', 'https://www.happyscribe.com/public/girls-gotta-eat', 'https://www.happyscribe.com/public/global-news-podcast', 'https://www.happyscribe.com/public/golden-talkies', 'https://www.happyscribe.com/public/good-for-you', 'https://www.happyscribe.com/public/grounded-with-louis-theroux', 'https://www.happyscribe.com/public/handelsblatt-morning-briefing', 'https://www.happyscribe.com/public/handelsblatt-today', 'https://www.happyscribe.com/public/happy-place', 'https://www.happyscribe.com/public/haunted-places', 'https://www.happyscribe.com/public/haunted-places-ghost-stories', 'https://www.happyscribe.com/public/herrera-en-cope', 'https://www.happyscribe.com/public/highlights-from-the-pat-kenny-show', 'https://www.happyscribe.com/public/hintergrund-deutschlandfunk', 'https://www.happyscribe.com/public/historiquement-votre', 'https://www.happyscribe.com/public/hodgetwins', 'https://www.happyscribe.com/public/hold-these-truths-with-dan-crenshaw', 'https://www.happyscribe.com/public/hondelatte-raconte-christophe-hondelatte', 'https://www.happyscribe.com/public/hope-through-history', 'https://www.happyscribe.com/public/hotboxin-with-mike-tyson', 'https://www.happyscribe.com/public/hotel-matze', 'https://www.happyscribe.com/public/how-to-citizen-with-baratunde', 'https://www.happyscribe.com/public/how-to-fail-with-elizabeth-day', 'https://www.happyscribe.com/public/impaulsive-with-logan-paul', 'https://www.happyscribe.com/public/inside-the-greenroom-with-pv3', 'https://www.happyscribe.com/public/in-the-dark', 'https://www.happyscribe.com/public/in-the-red-clay', 'https://www.happyscribe.com/public/invest-like-the-best', 'https://www.happyscribe.com/public/it-was-said', 'https://www.happyscribe.com/public/jocko-podcast', 'https://www.happyscribe.com/public/joel-osteen-podcast', 'https://www.happyscribe.com/public/jong-beleggen-de-podcast', 'https://www.happyscribe.com/public/just-b-with-bethenny-frankel', 'https://www.happyscribe.com/public/justice-matters-with-glenn-kirschner', 'https://www.happyscribe.com/public/knorrepodcast-met-martijn-koning-en-sander-van-opzeeland', 'https://www.happyscribe.com/public/l-after-foot', 'https://www.happyscribe.com/public/la-rosa-de-los-vientos', 'https://www.happyscribe.com/public/la-vida-moderna', 'https://www.happyscribe.com/public/la-voz-de-cesar-vidal', 'https://www.happyscribe.com/public/les-grosses-tetes', 'https://www.happyscribe.com/public/les-imposteurs', 'https://www.happyscribe.com/public/let-s-do-shots', 'https://www.happyscribe.com/public/lex-fridman-podcast-artificial-intelligence-ai', 'https://www.happyscribe.com/public/l-heure-du-crime', 'https://www.happyscribe.com/public/literally-with-rob-lowe', 'https://www.happyscribe.com/public/live-slow-ride-fast-podcast', 'https://www.happyscribe.com/public/lore', 'https://www.happyscribe.com/public/lovett-or-leave-it', 'https://www.happyscribe.com/public/maintenance-phase', 'https://www.happyscribe.com/public/making-sense-with-sam-harris', 'https://www.happyscribe.com/public/man-man-man-de-podcast', 'https://www.happyscribe.com/public/market-mondays', 'https://www.happyscribe.com/public/marketplace', 'https://www.happyscribe.com/public/mark-levin-podcast', 'https://www.happyscribe.com/public/mas-de-uno', 'https://www.happyscribe.com/public/medical-medium-podcast', 'https://www.happyscribe.com/public/medical-murders', 'https://www.happyscribe.com/public/memorias-de-un-tambor', 'https://www.happyscribe.com/public/met-groenteman-in-de-kast', 'https://www.happyscribe.com/public/missing-in-alaska', 'https://www.happyscribe.com/public/modern-love', 'https://www.happyscribe.com/public/morbid-a-true-crime-podcast', 'https://www.happyscribe.com/public/mordlust', 'https://www.happyscribe.com/public/my-brother-my-brother-and-me', 'https://www.happyscribe.com/public/my-favorite-murder-with-karen-kilgariff-and-georgia-hardstark', 'https://www.happyscribe.com/public/mythes-et-legendes', 'https://www.happyscribe.com/public/nadie-sabe-nada', 'https://www.happyscribe.com/public/netflix-is-a-daily-joke', 'https://www.happyscribe.com/public/nice-white-parents', 'https://www.happyscribe.com/public/nrc-onbehaarde-apen', 'https://www.happyscribe.com/public/office-ladies', 'https://www.happyscribe.com/public/on-being-with-krista-tippett', 'https://www.happyscribe.com/public/once-upon-a-time-in-the-valley', 'https://www.happyscribe.com/public/on-purpose-with-jay-shetty', 'https://www.happyscribe.com/public/oprah-s-supersoul-conversations', 'https://www.happyscribe.com/public/pardon-my-take', 'https://www.happyscribe.com/public/people-i-mostly-admire', 'https://www.happyscribe.com/public/pod-save-america', 'https://www.happyscribe.com/public/pod-save-the-world', 'https://www.happyscribe.com/public/radiolab', 'https://www.happyscribe.com/public/radio-rental', 'https://www.happyscribe.com/public/radiowissen', 'https://www.happyscribe.com/public/rationally-speaking-podcast', 'https://www.happyscribe.com/public/real-dictators', 'https://www.happyscribe.com/public/reality-steve-podcast', 'https://www.happyscribe.com/public/real-time-with-bill-maher', 'https://www.happyscribe.com/public/red-table-talk', 'https://www.happyscribe.com/public/relatable-with-allie-beth-stuckey', 'https://www.happyscribe.com/public/relative-unknown', 'https://www.happyscribe.com/public/revisionist-history', 'https://www.happyscribe.com/public/sadhguru-s-podcast', 'https://www.happyscribe.com/public/sallys-welt', 'https://www.happyscribe.com/public/scientology-fair-game', 'https://www.happyscribe.com/public/serial-killers', 'https://www.happyscribe.com/public/sex-with-emily', 'https://www.happyscribe.com/public/sh-ged-married-annoyed', 'https://www.happyscribe.com/public/small-town-murder', 'https://www.happyscribe.com/public/smartless', 'https://www.happyscribe.com/public/smoke-screen-fake-priest', 'https://www.happyscribe.com/public/snacks-daily', 'https://www.happyscribe.com/public/snap-judgment-presents-spooked', 'https://www.happyscribe.com/public/sofia-with-an-f', 'https://www.happyscribe.com/public/spittin-chiclets', 'https://www.happyscribe.com/public/steingarts-morning-briefing-der-podcast', 'https://www.happyscribe.com/public/stern-crime-spurensuche', 'https://www.happyscribe.com/public/stories-your-granny-never-told', 'https://www.happyscribe.com/public/stuff-you-missed-in-history-class', 'https://www.happyscribe.com/public/stuff-you-should-know', 'https://www.happyscribe.com/public/superstitions', 'https://www.happyscribe.com/public/sway', 'https://www.happyscribe.com/public/switched-on-pop', 'https://www.happyscribe.com/public/sword-and-scale', 'https://www.happyscribe.com/public/ted-talks-daily', 'https://www.happyscribe.com/public/tenfold-more-wicked', 'https://www.happyscribe.com/public/ten-percent-happier-with-dan-harris', 'https://www.happyscribe.com/public/the-andrew-klavan-show', 'https://www.happyscribe.com/public/the-argument', 'https://www.happyscribe.com/public/the-bald-and-the-beautiful-with-trixie-mattel-and-katya-zamo', 'https://www.happyscribe.com/public/the-bill-bert-podcast', 'https://www.happyscribe.com/public/the-bill-simmons-podcast', 'https://www.happyscribe.com/public/the-blindboy-podcast', 'https://www.happyscribe.com/public/the-breakfast-club', 'https://www.happyscribe.com/public/the-cut', 'https://www.happyscribe.com/public/the-daily', 'https://www.happyscribe.com/public/the-daily-show-with-trevor-noah-ears-edition', 'https://www.happyscribe.com/public/the-dan-bongino-show', 'https://www.happyscribe.com/public/the-dan-le-batard-show-with-stugotz', 'https://www.happyscribe.com/public/the-darin-olien-show', 'https://www.happyscribe.com/public/the-dave-portnoy-show-with-eddie-co', 'https://www.happyscribe.com/public/the-dave-ramsey-show', 'https://www.happyscribe.com/public/the-documentary-podcast', 'https://www.happyscribe.com/public/the-dr-john-delony-show', 'https://www.happyscribe.com/public/the-english-we-speak', 'https://www.happyscribe.com/public/the-etcs-with-kevin-durant', 'https://www.happyscribe.com/public/the-happiness-lab-with-dr-laurie-santos', 'https://www.happyscribe.com/public/the-hidden-djinn', 'https://www.happyscribe.com/public/the-jimmy-dore-show', 'https://www.happyscribe.com/public/the-joe-budden-podcast-with-rory-mal', 'https://www.happyscribe.com/public/the-joe-rogan-experience', 'https://www.happyscribe.com/public/the-jordan-b-peterson-podcast', 'https://www.happyscribe.com/public/the-journal', 'https://www.happyscribe.com/public/the-knowledge-project-with-shane-parrish', 'https://www.happyscribe.com/public/the-laughs-of-your-life-with-doireann-garrihy', 'https://www.happyscribe.com/public/the-lincoln-project', 'https://www.happyscribe.com/public/the-lupe-and-royce-show', 'https://www.happyscribe.com/public/the-meateater-podcast', 'https://www.happyscribe.com/public/the-megyn-kelly-show', 'https://www.happyscribe.com/public/the-michelle-obama-podcast', 'https://www.happyscribe.com/public/the-mindset-mentor', 'https://www.happyscribe.com/public/the-moth', 'https://www.happyscribe.com/public/the-murders-at-white-house-farm-the-podcast', 'https://www.happyscribe.com/public/the-new-abnormal-with-molly-jong-fast-rick-wilson', 'https://www.happyscribe.com/public/the-orange-tree', 'https://www.happyscribe.com/public/the-piketon-massacre', 'https://www.happyscribe.com/public/the-prof-g-show-with-scott-galloway', 'https://www.happyscribe.com/public/the-pulte-podcast', 'https://www.happyscribe.com/public/the-rachel-maddow-show', 'https://www.happyscribe.com/public/the-ranveer-show', 'https://www.happyscribe.com/public/the-rich-roll-podcast', 'https://www.happyscribe.com/public/the-rush-limbaugh-show', 'https://www.happyscribe.com/public/the-sarah-silverman-podcast', 'https://www.happyscribe.com/public/the-secret-s-out', 'https://www.happyscribe.com/public/the-seen-and-the-unseen-hosted-by-amit-varma', 'https://www.happyscribe.com/public/the-sip-with-ryland-adams-and-lizze-gordon', 'https://www.happyscribe.com/public/the-slutrepreneur-podcast', 'https://www.happyscribe.com/public/the-syndicate', 'https://www.happyscribe.com/public/the-tim-ferris-show', 'https://www.happyscribe.com/public/the-tommy-and-hector-podcast-with-laurita-blewitt', 'https://www.happyscribe.com/public/the-way-i-heard-it-with-mike-rowe', 'https://www.happyscribe.com/public/the-wild-project', 'https://www.happyscribe.com/public/think-fast-talk-smart-communication-techniques', 'https://www.happyscribe.com/public/this-american-life', 'https://www.happyscribe.com/public/this-is-actually-happening', 'https://www.happyscribe.com/public/this-is-important', 'https://www.happyscribe.com/public/tom-brown-s-body', 'https://www.happyscribe.com/public/too-tired-to-be-crazy-with-violet-benson', 'https://www.happyscribe.com/public/unfiltered-faith', 'https://www.happyscribe.com/public/un-libro-una-hora', 'https://www.happyscribe.com/public/verbrechen-von-nebenan-true-crime-aus-der-nachbarschaft', 'https://www.happyscribe.com/public/very-presidential-with-ashley-flowers', 'https://www.happyscribe.com/public/views-with-david-dobrik-and-jason-nash', 'https://www.happyscribe.com/public/virtual-frontier', 'https://www.happyscribe.com/public/vivons-heureux-avant-la-fin-du-monde', 'https://www.happyscribe.com/public/we-study-billionaires-the-investor-s-podcast-network', 'https://www.happyscribe.com/public/where-is-george-gibney', 'https://www.happyscribe.com/public/where-the-bodies-are-buried', 'https://www.happyscribe.com/public/whoa-that-s-good-podcast', 'https://www.happyscribe.com/public/wild-til-9', 'https://www.happyscribe.com/public/wrongful-conviction-podcasts', 'https://www.happyscribe.com/public/wtf-with-marc-maron', 'https://www.happyscribe.com/public/you-and-me-both-with-hillary-clinton', 'https://www.happyscribe.com/public/you-re-wrong-about', 'https://www.happyscribe.com/public/your-mom-s-house-with-christina-p-and-tom-segura', 'https://www.happyscribe.com/public/your-undivided-attention', 'https://www.happyscribe.com/public/zack-to-the-future', 'https://www.happyscribe.com/public/zane-and-heath-unfiltered', 'https://www.happyscribe.com/public/zelfspodcast']

    # functions for scraping transcripts for an individual podcast

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
                        self.default_download_location + '/*')
                    latest_file = max(list_of_files, key=os.path.getctime)
                    latest_file_time = os.path.getmtime(latest_file)
                    if latest_file_time > download_time and latest_file[-4:] == ".pdf":
                        break
                    else:
                        time.sleep(2)
                        i += 1
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
        :return: list of episode urls on page
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

    # functions for scraping base urls for all podcasts

    def is_valid_podcast_list_page(self, url: str):
        """
        checks if url leads to page with list of links to podcast subpages
        :return: Boolean
        """
        options = webdriver.ChromeOptions()
        options.binary_location = self.chrome_binary_location
        options.headless = True

        driver = webdriver.Chrome(self.chrome_driver_binary_location, options=options)
        driver.get(url)
        text = "Sorry, we currently don't have a podcast with this category and language"
        if text in driver.page_source:
            driver.quit()
            return False
        else:
            driver.quit()
            return True

    def update_all_podcasts_urls(self):
        """
        updates the object variable all_podcast_urls
        """

        self.all_podcast_urls = self.get_all_podcast_urls()

    def get_all_podcast_urls(self):
        """
        writes list of base urls of all podcast into self.list_file_of_all_podcasts_urls and self.list_of_all_podcasts_urls
        :return:
        """
        i = 1
        urls = []
        print("current page:")
        while i > 0:
            if not self.is_valid_podcast_list_page(self.url_all_podcasts + "?page=" + str(i)):
                break
            else:
                print(i)
                urls += (self.get_podcast_urls_on_page(self.url_all_podcasts + "?page=" + str(i)))
                i += 1
        return urls

    def get_podcast_urls_on_page(self, page: str):
        """
        :return: list of podcast urls on page
        """
        options = webdriver.ChromeOptions()
        options.binary_location = self.chrome_binary_location
        options.headless = True

        driver = webdriver.Chrome(self.chrome_driver_binary_location, options=options)

        driver.get(page)
        links = []
        for podcast in driver.find_elements_by_class_name('hsp-card-podcast'):
            link = podcast.get_attribute('href')
            links.append(link)
        driver.quit()
        return links

    # other functions
    def set_base_url(self, base_url):
        self.current_base_url = base_url

    # probably unneeded
    def get_urls_of_podcast_list_pages(self):
        """
                :param base_url:  url of first page for list of podcasts
                :return: list of all url's that list podcast url's
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

