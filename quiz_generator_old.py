"""
Quiz generator.
name: Quiz_generator_old.py
date: 6th Feb 2020
author: Mallesha SC
"""
#Quiz_generator Function generate the quizzes as per given conditions
def Quiz_generator(input_file):
    #read the file contetnts to list using readlines method
    with open(input_file, 'r')as f:
        data = f.readlines()
    #segregate the data as per difficulty level
    easy_q = []
    med_q = []
    hard_q = []
    for question in data:
        if 'EASY' in question:
            easy_q.append(question)
        elif 'MEDIUM' in question:
            med_q.append(question)
        elif 'HARD' in question:
            hard_q.append(question)
    #quiz_list will contain all possible quizzes
    quiz_list = []
    tags = ['Tag1','Tag2','Tag3','Tag4','Tag5','Tag6']
    #while loop executes till it generates maximum possible quizzes with 6 question per quiz
    while len(quiz_list) < len(data)//10:  
        t1,t2,t3,t4,t5,t6 = False,False,False,False,False,False       
        quiz  = []  
        x = 0
        for question in easy_q:
            if tags[0] in question and not t1:
                quiz.append(question)
                easy_q.remove(question)
                t1 = True
                x+=1
            elif tags[1] in question and not t2:
                quiz.append(question)
                easy_q.remove(question)
                t2 = True
                x+=1
            if x ==2:
                break
        for question in med_q:
            if tags[2] in question and not t3:
                quiz.append(question)
                med_q.remove(question)
                t3 = True
                x+=1
            elif tags[3] in question and not t4:
                quiz.append(question)
                med_q.remove(question)
                t4 = True
                x+=1
            if x ==4 :
                break
        for question in hard_q:
            if tags[4] in question and not t5:
                quiz.append(question)
                hard_q.remove(question)
                t5 = True
                x+=1
            elif tags[5] in question and not t6:
                quiz.append(question)
                hard_q.remove(question)
                t6 = True
                x+=1
            if x ==6 :
                break
        quiz_list.append(quiz)
        #Shuffle the tags to pick questions uniformly from all difficulty levels
        tags = tags[2:] + tags[:2]
    '''                     
    At this point each quiz in quiz_list has 6 questions.
    Randomly append the remaining questions to each quiz (4 questions each)
    so the total number of questions will become 10 per quiz
    and return quiz_list, number of quizzes generated
    '''
    data = list(set(easy_q+med_q+hard_q))
    for question in quiz_list:
        question.extend(data[:4])
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
