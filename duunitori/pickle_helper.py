import pickle
from duunitori.class_job import Job 

def pickle_save(my_data, path ="jobs.pkl" ):   
    with open("jobs.pkl", "wb") as f:
        pickle.dump(my_data, f)

def load( path = "jobs.pkl"):
    with open(path, "rb") as f:
        loaded_data = pickle.load(f)
    return loaded_data