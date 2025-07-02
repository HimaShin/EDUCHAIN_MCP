# content_generator.py

from educhain.engines import QnAEngine
from educhain.models import LessonPlan

from dotenv import load_dotenv
load_dotenv()

# MCQ Generator
def generate_mcqs(topic="Linear Equations", num_questions=5):
    engine = QnAEngine()
    mcqs = engine.generate_mcq_math(topic, num_questions)
    return [q.dict() for q in mcqs.questions]


# Lesson Plan Generator (simplified)

# from educhain.models import LessonPlan

def get_lesson_plan(subject="Algebra"):
    def build_subtopic(title, desc):
        return {
            "title": title,
            "description": desc,
            "key_concepts": [{
                "type": "definition",
                "title": f"{title} Concept",
                "content": f"Core concept of {title}"
            }],
            "discussion_questions": [{
                "question": f"What is the significance of {title} in {subject}?"
            }],
            "hands_on_activities": [{
                "title": f"{title} Activity",
                "description": f"Do a practical activity about {title}"
            }],
            "reflective_questions": [{
                "question": f"How can {title} be applied in real life?"
            }],
            "assessment_ideas": [{
                "type": "quiz",
                "description": f"Short quiz on {title}"
            }]
        }

    return LessonPlan(
        title=f"Introduction to {subject}",
        subject=subject,
        learning_objectives=[
            "Understand the fundamentals",
            "Solve example problems",
            "Apply concepts in real scenarios"
        ],
        lesson_introduction=f"This lesson covers the basics of {subject}.",
        main_topics=[
            {
                "title": f"Core concepts of {subject}",
                "description": "Detailed explanation of concepts",
                "subtopics": [
                    build_subtopic("Terminology", "Key terms and their meanings"),
                    build_subtopic("Examples", "Worked-out examples"),
                    build_subtopic("Formulas", "Common formulas used")
                ]
            },
            {
                "title": "Practice problems",
                "description": "Step-by-step solutions",
                "subtopics": [
                    build_subtopic("Level 1", "Basic problems"),
                    build_subtopic("Level 2", "Intermediate problems"),
                    build_subtopic("Challenge", "Advanced problems")
                ]
            }
        ]
    ).model_dump()




if __name__ == "__main__":
    print("Sample MCQs:")
    for q in generate_mcqs("Python Loops"):
        print(q)

    print("\nLesson Plan:")
    print(get_lesson_plan("Algebra"))
