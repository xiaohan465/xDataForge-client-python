import json
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


class Datapoint:
    id: int
    input: dict

    def __init__(self, id, input):
        self.id = id
        self.input = json.loads(input)


@dataclass
class Task:
    id: int
    dataset_id: int
    last_checkpoint_id: int
    api_client: APIClient
    current_datapoint: Optional[Datapoint] = None
    def fetch_next_datapoint(self) -> Datapoint:  # generator
        while True:
            try:
                path = f'datapoint/{self.last_checkpoint_id}/next'
                datapoint = self.api_client.get(path, {"task_id": self.id})
                self.last_checkpoint_id = datapoint['id']
                self.current_datapoint = Datapoint(id=datapoint['id'], input=datapoint['input'])

                yield self.current_datapoint
            except Exception as e:
                break

    def commit_result(self, result: dict):
        if not isinstance(result, dict):
            raise ValueError("result should be a dict")
        path = f'datapoint/{self.current_datapoint.id}/commit'
        self.api_client.post(path,
                             {
                                 "task_id": self.id,
                                 "output" : json.dumps(result),
                                 "input"  : json.dumps(self.current_datapoint.input)}
                             )


# todo update task status to done

@dataclass
class Run:
    tasks: List[Task]
