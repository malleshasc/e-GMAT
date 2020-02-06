"""
Quiz generator.
name: Quiz_generator.py
date: 6th Feb 2020
author: Mallesha SC
"""
import random 

def Quiz_generator(input_file):
    #read the file contetnts to list using readlines method
    with open(input_file, 'r')as f:
        data = f.readlines()
    data = list(set(data))   
    quiz_list = []
    data_len = len(data)//10
    #while loop executes till it generates maximum possible quizzes with 6 question per quiz
    while len(quiz_list) < data_len:
        quiz = []
        tags = []
        diff_dict = {'EASY':0,'MEDIUM':0,'HARD':0}
        while len(quiz)<6:  
            question = random.choice(data)
            tag_id,diff_id = question.split('|')[2],question.split('|')[1]
            if tag_id not in tags and diff_dict[diff_id]!=2:
                quiz.append(question)
                data.remove(question)
                tags.append(tag_id)
                diff_dict[diff_id] += 1
        quiz_list.append(quiz)
    data = list(set(data))   
    for quiz in quiz_list:
        quiz.extend(data[:4])
        data = data[4:]
    return quiz_list,len(quiz_list)

def main():
    file_name = input("Please enter the input file name:")
    if file_name=='':
        print("You haven't entered input filename, default file 1.txt has been taken")
        file_name='1.txt'
    quizzes,no_of_quiz = Quiz_generator(file_name)
    print('----------------------------------------')
    print("Valid quizzes generated:",no_of_quiz)     
    print('----------------------------------------')             

if __name__ == '__main__':
    main()
