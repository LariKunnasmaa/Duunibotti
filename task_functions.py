from duunitori.pickle_helper import pickle_save, load
from duunitori.class_job import Job
from duunitori.duunitori_functions import get_all_jobs, get_job_text
from duunitori.class_session import SeleniumSession


def get_job_datas():
    """
    Fetches job postings from the Duunitori website, retrieves detailed job text,
    and returns the combined job data. For more analysis
    Returns:
        list: A list of job postings with detailed information.
    """
    job_postings_list: list[dict]
    session: SeleniumSession
    job_postings_list, session = get_all_jobs()
    get_job_text(job_postings_list, session)
    return job_postings_list