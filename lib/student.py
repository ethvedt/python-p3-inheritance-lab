#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []
    
    def learn(self, str):
        return self.knowledge.append(str)