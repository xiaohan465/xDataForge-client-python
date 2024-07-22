from typing import Optional
from .api_client import APIClient
import requests

from .models import Project, Plan, Run, Task


class XDataForge:
    pass


class XDataForge:
    api_client: APIClient
    project: Project
    plan: Plan
    run_id: str

    def __init__(self, base_url: str, api_token: str):
        self.api_client = APIClient(base_url, api_token)

    def setup(self, project_name: str, plan_name: str, run_id: str = ""):
        path = f'project/{project_name}'
        project = self.api_client.get(path)
        self.project = Project(**project)
        path = f'plan/{plan_name}'
        plan =  self.api_client.get(path, {'project_id': self.project.id})
        self.plan = Plan(id=plan['id'],name=plan['name'])
        if run_id == "":
            run_id = self.create_run()
        self.run_id = run_id
        return self

    def create_run(self) -> str:
        path = 'run'
        run = self.api_client.post(path, {'plan_id': self.plan.id})
        return run['name']

    # find run by id
    def fetch_tasks(self):
        path = f'run/{self.run_id}/tasks'
        tasks = self.api_client.get(path)['items']
        return [Task(id=task['id'],dataset_id=task['checklist']['dataset']['id'],
                     last_checkpoint_id=task['last_checkpoint_id'],api_client=self.api_client) for task in tasks]


