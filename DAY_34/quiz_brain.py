import html
import requests

class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = []  # Initialize question_list as an empty list
        self.current_question = None
        self.parameters = {
            "amount": 20,
            "type": "boolean",
            "category": 18  
        }

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question[0])
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer):
        correct_answer = self.current_question[1]
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def new_qlist(self):
        try:
            self.question_list = []  # Clear existing questions
            # Constructing the API endpoint URL using parameters
            url = "https://opentdb.com/api.php"
            response = requests.get(url, params=self.parameters)
            response.raise_for_status()
            data = response.json()
            if "results" in data:
                self.question_data = data["results"]
                for question in self.question_data:
                    question_text = html.unescape(question["question"])
                    question_answer = html.unescape(question["correct_answer"])
                    self.question_list.append((question_text, question_answer))
            else:
                print("No results found in the response:", data)
        except requests.exceptions.RequestException as e:
            print("Error fetching questions:", e)  # Append new questions to question_list
