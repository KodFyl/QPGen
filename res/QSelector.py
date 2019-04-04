'''
QSelector - QPGen v1.0
    This module selects the questions based on their required weight.
'''

from res.QReader import QReader
import random

class QSelector():
    
    def __init__(self):
        pass
    
    def select(self, levelName, levelMark):

        self.reader = QReader("QList.json")
        questions = self.reader.read_questions(levelName)

        while( True ):

            tempMark = 0
            tempQuestions = random.sample(questions, random.randint(1, len(questions)))
            for ques in tempQuestions:
                tempMark += ques["marks"]
            
            if(tempMark == levelMark):
                return tempQuestions
            
