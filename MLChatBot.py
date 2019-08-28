from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


bot = ChatBot("ChatBot")

trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

browser = webdriver.Firefox(executable_path=r"C:\Users\Vpc\Desktop\geckodriver")
browser.get("http://cleverbot.com")
time.sleep(4)

while True:
        for x in browser.find_elements_by_xpath('.//span[@class="bot"]'):
            clever = x.text
        time.sleep(1)
        response = bot.get_response("Hi there")
        request = browser.find_element_by_name("stimulus")
        time.sleep(1)
        request.send_keys(str(response))
        request.send_keys(Keys.RETURN)
        time.sleep(1)
        print("Clever :",clever)
        print("Ben :", response)