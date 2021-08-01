# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
import script_load
sl = script_load.script_load()
for i in range(4,8):
    sl.current_base_url= sl.all_podcast_urls[i]
    sl.current_download_location = "../downloads/"+str(i)
    sl.get_all_transcripts_of_this_podcast()

#a.set_base_url("https://www.happyscribe.com/public/lex-fridman-podcast-artificial-intelligence-ai")
#a.get_all_transcripts_of_this_podcast()
#a.get_file("https://www.happyscribe.com/public/lex-fridman-podcast-artificial-intelligence-ai/168-silvio-micali-cryptocurrency-blockchain-algorand-bitcoin-and-ethereum")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
