from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from educhain.engines import QnAEngine, ContentEngine
from dotenv import load_dotenv
import uvicorn

load_dotenv()


app = FastAPI()
qna_engine = QnAEngine()
content_engine = ContentEngine()

# Request body for MCQ generation
class MCQRequest(BaseModel):
    topic: str
    num_questions: int = 5

# Request body for Lesson Plan generation
class LessonPlanRequest(BaseModel):
    topic: str

@app.post("/generate-mcq")
def generate_mcq(request: MCQRequest):
    try:
        result = qna_engine.generate_mcq_math(request.topic, request.num_questions)
        return result.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-lesson-plan")
def generate_lesson_plan(request: LessonPlanRequest):
    try:
        result = content_engine.generate_lesson_plan(request.topic)
        return result.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("mcp_server:app", host="0.0.0.0", port=8000, reload=True)
