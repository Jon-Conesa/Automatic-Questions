print("Running")

flashcards = []

f = open("apuntes.txt", "r")
if f.mode == 'r':
    contents = f.read()
    contents = contents.replace("**", "")
    contents += "\n"
def reverse(x):
  return x[::-1]

def printquestions():
    f = open("questions.txt","w+")
    for i in range(len(flashcards)):
        f.write(flashcards[i]+"\n")

def find_definitions():
    for i in range(len(contents)):
        if contents[i] == ":" and contents[i+1] != "/":
            concept = ""
            definition = ""
            question = ""
            question2 = ""
            s = i-1
            t=i+1
            while contents[s] != "\n" and contents[s] != "-":
                concept += contents[s]
                s = s-1
            while contents[t] != "\n":
                definition += contents[t]
                t = t+1
            concept = reverse(concept)
            for h in range(1):
                if concept[h] == " ":
                    concept = concept.replace(" ", "", 1)
            if "Fórmula" in concept or "Fòrmula" in concept or "Formula" in concept or "fòrmula" in concept or "fórmula" in concept or "formula" in concept:
                print("One Fórmula skiped")
            else:
                question = "Explica <b>"+concept+"</b> 📖"+"	"+definition
                question2 = "Troba la paraula 💬:<br>"+definition+"	"+"<b>"+concept+"</b>"
                flashcards.append(question)
                flashcards.append(question2)

def find_preguntes():
    for i in range(len(contents)):
        if contents[i] == "?" and contents[i+1] != "/":
            concept = ""
            definition = ""
            question = ""
            s = i-1
            t=i+1
            while contents[s] != "\n" and contents[s] != "-":
                concept += contents[s]
                s = s-1
            while contents[t] != "\n":
                definition += contents[t]
                t = t+1
            concept = reverse(concept)
            question = concept+"❓"+"	"+definition
            flashcards.append(question)

def find_history():
    for i in range(len(contents)):
        if contents[i] == "-" and contents[i-1] != "\n" and contents[i-3] != " ":
            p = i-1
            permision = "false"
            while contents[p] != "\n":
                if contents[p] != "-":
                    permision = "true"
                else:
                    permision = "false"
                    break
                p = p-1
            if permision == "true":
                total_history = ""
                s = i-1
                t=i
                events = []
                total_history = ""
                while contents[s] != "\n":
                    total_history += contents[s]
                    s = s-1
                total_history = reverse(total_history)
                while contents[t] != "\n":
                    total_history += contents[t]
                    t = t+1
                split_list = []
                split_list = total_history.split("-")
                # print(split_list)
                final_question = split_list[0]+"- "+("<font color=""#003cff"">[..]</font> - ")*(len(split_list)-2)+"[..]"+"       "
                for i in range(len(split_list)):
                    question = ""
                    if i == 0:
                        question = "<font color=""#003cff"">[..]</font> - "+split_list[i+1]+" - [..]"*(len(split_list)-2)+"	"+"<font color=""#003cff"">"+split_list[i]+"</font>"+" - "+split_list[i+1]+" - [..]"*(len(split_list)-2)
                        flashcards.append(question)
                        final_question += split_list[i]+"-"
                    elif i == len(split_list)-1:
                        question = "[..] - "*(len(split_list)-2)+split_list[i-1]+" - <font color=""#003cff"">[..]</font>"+"	"+"[..] - "*(len(split_list)-2)+split_list[i-1]+" - "+"<font color=""#003cff"">"+split_list[i]+"</font>"
                        flashcards.append(question)
                        final_question += split_list[i]
                    else:
                        question = "[..] - "*(i-1)+split_list[i-1]+" - <font color=""#003cff"">[..]</font> - "+split_list[i+1]+" - [..] "*(len(split_list)-i-2)+"	"+"[..] - "*(i-1)+split_list[i-1]+" -<font color=""#003cff"">"+split_list[i]+"</font> - "+split_list[i+1]+" - [..] "*(len(split_list)-i-2)
                        flashcards.append(question)
                        final_question += split_list[i]+"-"

                flashcards.append(final_question)

def find_comas():
    for i in range(len(contents)):
        if contents[i] == ",":
            p = i-1
            t= i+1
            total_phrase = ""
            permision = "false"
            aux = "false"
            while contents[p] != "\n":
                if contents[p] != "," and contents[p] != "-" and contents[p] != ":":
                    permision = "true"
                    total_phrase += contents[p]
                else:
                    permision = "false"
                    break
                p = p-1
            total_phrase = reverse(total_phrase) +","
            while contents[t] != "\n" and contents[t] != ":":
                if contents[t] != ",":
                    aux = "true"
                    total_phrase += contents[t]
                else:
                    aux = "false"
                    break
                t = t+1
            # Be careful with this type of sentences like -------, ------------ i ------.
            if permision == "true" and aux == "true":
                part = []
                part1 = ""
                part2 = ""
                part = total_phrase.split(",")
                part1= part[0]
                part2 = part[1]
                part = part1.split(" ", 2)
                part += part2.split(" ", 2)
                #question = part[0]+" "+part[1]+" [...], "+part[4]+" "+part[5]+"     "+part[0]+" "+part[1]+" "+part[2]+", "+part[4]+" "+part[5]
                #flashcards.append(question)
                #question = part[0]+" "+part[1]+" "+part[2]+", "+part[4]+" [...]."+"	"+part[0]+" "+part[1]+" "+part[2]+", "+part[4]+" "+part[5]
                #flashcards.append(question)

def find_because():
    for i in range(len(contents)):
        if contents[i] == "p" or contents[i] == "b":
            if contents[i+1] == "o" or contents[i+1] == "e":
                if contents[i+2] == "r" or contents[i+2] == "c":
                    if contents[i+3] == "q" or contents[i+3] == "a":
                        if contents[i+4] == "u":
                            if contents[i+5] == "e" or contents[i+5] == "s" or contents[i+5] == "è":
                                total_phrase = ""
                                split_list = []
                                s = i-1
                                t= i

                                while contents[s] != "\n":
                                    if contents[s] == ":":
                                        return None
                                    total_phrase += contents[s]
                                    s = s-1
                                total_phrase = reverse(total_phrase)
                                while contents[t] != "\n":
                                    total_phrase += contents[t]
                                    t = t+1

                                split_list = total_phrase.split("perque")
                                if len(split_list) == 1:
                                    split_list = total_phrase.split("perquè")
                                if len(split_list) == 1:
                                    split_list = total_phrase.split("porque")
                                if len(split_list) == 1:
                                    split_list = total_phrase.split("because")
                                if len(split_list) == 1:
                                    split_list = total_phrase.split("perqué")

                                question = "Per què "+split_list[0].lower()+"❓"+"	"+"Perquè"+split_list[1].lower()
                                flashcards.append(question)

def find_formulas():
    for i in range(len(contents)):
        if contents[i] == "$":
            if contents[i+1] == "$":
                total_formula = ""
                permision = "true"
                s = i-1
                while contents[s] != "\n":
                    if contents[s] == "$":
                        permision = "false"
                    s = s-1
                if permision == "true":
                    t = i
                    while contents[t] != "\n":
                        total_formula += contents[t]
                        t = t+1
                    total_formula = total_formula.replace('$', '')
                    total_formula = "\("+total_formula+"\)"
                    question = ""
                    problem = ""
                    s = i
                    while contents[s] != ":":
                        t = s
                        while contents[t] != "\n":
                            problem += contents[t]
                            t=t-1
                        s = s-1
                    problem = reverse(problem)
                    problem = problem.replace("$", "")
                    question = "Troba 🔢: <br>"+problem+"	"+total_formula
                    flashcards.append(question)

def find_lists():
    for i in range(len(contents)):
        if contents[i] == "-" and contents[i-1] == "\n":
            permision = "true"
            list_title = ""
            s=i-3
            while contents[s] != "\n":
                if contents[s] == "-":
                    permision = "false"
                    break
                else:
                    list_title += contents[s]
                s = s-1
            if permision == "true":
                list_title = reverse(list_title)
                list_title = list_title.replace("##", "")
                #print(list_title)
                #if list_title[0] == " ":
                    #list_title = list_title.replace(" ", "", 1)
                total_list_string = ""
                permision_string = ""
                while 1==1:
                    if contents[i] == "\n":
                        s=i+1
                        permision_string = ""
                        while contents[s] != "\n":
                            permision_string += contents[s]
                            s += 1
                        if len(permision_string) < 2:
                            break
                    total_list_string += contents[i]
                    i = i+1

                total_list_array = total_list_string.split("\n")
                word_list = ""
                for y in range(len(total_list_array)):
                    total_list_array[y] = total_list_array[y].replace("-", "0")
                    total_list_array[y] = total_list_array[y].replace("    ", "1")

                question_first_array = []
                for h in range(len(total_list_array)): #For first bullet
                    word_test = total_list_array[h]
                    if word_test[0] == "0":
                        word_test = word_test.replace("0", "")
                        question_first_array.append(word_test)
                final_question_first = "<b>"+list_title+"</b>"+"<br> <br>"+("<font color=""#003cff"">[..]</font><br>")*(len(question_first_array))+"	"
                for g in range(len(question_first_array)):
                    question_first = ""
                    if g == 0:
                        question_first = "<b>"+list_title+"</b>"+"<br> <br>"+"<font color=""#003cff"">[..]</font> <br> "+question_first_array[g+1]+"<br> [..] <br>"*(len(question_first_array)-2)+"	"+"<b>"+list_title+"</b>"+"<br> <br>"+"<font color=""#003cff"">"+question_first_array[g]+"</font>"+"<br>"+question_first_array[g+1]+"<br>"+"[..] <br>"*(len(question_first_array)-2)
                        flashcards.append(question_first)
                        final_question_first += question_first_array[g]+"<br>"
                    elif g == len(question_first_array)-1:
                        question_first = "<b>"+list_title+"</b>"+"<br> <br>"+"[..] <br>"*(len(question_first_array)-2)+question_first_array[g-1]+"<br> <font color=""#003cff"">[..]</font><br>"+"	"+"<b>"+list_title+"</b>"+"<br> <br>"+"[..] <br>"*(len(question_first_array)-2)+question_first_array[g-1]+"<br>"+"<font color=""#003cff"">"+question_first_array[g]+"</font>"
                        flashcards.append(question_first)
                        final_question_first += question_first_array[g]+"<br>"
                    else:
                        question_first = "<b>"+list_title+"</b>"+"<br> <br>"+"[..] <br> "*(g-1)+question_first_array[g-1]+"<br> <font color=""#003cff"">[..]</font> <br>"+question_first_array[g+1]+"<br> [..]"*(len(question_first_array)-g-2)+"	"+"<b>"+list_title+"</b>"+"<br> <br>"+"[..] <br> "*(g-1)+question_first_array[g-1]+"<br> <font color=""#003cff"">"+question_first_array[g]+"</font> <br>"+question_first_array[g+1]+"<br> [..] <br>"*(len(question_first_array)-g-2)
                        flashcards.append(question_first)
                        final_question_first += question_first_array[g]+"<br>"
                flashcards.append(final_question_first)

                array_second_list = []
                allow=""
                for k in range(len(total_list_array)):
                	initial_word = "1"*(k+1)+"0"
                	for n in range(len(total_list_array)):
                		if total_list_array[n].find(initial_word) != -1:
                			array_second_list.append(total_list_array[n])
                			allow="false"
                			if total_list_array[n-1].find(initial_word) == -1:
                					allow = "true"
                					print("")
                			if allow == "true":
                				title_second = total_list_array[n-1]
                				same_level_array = [total_list_array[n]]
                				print(total_list_array[n])
                				"""v = n
                				while 1==1:
                					if total_list_array[v].find(initial_word) != -1:
                						same_level_array +=total_list_array[v]
                					elif total_list_array[v].find(initial_word) == -1:
                						break
                					v += 1
                				print(same_level_array)"""


                					#print(allow)
                			
                			"""
                			while total_list_array[s].find(initial_word) != -1:
                				if total_list_array[s].find(initial_word) != -1:
                					allow = "false"
                				s = s-1
                				print("Hello", total_list_array[s])"""
                
find_definitions()
find_preguntes()
find_history()
find_comas()
find_because()
find_formulas()
find_lists()
printquestions()
