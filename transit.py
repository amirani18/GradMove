from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os


def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)

def download_svg(svg_url, save_path):
    response = requests.get(svg_url)
    if response.status_code == 200:
        with open(save_path, 'w', encoding='utf-8') as file:  # Notice 'w' for writing text
            file.write(response.text)

def get_walk_score_selenium(city, state_code):
     # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Add the headless argument
    chrome_options.add_argument("--disable-gpu")  # Optional argument, recommended for headless
    service = Service(ChromeDriverManager().install())


    driver = webdriver.Chrome(service=service)
    url = f"https://www.walkscore.com/{state_code}/{city.replace(' ', '_')}"

    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        
        # Locate the element using XPath

        #walk score
        walk_score_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/img[1]"))
        )

        #map showing appts for rent 
        appt_for_rent = wait.until(
            EC.presence_of_element_located((By.XPATH, "//html/body/div[3]/div/div/div[2]/div/div[1]/a/div/div[2]/img"))
        )

        walkability_data = wait.until((
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/p[1]"))
        ))


        walkability_data2 = wait.until((
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/p[2]"))
        ))


        ret_walkability_data = walkability_data.text + " " + walkability_data2.text
        #write to file called walkability_data.txt
        with open("walkability_data.txt", "w") as file:
            file.write(ret_walkability_data)

        

        
        # Get the image URL from the 'src' attribute of the image
        image_url_walkscore = walk_score_element.get_attribute('src')
        image_url_rentapptmap = appt_for_rent.get_attribute('src')
        
        # Check if the image URL ends with '.svg' to determine the save method
        if image_url_walkscore.endswith('.svg'):
            save_path_walkscore = os.path.join(os.getcwd(), f"{city.replace(' ', '_')}_walk_score2.svg")
            download_svg(image_url_walkscore, save_path_walkscore)
        else:
            save_path_walkscore = os.path.join(os.getcwd(), f"{city.replace(' ', '_')}_walk_score2.png")
            download_image(image_url_walkscore, save_path_walkscore)

        if image_url_rentapptmap.endswith('.svg'):
            save_path_map = os.path.join(os.getcwd(), f"{city.replace(' ', '_')}_appts_to_rent.svg")
            download_svg(image_url_rentapptmap, save_path_map)
        else:
            save_path_map = os.path.join(os.getcwd(), f"{city.replace(' ', '_')}_appts_to_rent.png")
            download_image(image_url_rentapptmap, save_path_map)

        
        
        # print(f"Walk Score image for {city}, {state_code} has been downloaded to: {save_path_walkscore}")
        # print(f"Appartments for rent map for {city}, {state_code} has been downloaded to: {save_path_map}")

    except Exception as e:
        print(f"Error retrieving for {city}, {state_code}: {str(e)}")
    finally:
        driver.quit()

        
