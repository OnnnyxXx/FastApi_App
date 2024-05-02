from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STasksAdd, STask, STaskID

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи']
)


@router.post('')
async def add_task(
        task: Annotated[STasksAdd, Depends()],
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {'Ok': True, 'task_id': task_id}


@router.get('')
async def get_tasks() -> list[STask]:
    task = await TaskRepository.find_all()
    return task
