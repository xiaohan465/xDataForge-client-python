from .api_client import xDataForge
from typing import List

def process_data(client: xDataForge, project_name: str, plan_name: str) -> List[float]:
    project = client.get_project(project_name)
    if not project:
        raise ValueError("project not found")

    plan = client.get_plan(project.id, plan_name)
    if not plan:
        raise ValueError("plan not found")

    run_info = client.create_run(plan.id)
    results = []
    for task in run_info.tasks:
        checkpoint = client.get_task_checkpoint(task.id)
        result = compute_result(checkpoint)
        client.update_task(task.id, {'result': result})
        results.append(result)

    return results

def compute_result(checkpoint: float) -> float:
    # 这里添加具体的计算逻辑
    return checkpoint * 2  # 示例计算