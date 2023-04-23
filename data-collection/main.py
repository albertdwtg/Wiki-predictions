import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import glob
from variables import DOWNLOAD_PATH
from typing import List


root = os.path.dirname(os.path.dirname(__file__))
driver_path = os.path.join(root, "chromedriver")
storage_path = os.path.join(root, "data-storage")
storage_path = os.path.join(storage_path, "raw")
print(storage_path)


def collect_affluence_stats(pages: List[str]):
    """Function to collect affluence stats about multiple pages

    Args:
        pages (list[str]): list of pages we want to study
    """

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(driver_path, options=options)

    for page in pages:
        driver.get("https://pageviews.wmcloud.org/pageviews/?project=en.wikipedia.org&platform=all-access&agent=user&redirects=0&range=all-time&pages={}".format(page))
        # Maximize the window and let code stall
        driver.maximize_window()
        time.sleep(2)
        # Obtain button by class name and click.
        button = driver.find_elements(By.CLASS_NAME, "caret")
        # open dropdown
        button[4].click()
        time.sleep(1)
        # click on download button
        button2 = driver.find_element(By.CLASS_NAME, "download-csv")
        button2.click()
        time.sleep(2)

        list_of_files = get_sorted_files_from_directory(DOWNLOAD_PATH)
        # get last file of downloads
        last_download = list_of_files[-1]

        # move file in another folder
        target_path = storage_path + "/" + page + ".csv"
        if os.path.exists(target_path):
            os.remove(target_path)
        os.replace(last_download, target_path)


def get_sorted_files_from_directory(directory: str) -> List[str]:
    """Get all file from a specific directory, sorted by time they have been added

    Args:
        directory (str): directory path we want to study

    Returns:
        list[str]: list of directory of files sorted by date
    """

    # Get list of all files only in the given directory
    print(directory + r"\*")
    list_of_files = filter(os.path.isfile,
                           glob.glob(directory + r'\*'))

    # Sort list of files based on last modification time in ascending order
    list_of_files = sorted(list_of_files,
                           key=os.path.getmtime)

    return list_of_files


collect_affluence_stats(["Manchester_United_Football_Club"])
