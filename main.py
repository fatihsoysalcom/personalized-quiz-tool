import random

# Define questions with topics, mimicking PSM I exam areas
questions = [
    {"id": 1, "topic": "Scrum Roles", "question": "Who is responsible for maximizing the value of the product resulting from the work of the Development Team?", "options": ["A. Scrum Master", "B. Product Owner", "C. Development Team", "D. Stakeholder"], "correct": "B"},
    {"id": 2, "topic": "Scrum Roles", "question": "Who facilitates Scrum events as requested or needed?", "options": ["A. Product Owner", "B. Development Team", "C. Scrum Master", "D. Project Manager"], "correct": "C"},
    {"id": 3, "topic": "Scrum Events", "question": "What is the time-box for a Daily Scrum?", "options": ["A. 30 minutes", "B. 15 minutes", "C. 1 hour", "D. As long as needed"], "correct": "B"},
    {"id": 4, "topic": "Scrum Events", "question": "When does the Sprint Retrospective occur?", "options": ["A. Before the Sprint Review", "B. After the Sprint Review and before the next Sprint Planning", "C. During the Sprint", "D. At the beginning of the Sprint"], "correct": "B"},
    {"id": 5, "topic": "Scrum Artifacts", "question": "Which Scrum Artifact provides transparency into the work the Development Team plans to accomplish during the Sprint?", "options": ["A. Product Backlog", "B. Sprint Backlog", "C. Increment", "D. Burndown Chart"], "correct": "B"},
    {"id": 6, "topic": "Scrum Artifacts", "question": "What does the Product Backlog list?", "options": ["A. All tasks for the current Sprint", "B. All features, functions, requirements, enhancements, and fixes that constitute the changes to be made to the product in future releases", "C. The work completed in the last Sprint", "D. Impediments"], "correct": "B"},
    {"id": 7, "topic": "Empiricism", "question": "What are the three pillars of Empiricism?", "options": ["A. Planning, Execution, Review", "B. Transparency, Inspection, Adaptation", "C. Analysis, Design, Implementation", "D. Vision, Strategy, Tactics"], "correct": "B"},
    {"id": 8, "topic": "Empiricism", "question": "Which Scrum event is primarily for Inspection and Adaptation of the Product Backlog?", "options": ["A. Daily Scrum", "B. Sprint Review", "C. Sprint Retrospective", "D. Sprint Planning"], "correct": "B"},
]

# Initialize weakness scores for each topic. Higher score means more weakness.
topic_weakness = {topic: 0 for topic in set(q["topic"] for q in questions)}

# Keep track of asked questions to avoid repetition in a single session
asked_question_ids = set()

def get_next_question(current_topic_weakness, available_questions):
    """
    Selects the next question based on topic weakness.
    Prioritizes topics with higher weakness scores.
    """
    # Sort topics by weakness score in descending order
    sorted_topics = sorted(current_topic_weakness.items(), key=lambda item: item[1], reverse=True)

    for topic, _ in sorted_topics:
        # Find available questions for the current weakest topic that haven't been asked yet
        possible_questions = [q for q in available_questions if q["topic"] == topic and q["id"] not in asked_question_ids]
        if possible_questions:
            return random.choice(possible_questions) # Pick a random one from the weakest topic

    # If all questions from weakest topics have been asked, pick any remaining available question
    remaining_questions = [q for q in available_questions if q["id"] not in asked_question_ids]
    if remaining_questions:
        return random.choice(remaining_questions)

    return None # No more questions

def run_quiz():
    print("Welcome to the Personalized PSM I Practice Tool!")
    print("Answer questions to help the tool identify your weak areas.")
    print("Type 'exit' to quit at any time.\n")

    score = 0
    total_questions_asked = 0

    while True:
        question_to_ask = get_next_question(topic_weakness, questions)

        if not question_to_ask:
            print("\nAll available questions have been asked! Good job!")
            break

        print(f"\n--- Topic: {question_to_ask['topic']} ---")
        print(f"Question: {question_to_ask['question']}")
        for opt in question_to_ask['options']:
            print(f"  {opt}")

        user_answer = input("Your answer (A, B, C, D): ").strip().upper()

        if user_answer == 'EXIT':
            break

        asked_question_ids.add(question_to_ask['id'])
        total_questions_asked += 1

        if user_answer == question_to_ask['correct']:
            print("Correct!\n")
            score += 1
            # CONCEPT: Decrease weakness for this topic on correct answer
            topic_weakness[question_to_ask['topic']] = max(0, topic_weakness[question_to_ask['topic']] - 1)
        else:
            print(f"Incorrect. The correct answer was {question_to_ask['correct']}.\n")
            # CONCEPT: Increase weakness for this topic on incorrect answer
            topic_weakness[question_to_ask['topic']] += 2 # Using +2 to make the impact more noticeable

        print("Current Topic Weakness Scores (higher means weaker):")
        for topic, weakness in sorted(topic_weakness.items(), key=lambda item: item[1], reverse=True):
            print(f"  {topic}: {weakness}")

    print(f"\n--- Quiz Ended ---")
    print(f"You answered {score} out of {total_questions_asked} questions correctly.")
    print("Final Topic Weakness Scores:")
    for topic, weakness in sorted(topic_weakness.items(), key=lambda item: item[1], reverse=True):
        print(f"  {topic}: {weakness}")

if __name__ == "__main__":
    run_quiz()
