import json

from openai import OpenAI

from src.models.cv_analysis import CVAnalysis

client = OpenAI()


def analyze_cv(
    cv_text: str,
    job_description: str,
) -> str:
    response = client.responses.create(
        model="gpt-5",
        input=[
            {"role": "system", "content": "You are an ai cv assistant."},
            {
                "role": "system",
                "content": (
                    "Output example: {"
                    '"summary_assessment":"Strong backend skills.",'
                    '"resume_improvements":["max 3 suggestions, e.g., Add dates if missing"],'
                    '"areas_to_improve":["max 3 suggestions, e.g., No leadership"],'
                    '"overall_score":80'
                    "}"
                ),
            },
            {"role": "user", "content": "CV Text:\n" + cv_text},
            {"role": "user", "content": "Job Description:\n" + job_description},
        ],
    )
    return response.output_text


def run_analysis(
    cv_text: str,
    job_description: str,
) -> CVAnalysis:
    print(cv_text)
    json_str = analyze_cv(cv_text=cv_text, job_description=job_description)
    try:
        parsed_json = json.loads(json_str)
        return CVAnalysis(**parsed_json)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        print(f"JSON received: {json_str}")
        raise ValueError("Error in parsed the LLM response") from e
