from pydantic import BaseModel
from typing import List


class CVAnalysis(BaseModel):
    summary_assessment: str
    resume_improvements: List[str]
    areas_to_improve: List[str]
    overall_score: int
