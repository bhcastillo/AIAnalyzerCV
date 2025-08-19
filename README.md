# AIAnalyzerCV

AIAnalyzerCV is a project built with **FastAPI** and powered by **GPT-5** to analyze and improve CVs (resumes) instantly.  
It uses **Uvicorn** as the ASGI server.

## Prerequisites
- Python 3.8+
- pip (Python package manager) (23.0.1)
- (Optional) [virtualenv](https://virtualenv.pypa.io/) or [venv](https://docs.python.org/3/library/venv.html) for virtual environments

## Installation

1. 
   ```bash
   git clone https://github.com/your-username/AIAnalyzerCV.git
   cd AIAnalyzerCV
   ```
2. ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. ```bash
   pip install -r requirements.txt 
   ```
4. ```bash
   uvicorn main:api --reload 
   ```
   <img width="1309" height="326" alt="image" src="https://github.com/user-attachments/assets/b8d274ae-877e-4142-b280-d336867cb0c6" />
5. Start the frontend [AIAnalyzerCV_frontend](https://github.com/bhcastillo/AIAnalyzerCV_frontend)
