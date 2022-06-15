from instafollower import InstaFollower

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "xxx"
USERNAME = "xxx"
PASSWORD = "xxx"

bot = InstaFollower(CHROME_DRIVER_PATH)

bot.accept_cookies()
bot.login(USERNAME, PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT)
bot.follow()


# bot.driver.quit()