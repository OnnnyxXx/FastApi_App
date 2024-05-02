from sqlalchemy import select

from database import new_session, TasksORM
from schemas import STasksAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STasksAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> [STask]:
        async with new_session() as session:
            query = select(TasksORM)
            result = await session.execute(query)
            task_model = result.scalars().all()
            task_schemes = [STask.model_validate(task_model) for i in task_model]
            return task_schemes
