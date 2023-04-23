from main import get_sorted_files_from_directory, collect_affluence_stats
#from variables import DOWNLOAD_PATH
from typing import List
import random
import os

DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH")
print(DOWNLOAD_PATH)

def test_return_type_get_sorted_files():
    list_of_files = get_sorted_files_from_directory(DOWNLOAD_PATH)
    assert isinstance(list_of_files, list)
    
def test_return_get_sorted_files_empty():
    list_of_files = get_sorted_files_from_directory(DOWNLOAD_PATH)
    assert len(list_of_files)>0

def test_get_sorted_files_returns_strings():
    list_of_files = get_sorted_files_from_directory(DOWNLOAD_PATH)
    numb = random.randint(0, len(list_of_files))
    assert isinstance(list_of_files[numb], str)
    