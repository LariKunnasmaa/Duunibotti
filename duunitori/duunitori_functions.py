from .class_session import init_session
from .pickle_helper import load, pickle_save
from .class_session import SeleniumSession
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from .class_job import Job

def generate_search_url(page):
    """
    Generates a search URL query string for job listings based on the specified page number.
    Args:
        page (int or str): The page number to include in the search query.
    Returns:
        str: A URL-encoded query string with predefined search parameters for job type, relation, and keyword.
    Example:
        >>> generate_search_url(2)
        'haku=python&filter_work_type=full_time&filter_work_relation=permanent&sivu=2'
    """

    haku_dict = {"haku": "python",
                 "filter_work_type": "full_time",
                 "filter_work_relation": "permanent",
                 "sivu": str(page)}
    return "&".join(["".join(v + "=" + i) for v, i in haku_dict.items()])

def get_page_jobs(session:SeleniumSession, last_page):
    """
    Fetches job postings from multiple pages and returns a combined list of Job objects.
    Args:
        session (Selenium_session): An active Selenium session used to interact with the web pages.
        last_page (int or str): The last page number to fetch job postings from.
    Returns:
        list: A list of Job objects collected from all specified pages.
    Notes:
        - For each page from 1 to last_page (inclusive), the function navigates to the corresponding URL,
          extracts up to 20 job elements, and creates Job objects from them.
        - The function relies on the presence of a `generate_search_url` function and a `Job` class.
    """
    combined_list = []
    for i in range(1,int(last_page)+1):
        session.open_url("https://duunitori.fi/tyopaikat?"+generate_search_url(i))
        #We know that there are 20 jobs per page, rest are ads
        jlist = session.xpaths("//*[contains(@class, 'grid grid--middle job-box')]/a")[:20]
        combined_list.extend([Job(job) for job in jlist])
    return combined_list

def get_all_jobs():
    """
    Fetches all job listings from the Duunitori website.
    Uses the last page number to determine how many pages to scrape.
    Returns:
        tuple: A tuple containing:
            - combined_list (list): A list of all job postings retrieved.
            - session (Selenium_session): The Selenium session used for scraping.
    """
    
    session:SeleniumSession = init_session()
    session.open_url("https://duunitori.fi/tyopaikat?"+generate_search_url(1))
    combined_list:list[Job] = []
    last_page:str = session.xpaths('//*[@class= "pagination__pagenum "]')[-1].text
    combined_list = get_page_jobs(session, last_page)
    return combined_list, session


def get_job_text(combined_list: list[Job], session: SeleniumSession):
    """
    Fetches the detailed text and end date for each job in the combined list.
    Args:
        combined_list (list[Job]): A list of Job objects for which to fetch details.
        session (Selenium_session): An active Selenium session used to interact with the web pages.
    """
    for job in combined_list:
        session.open_url(job.link)
        job.text = session.xpath('//div[@class="description-box"]').text
        job.end_date = session.xpath("//*[contains(text(), 'Julkaistu ') or contains(text(), 'Published ')]/following-sibling::span").text
