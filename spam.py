from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

def submit_survey(url, text1, text2, text3):
    # Setup Firefox
    options = Options()
    options.add_argument("-profile")
    options.add_argument("/home/bikisser/snap/firefox/common/.mozilla/firefox/illslh6c.selenium-profile")
    driver = webdriver.Firefox(options=options)
    
    try:
        # Navigate to the survey page
        driver.get(url)
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        
        # Find all radio buttons
        radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
        
        # Select first option for first 5 questions (5 options per question)
        for i in range(5):
            index = i * 5  # First option in each question
            radio_buttons[index].click()
        
        # Select third option for final 8 questions (3 options per question)
        for i in range(5, 13):
            index = (5 * 5) + ((i - 5) * 3) + 2  # Third option index
            radio_buttons[index].click()
        
        # Find and fill the three text fields
        text_fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text'], textarea")
        
        if len(text_fields) >= 3:
            text_fields[0].send_keys(text1)
            text_fields[1].send_keys(text2)
            text_fields[2].send_keys(text3)
        
        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")
        submit_button.click()
        
        # Wait for submission to complete
        time.sleep(2)
        
        return True
    
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    
    finally:
        # Close the browser
        driver.quit()

# Main infinite loop
def main():
    # Replace with your survey URL
    survey_url = "https://secured.heritage.org/the-heritage-doge-survey/"
    
    # Your three text strings
    text_string_1 = ["Suck my tranny gock", "TRANS RIGHTS ARE HUMAN RIGHTS", "Free Bottom Suregery at ur moms house"]
    text_string_2 = ["I love giving puberty blockers to queer children", "I love pride parades", "NEVER BACK DOWN NEVER WHAT?"]
    text_string_3 = ["ExplodeInsideMe@freeboipussy.com", "tgirlDickNearYou@gayness.com", "GAWKGAWKGAWK@ICANFEELYOUEXPLODINGINSIDEOFMEEEEE.COM"]
    
    counter = 1
    
    # Run infinitely
    while True:
        print(f"Submission attempt #{counter}")
        success = submit_survey(survey_url, random.choice(text_string_1), random.choice(text_string_2), random.choice(text_string_3))
        
        if success:
            print(f"Submission #{counter} successful")
        else:
            print(f"Submission #{counter} failed")
        
        counter += 1
        
        # Small delay between submissions (can be adjusted)
        time.sleep(3)

if __name__ == "__main__":
    main()
