# 📚 EduChain MCP Server

An MCP (Modular Content Provider) server built using **FastAPI** and **EduChain**, designed to expose endpoints for generating:
- 📝 Multiple Choice Questions (MCQs)
- 📖 Lesson Plans

---

## 🚀 Features

- ✅ `POST /generate-mcq`: Generate topic-specific MCQs
- ✅ `POST /generate-lesson-plan`: Generate structured lesson plans
- ✅ 🔐 Powered by OpenAI (via LangChain)
- 🧠 Smart question logic using LLM Math Chain
- The Demo video also available Demo_MCP(1)

---

## 📦 Requirements

```bash
pip install -r requirements.txt
Also set your OpenAI API key as an environment variable:

bash
Copy
Edit
export OPENAI_API_KEY="your-key-here"
Or create a .env file:

env
Copy
Edit
OPENAI_API_KEY=your-key-here
▶️ Run the Server
bash
Copy
Edit
python mcp_server.py
The server will start on http://localhost:8000

📬 API Endpoints
1. POST /generate-mcq
Generate MCQs from a topic.

Request JSON:

json
Copy
Edit
{
  "topic": "Strings",
  "num_questions": 5
}
Response:
Returns a list of MCQs with question, options, correct answer, and explanation.

2. POST /generate-lesson-plan
Generate a lesson plan from a topic.

Request JSON:

json
Copy
Edit
{
  "topic": "Strings"
}
Response:
Returns a complete structured lesson plan with:

Learning objectives

Topics and subtopics

Hands-on activities

Reflective questions

Assessments

📁 Project Structure
bash
Copy
Edit
.
├── content_generator.py      # Core logic for generating content using EduChain
├── mcp_server.py             # FastAPI server with exposed endpoints
├── requirements.txt          # Python dependencies
├── .env.example              # Sample environment file
└── demo_video.mp4            # Demo video (optional)
📽️ Demo
Check out the demo video here (link if hosted or uploaded to GitHub).

🧠 Powered By
FastAPI

EduChain

LangChain

OpenAI API

🙋‍♂️ Author
👤 Himakar Pendlimarri
📧 himashink@gmail.com
🔗 GitHub: HimaShin
