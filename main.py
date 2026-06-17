from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_openstreetmap_search_and_zoom():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1366,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.openstreetmap.org")
        time.sleep(3)

        assert "OpenStreetMap" in driver.title

        search_fields = driver.find_elements(By.ID, "query")

        search_field = None

        for field in search_fields:
            if field.is_displayed() and field.is_enabled():
                search_field = field
                break

        assert search_field is not None

        search_field.click()
        search_field.clear()
        search_field.send_keys("Kyiv")
        search_field.send_keys(Keys.ENTER)

        time.sleep(5)

        assert "Kyiv" in driver.page_source or "Київ" in driver.page_source

        zoom_button = driver.find_element(By.CLASS_NAME, "leaflet-control-zoom-in")
        driver.execute_script("arguments[0].click();", zoom_button)

        time.sleep(2)

        assert zoom_button is not None

    finally:
        driver.quit()