from task_data_retival import get_job_datas
from task_excel_formatting import excel_mani
from task_llm_call import call_llm



"""
This script orchestrates the retrieval, processing, and storage of job data.
Workflow:
1. Retrieves job data using `get_job_datas` from `task_data_retival`.
2. Processes the job data using a language model via `call_llm` from `task_llm`.
3. Manipulates and stores the processed job data in an Excel file using `excel_mani` from `task_excel`.
Modules:
- task_data_retival: Provides the `get_job_datas` function to fetch job data.
- task_llm: Provides the `call_llm` function to process job data with a language model.
- task_excel: Provides the `excel_mani` function to handle Excel file operations.
Entry Point:
- The script executes the workflow when run as the main module.
"""

if __name__ == '__main__':
    jobs_list =  get_job_datas()
    jobs_list = call_llm(jobs_list)
    excel_mani(jobs_list)
