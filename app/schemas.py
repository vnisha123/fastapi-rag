from pydantic import BaseModel, ConfigDict
from datetime import datetime

class DocumentResponse(BaseModel):
    id: int
    filename: str
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)


class QueryRequest(BaseModel):
    question: str
    document_id: int


class QueryResponse(BaseModel):
    question: str
    answer: str
    source_chunks_used: list[int]

