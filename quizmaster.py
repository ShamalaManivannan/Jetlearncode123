import pgzrun
title= "Quiz Master" 
WIDTH = 870
HEIGHT = 650

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)
score = 0
time_left = 10
question_filename = "C:/Users/35262/Downloads/questions.txt"
marquee_message = ""
game_over = False
answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
questions = []
question_count = 0
question_index = 0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color='black')
    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box,"navy blue")
    screen.draw.filled_rect(timer_box,"navy blue")
    screen.draw.filled_rect(skip_box,"dark green")
    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,"dark orange")
    marquee_message= "Welcome to Quizmaster"  
    marquee_message= marquee_message+f"Q:{question_index} of {question_count}"
    screen.draw.textbox(marquee_message,marquee_box,color= "white")
    screen.draw.textbox(str(time_left),timer_box,color="white")
    screen.draw.textbox("skip",skip_box, color="black", angle=-90)
    screen.draw.textbox(question[0].strip(),question_box,color= "white")
    index = 1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box, color="black")
        index+=1

def update():
    move_marquee()

def move_marquee():
    marquee_box.x-= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def read_question_file():
    global question_count,questions
    q_file= open(question_filename,"r")
    for question in q_file:
        questions.append(question)
        question_count+=1
    q_file.close()

def read_next_question():
    global question_index 
    question_index+=1
    return questions.pop(0).split(",")

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                game_over()
        index+=1
    if skip_box.collidepoint(pos):
        skip_question()

def correct_answer():
    global score,question,time_left,questions
    score+=1
    if questions:
        question=read_next_question()
        time_left = 10 
    else:
        game_over()

def game_over():
    global question,time_left,game_over
    message = f"game over! You got {score} questions correct"
    question = [message,"-","-", "-","-",5]
    time_left=0
    game_over = True

def skip_question():
    global question, time_left
    if questions and not game_over:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def updatetime_left():
    global time_left
    if time_left:
        time_left-=1    
    else:
        game_over()

read_question_file()
question = read_next_question()
clock.schedule_interval(updatetime_left,1)

pgzrun.go()




