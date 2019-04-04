'''
QReader - QPGen v1.0
    This module perfoms Read operation for Questions and their attributes from target file.
'''

import os
import json

class QReader():
    def __init__(self, filename):
        self.filename = filename
        try:
            with open("QList.json") as QList:
                self.data = json.load(QList)
        except:
            print("Error: Reading data from file failed.")

    def read_total(self):
        return self.data["total"]

    def read_questions(self, difficulty):
        questions = self.data['questions']
        questions = list(filter(lambda x: x["difficulty"] == difficulty, questions))
        return questions

    def read_maxmarks(self):
        return self.data["maxMarks"]

    def read_level(self, difficulty):
        return self.data["level"][difficulty]
        