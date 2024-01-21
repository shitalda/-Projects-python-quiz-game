class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_num):
        question = self.questions[question_num]["question"]
        options = self.questions[question_num]["options"]
        print(f"\n{question}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        user_answer = input("Your answer (enter the option number): ")
        return int(user_answer)

    def check_answer(self, question_num, user_answer):
        correct_answer = self.questions[question_num]["correct_answer"]
        if user_answer  == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            correct_option = correct_answer + 1
            print(f"Wrong! The correct answer is {correct_option}.")

    def run_quiz(self):
        for i in range(len(self.questions)):
            user_answer = self.display_question(i)
            self.check_answer(i, user_answer)

        print(f"\nYour final score is: {self.score}/{len(self.questions)}")


def main():
    # Example quiz questions
    quiz_questions = [
        {
            "question": "1.Who is the father of our nation?",
            "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "D.B.R Ambedkar", "Lokmanya Tilak"],
            "correct_answer": 2
        },
        {
            "question": "2.Who was the first Prime Minister of India?",
            "options": ["Pruthviraj Chavhan ", "Indira Gandhi", "Jawaharlal Nehru", "Narendra Modi"],
            "correct_answer": 3
        },
       
        {
            "question": "3.Smallest state of India is?",
            "options": ["Kerala", "Aassam", "Sikkim", "Goa"],
            "correct_answer": 4
        },
         {
            "question": "4.India lies in which continent?",
            "options": ["Asia", "Australia", "Africa", "Arctic"],
            "correct_answer": 1
        },
         {
            "question": "5.Gateway of India is located at?", 
            "options": ["Hydrabad", "Chennai", "Mumbai", "Dehli"],
            "correct_answer": 3
        },
         {
            "question": "6.What is the capital of Uttarakhand?",
            "options": ["Bhopal", "Dehradun", "Lucknow", "Raipur"],
            "correct_answer": 2
        },
         {
            "question": "7.Who was the author of Ramayana?",
            "options": ["Valmiki", "Ved Vyas", "Amisha Tripathi", "R.K.Narayan"],
            "correct_answer": 1
        },
       {
            "question": "8.Which one of the seven wonders is located in India? ",
            "options": ["Statue of Liberty", "Golden Temple", "Konark Sun Temple", "Taj Mahal"],
            "correct_answer": 4
        },
        {
            "question": "9.Which festival in India is called the festival of colours? ",
            "options": ["Dussehra", "Holi", "Diwali", "Pongal"],
            "correct_answer": 2
        },
        {
            "question": "10.Which city is called the Pink City in India? ",
            "options": ["Nagpur","Jodhpur", "Jaipur","Udaipur"],
            "correct_answer": 4
        },
         
        
    ]

    # Create and run the quiz 
    my_quiz = Quiz(quiz_questions)
    my_quiz.run_quiz()


if __name__ == "__main__":
   main()
        