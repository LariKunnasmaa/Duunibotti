import re
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Job:
    """
    Represents a job posting extracted from duunitori.
    Attributes:
        title (str): The title of the job.
        company (str): The company offering the job.
        link (str): The URL link to the job posting.
        text (str): Additional text or description for the job.
        release (str): The release date of the job posting.
        end_date (str): The end date for the job posting.
        remote (str): Indicates if the job is remote.
        reason (str): The reason for the job posting or status.
    Methods:
        __init__(job_elem: WebElement):
            Initializes a Job instance from a given web element.
        _get_release_date(job_elem: WebElement) -> str:
            Extracts and returns the release date from the job element.
    """


    def __init__(self, job_elem:WebElement):
        self.title: str = job_elem.get_attribute("text")
        self.company: str = job_elem.get_attribute("data-company")
        self.link: str = job_elem.get_attribute("href")
        self.text: str = ""
        self.release: str = self._get_release_date(job_elem)
        self.end_date: str = ""
        self.remote: str = ""
        self.reason: str = ""
        

    def _get_release_date(self, job_elem:WebElement):
        date_text = job_elem.find_element(By.XPATH, "//*[@class= 'job-box__job-posted']").text
        date = re.findall(r"\d+\.\d+", date_text)[0]
        return date

