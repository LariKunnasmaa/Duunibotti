from duunitori.pickle_helper import load, pickle_save
from duunitori.duunitori_functions import get_all_jobs, get_job_text

def get_job_datas():
    """
    Fetches job postings from the Duunitori website, retrieves detailed job text,
    and returns the combined job data. For more analysis
    Returns:
        list: A list of job postings with detailed information.
    """
    job_postings_list, session = get_all_jobs()
    get_job_text(job_postings_list, session)
    return job_postings_list


if __name__ == '__main__':
    save_path = "jobs.pkl"
    combined_list = get_job_datas()
    pickle_save(combined_list, save_path)
