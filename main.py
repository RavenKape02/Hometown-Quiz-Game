import linecache
import random
import sys
import time

scores = {}
current_score = 0
questions = []
easy_questions = []
medium_questions = []
hard_questions = []
easy_question_lines = []
medium_question_lines = []
hard_question_lines = []
list_of_questions = []
question_lines = []
question_file = 'questions.txt'
start = ""
display_highscores = ""

# Simple function to animate loading dots
def loading_dots(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(4):
            sys.stdout.write('\rLoading' + '.' * i)
            time.sleep(0.2)
    print()

def calculating_scores_animation(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(4):
            sys.stdout.write('\rCalculating score' + '.' * i)
            time.sleep(1)

def customDotAnimation(duration, customString):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(4):
            sys.stdout.write('\r'+ customString + '.' * i)
            time.sleep(1)

with open("scores.txt", 'r') as highscores:
    first_character = highscores.read(1)
    if not first_character:
        display_highscores = "No High Scorers Yet"
    else:
        highscores.seek(0)
        for line in highscores.readlines():
            line = line.replace("\n","").split(" - ")
            scores[line[0]] = int(line[1])
            scores = dict(sorted(scores.items(), key= lambda item: item[1], reverse=True))

if len(scores) < 5:
    for keys, values in scores.items():
        display_highscores += str(keys) + ":" + str(values) + "\n "
else:
    c = 0
    for keys, values in scores.items():
        c += 1
        if c > 5:
            break
        display_highscores += str(keys) + ":" + str(values) + "\n "
    
print("Welcome to Hometown Quiz Game!!!")
print("""
 __      __   _                    _         _                                            _  
 \ \    / /__| |__ ___ _ __  ___  | |_ ___  | |   __ _ __ _ _  _ _ _  __ _   __ _ _ _  __| | 
  \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \ | |__/ _` / _` | || | ' \/ _` | / _` | ' \/ _` | 
   \_/\_/\___|_\__\___/_|_|_\___|  \__\___/ |____\__,_\__, |\_,_|_||_\__,_| \__,_|_||_\__,_| 
   ___      _            _             ___       _    |___/_                  _   _   _      
  / __|__ _| |__ _ _ __ | |__  __ _   / _ \ _  _(_)___  / __|__ _ _ __  ___  | | | | | |     
 | (__/ _` | / _` | '  \| '_ \/ _` | | (_) | || | |_ / | (_ / _` | '  \/ -_) |_| |_| |_|     
  \___\__,_|_\__,_|_|_|_|_.__/\__,_|  \__\_\\_,_|_/__|  \___\__,_|_|_|_\___| (_) (_) (_)                                                                                                                                                                                                                        
""")

print("Highscorers:\n", display_highscores)

username = input("Input your username, make it unique: ")
while True:
    start = input("Type \"start\" to start the game: ")
    if start.lower() == "start":
        break
    else:
        print("Invalid Keyword")

loading_dots(2)
print("""
   ___   _   __  __ ___   _  _   _   ___   ___ _____ _   ___ _____ ___ ___    _   _   _ 
  / __| /_\ |  \/  | __| | || | /_\ / __| / __|_   _/_\ | _ \_   _| __|   \  | | | | | |
 | (_ |/ _ \| |\/| | _|  | __ |/ _ \\\__ \ \__ \ | |/ _ \|   / | | | _|| |) | |_| |_| |_|
  \___/_/ \_\_|  |_|___| |_||_/_/ \_\___/ |___/ |_/_/ \_\_|_\ |_| |___|___/  (_) (_) (_)                                                                                       
""")

i = 0
while i < 4:
    r = random.randint(1,9)
    if r not in easy_question_lines:
        easy_question_lines.append(r)
        i += 1

i = 0
while i < 3:
    r = random.randint(10,19)
    if r not in medium_question_lines:
        medium_question_lines.append(r)
        i += 1

i = 0
while i < 3:
    r = random.randint(20,28)
    if r not in hard_question_lines:
        hard_question_lines.append(r)
        i += 1

for i in easy_question_lines:
    question = linecache.getline(question_file, i).replace('\n', '')
    easy_questions.append(question.split(" - "))
    list_of_questions.append(question.split(" - "))

for i in medium_question_lines:
    question = linecache.getline(question_file, i).replace('\n', '')
    medium_questions.append(question.split(" - "))
    list_of_questions.append(question.split(" - "))

for i in hard_question_lines:
    question = linecache.getline(question_file, i).replace('\n', '')
    hard_questions.append(question.split(" - "))
    list_of_questions.append(question.split(" - "))

for i in range(10):
    loading_dots(1)
    print("Questions to answer:")
    for j in range(len(list_of_questions)):
        print(str(j+1)+".)",list_of_questions[j][0]+" ["+list_of_questions[j][2]+"]")
    while True:    
        try:
            choice = int(input("Pick a question by inputting the number of your choice: "))
            if choice > 0 and choice <= len(list_of_questions):
                choice -= 1
                question_choice = list_of_questions[choice][3]
                break
            else:
                print("Make sure the number you inputted is right")
        except:
            print("Invalid input!!!")
    loading_dots(3)
    print("\n+-------------------------------------------------------------------------------+")
    print("Question #"+str(i+1))
    print(list_of_questions[choice][0] + " [" +list_of_questions[choice][2] + "]")
    print(list_of_questions[choice][1])
    print("+-------------------------------------------------------------------------------+")
    while True:
        answer = input("What is your answer? ")
        if answer.lower() == "a" or answer.lower() == "b" or answer.lower() == "c" or answer.lower() == "d":
            break
        else:
            print("Only input letters: \"A\" \"B\" \"C\" \"D\"")
    customDotAnimation(2, "Verifying Answer")
    if answer.lower() == list_of_questions[choice][3].lower():
        print("""
   ____ ___  ____  ____  _____ ____ _____ 
  / ___/ _ \|  _ \|  _ \| ____/ ___|_   _|
 | |  | | | | |_) | |_) |  _|| |     | |  
 | |__| |_| |  _ <|  _ <| |__| |___  | |  
  \____\___/|_| \_\_| \_\_____\____| |_|                                         
""")
        if list_of_questions[choice][2] == "Easy":
            current_score += 5
        elif list_of_questions[choice][2] == "Medium":
            current_score += 10
        elif list_of_questions[choice][2] == "Hard":
            current_score += 15
        print("Current Score:", current_score)
    else:
        print("""
 __        ______   ___  _   _  ____ 
 \ \      / /  _ \ / _ \| \ | |/ ___|
  \ \ /\ / /| |_) | | | |  \| | |  _ 
   \ V  V / |  _ <| |_| | |\  | |_| |
    \_/\_/  |_| \_\\___/|_| \_|\____|                                    
""")
    list_of_questions.pop(choice)

calculating_scores_animation(4)
print("\nYour total score:", current_score)
with open("scores.txt", 'r') as highscores:
    content = highscores.read()
    if username in content:
        start_index = content.index(username)
        end_index = content.find('\n', start_index)
        if end_index == -1:
            end_index = len(content)
        line = content[start_index:end_index]
        username_found = True
    else:
        print("Your username isn't registered yet on the scoresheet")
        username_found = False

if username_found:
    saved_score = line.split(" - ")
    print("Your high score:", saved_score[1])
    print("Your current score:", current_score)
    if current_score > int(saved_score[1]):
        newscore = username + " - " + str(current_score)
        customDotAnimation(4, "Replacing your previous high score with new one")
        with open('scores.txt', 'r') as file:
            lines = file.readlines()
        replacedline = [newline.replace(line, newscore) for newline in lines]
        with open("scores.txt", 'w') as file:
            file.writelines(replacedline)
        print()
        print("Congratulations on your new high score!!!")
    else:
        print("You didn't surpass your high score, therefore this score won't be recorded. Be better next time")

else:
    newscore = username + " - " + str(current_score) + "\n"
    with open("scores.txt", 'a') as file:
        file.write(newscore)
    customDotAnimation(3, "Registering your username and score")
    print()
    print(username, ", you have been registered successfully on the scoresheet")
    print("Your current high score:", current_score)