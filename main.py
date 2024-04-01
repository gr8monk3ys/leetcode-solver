from bot import *
from time import *
import Random
from openai import OpenAI


if __name__ == '__main__':
    bot = LeetcodeBot()
    driver = webdriver.Firefox()
    try:
        email, password = bot.get_credentials()
        bot.login(email, password, driver)
        
        bot.click_play(driver)
        time_start = time()
        sleep(2)
        time_elapsed = time() - time_start

        soup = bot.get_html(driver)
        select_random(driver)

        sleep(2)

        url = get_problem(driver)
        code = get_code(driver)
        sleep(1)
        
        llm_client = OpenAI()
        solve(driver, url, code, llm_client)
        sleep(3)
        submit()

        time_elapsed = time() - time_start

    except Exception as e:
        print(f"Error encountered: {e}")
        bot.closedriver()

sleep(3)
bot.closedriver(driver)