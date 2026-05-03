from pydantic import BaseModel


class TodoSchema(BaseModel):
    text : str
    completed : bool

    