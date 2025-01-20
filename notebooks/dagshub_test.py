import mlflow
import dagshub

mlflow.set_tracking_uri('https://dagshub.com/XzisT33/end_to_end_mlops_project.mlflow')

dagshub.init(repo_owner='XzisT33', repo_name='end_to_end_mlops_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)