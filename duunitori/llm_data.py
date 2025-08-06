from pydantic import BaseModel, Field
from typing import Optional

def remote_job_question():
    """Generates a question for the language model to determine if a job is fully remote.
    Returns:
        str: A question that prompts the model to analyze job descriptions for remote work options.
    """
    return  "You are a helpful assistant that determines whether a job description has remote as the only option. " \
            "Hybrid does not count. " \
            "If there is any mention of office needed then it is not remote Always respond with a justification."

class Question(BaseModel):
    """A model representing a question to be asked to the language model."""
    sta:bool= Field( 
        default=..., description="Is the job a fully remote job?")
    justification: Optional[str] = Field(
        default=..., description="Explain is the job a fully remote job?"
    )

