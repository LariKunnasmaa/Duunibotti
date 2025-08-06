from duunitori.class_job import Job
from duunitori.pickle_helper import load, pickle_save
from duunitori.functions_llm import call_model
from duunitori.llm_data import remote_job_question, Question
from duunitori.class_job import Job


def call_llm(jobs_list):
    """
    Processes a list of job objects by querying a language model for each job's text.
    For each job in the provided list, this function calls the `call_model` function with a question,
    the job's text, and a remote job question. The response from the model is unpacked and assigned
    to the `remote` and `reason` attributes of the job object.
    Args:
        jobs_list (list): A list of job objects, each expected to have a `text` attribute.
    Returns:
        list: The updated list of job objects with `remote` and `reason` attributes set based on the model's response.
    """
    
    #jobs_list:list[Job] = jobs_filterin(jobs_list)
    for job in jobs_list:
        response = call_model(Question, job.text, remote_job_question())
        job.remote, job.reason = response
    return jobs_list


if __name__ == '__main__':
    jobs_list = call_llm(load())
    pickle_save(jobs_list)