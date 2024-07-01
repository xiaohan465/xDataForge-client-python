from dataclasses import dataclass
from typing import List, Optional

from xdataforge.api_client import APIClient


@dataclass
class Project:
    id: int
    name: str
    description: str
    user_id: int
    created_at: int
    updated_at: int


@dataclass
class Plan:
    id: int
    name: str


@dataclass
class Datapoint:
    id: int
    input: str
    expected_output: str


@dataclass
class Task:
    id: int
    dataset_id: int
    last_checkpoint_id: int
    api_client: APIClient
    current_datapoint: Optional[Datapoint] = None

    def fetch_next_datapoint(self) -> Datapoint:
        path = f'datapoint/{self.last_checkpoint_id}/next'
        print(path)
        datapoint = self.api_client.get(path, {"task_id": self.id})
        self.last_checkpoint_id = datapoint['id']
        self.current_datapoint = Datapoint(id=datapoint['id'], input=datapoint['input'],
                                           expected_output=datapoint['expected_output'])
        yield self.current_datapoint

    def commit_result(self, result):
        path = f'datapoint/{self.current_datapoint.id}/commit'
        self.api_client.post(path, {"task_id": self.id, "output": result, "input": self.current_datapoint.input,
                                    "expected_output": self.current_datapoint.expected_output})

#todo update task status to done

@dataclass
class Run:
    tasks: List[Task]
