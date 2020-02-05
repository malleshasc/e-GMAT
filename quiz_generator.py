
def Quiz_generator(input_file):
    with open(input_file, 'r')as f:
        data = f.readlines()
#data = ''' Q1 | EASY | tag1'''

    easy_q = []
    med_q = []
    hard_q = []
    
    for i in data:
        if 'EASY' in i:
            easy_q.append(i)
        elif 'MEDIUM' in i:
            med_q.append(i)
        elif 'HARD' in i:
            hard_q.append(i)
        
    n = len(data)//10
    quiz_list = []
    a = ['Tag1','Tag2','Tag3','Tag4','Tag5','Tag6']
    
    while len(quiz_list) < n:  
        t1,t2,t3,t4,t5,t6 = False,False,False,False,False,False       
        quiz  = []  
        x = 0
        for i in easy_q:
            if a[0] in i and not t1:
                quiz.append(i)
                easy_q.remove(i)
                t1 = True
                x+=1
            elif a[1] in i and not t2:
                quiz.append(i)
                easy_q.remove(i)
                t2 = True
                x+=1
            if x ==2:
                break
        for i in med_q:
            
            if a[2] in i and not t3:
                quiz.append(i)
                med_q.remove(i)
                t3 = True
                x+=1
            elif a[3] in i and not t4:
                quiz.append(i)
                med_q.remove(i)
                t4 = True
                x+=1
            if x ==4 :
                break
        for i in hard_q:
        
            if a[4] in i and not t5:
                quiz.append(i)
                hard_q.remove(i)
                t5 = True
                x+=1
            elif a[5] in i and not t6:
                quiz.append(i)
                hard_q.remove(i)
                t6 = True
                x+=1
            if x ==6 :
                break
                  
        # At this point quiz list has 6 questions in it, append it to quiz list 
        quiz_list.append(quiz)
        #shuffle a
        a = a[2:] + a[:2]
    data = list(set(easy_q+med_q+hard_q))
    for i in quiz_list:
        i.extend(data[:4])
        data = data[4:]
    return quiz_list,len(quiz_list)

file_name = input("please enter the input file name:")
quizzes,no_of_quiz = Quiz_generator(file_name)
print("Valid quizzes generated:",no_of_quiz)
