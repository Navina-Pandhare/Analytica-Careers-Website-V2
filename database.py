from sqlalchemy import create_engine, text
import os

# Connect to the database
engine = create_engine(os.environ['DB_CONNECTION_STRING'])

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))

    jobs = []
    for row in result.mappings().all():
      jobs.append(dict(row))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val" : id})
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])


  


  


