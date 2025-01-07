from models.qp_model import SessionLocal, QuestionPaper, Question, CorrectAnswer, Option

class QuestionService:
    def __init__(self):
        self.db = SessionLocal()

    def get_question_paper(self, question_paper_id):
        return self.db.query(QuestionPaper).filter(QuestionPaper.question_paper_id == question_paper_id).first()
    
    def get_all_question_paper(self):
        return self.db.query(QuestionPaper).all()

    def create_question_paper(self, question_paper_data):
        question_paper = QuestionPaper(**question_paper_data)
        self.db.add(question_paper)
        self.db.commit()
        return question_paper

    # Question
    def get_question(self, question_id):
        return self.db.query(Question).filter(Question.question_id == question_id).first()
    

    def create_question(self, question_data):
        question = Question(**question_data)
        self.db.add(question)
        self.db.commit()
        return question

    # Option
    def get_option(self, option_id):
        return self.db.query(Option).filter(Option.option_id == option_id).first()

    def create_option(self, option_data):
        option = Option(**option_data)
        self.db.add(option)
        self.db.commit()
        return option

    # CorrectAnswer
    def get_correct_answer(self, correct_answer_id):
        return self.db.query(CorrectAnswer).filter(CorrectAnswer.question_id == correct_answer_id).first()

    def create_correct_answer(self, correct_answer_data):
        correct_answer = CorrectAnswer(**correct_answer_data)
        self.db.add(correct_answer)
        self.db.commit()
        return correct_answer
