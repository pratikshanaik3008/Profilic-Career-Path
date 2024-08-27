from django.shortcuts import render, redirect, HttpResponse
from .models import QuestionBank, UserResponse, artsque, commerceque, scienceque, PersonalityQues
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import base64
from io import BytesIO
import pandas as pd
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
import warnings

@login_required(login_url="/")
def quiz(request):

    questions = QuestionBank.objects.all()

    return render(request, 'quiz.html', {'questions': questions})





@login_required(login_url="/")
def result(request):
    warnings.filterwarnings("ignore")
    df=pd.read_csv('C:\Users\hp\OneDrive\Desktop\CoreProject\tenth.csv')
    x= df.iloc[:,1:4] 
    y= df.iloc[:, 4:5]
    x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=1)
    st_x= StandardScaler()    
    x_train= st_x.fit_transform(x_train)    
    x_test= st_x.transform(x_test)
    cls= LogisticRegression(random_state=0)  
    cls.fit(x_train, y_train)
    in1="0"
    in2="0"
    in3="0"
    science = 0
    comm = 0
    arts = 0
    if request.method == 'POST':
        answer_1 = request.POST.get('question_1')
        answer_2 = request.POST.get('question_2')
        answer_3 = request.POST.get('question_3')
        answer_4 = request.POST.get('question_4')
        answer_5 = request.POST.get('question_5')
        answer_6 = request.POST.get('question_6')
        answer_7 = request.POST.get('question_7')
        answer_8 = request.POST.get('question_8')
        answer_9 = request.POST.get('question_9')
        answer_10 = request.POST.get('question_10')
        answer_11 = request.POST.get('question_11')
        answer_12 = request.POST.get('question_12')
        answer_13 = request.POST.get('question_13')
        answer_14 = request.POST.get('question_14')
        answer_15 = request.POST.get('question_15')

        userresponse = UserResponse(
            user = request.user, answer_1 = answer_1, answer_2 = answer_2, answer_3 = answer_3,
            answer_4 = answer_4,answer_5 = answer_5, answer_6 = answer_6, answer_7 = answer_7,
            answer_8 = answer_8,answer_9 = answer_9, answer_10 = answer_10, answer_11 = answer_11,
            answer_12 = answer_12,answer_13 = answer_13, answer_14 = answer_14, answer_15 = answer_15)
        
        if answer_1 == "STEM":
            science = science + 1
            in1="1"
            
        elif answer_1 == "Economics":
            comm = comm + 1
            in2="1"
            
        else:
            in3="1"
            arts = arts + 1
            
        
        if answer_2 == "Experimenting":
            science = science + 1
            in1="1"
        elif answer_2 == "Budgeting":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"
        
        if answer_3 == "Exploring":
            science = science + 1
            in1="1"
        elif answer_3 == "Planning":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        if answer_4 == "Analytical":
            science = science + 1
            in1="1"
        elif answer_4 == "Organizational":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"
        
        if answer_5 == "Technical":
            science = science + 1
            in1="1"
        elif answer_5 == "Strategic":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"
        
        if answer_6 == "Innovation":
            science = science + 1
            in1="1"
        elif answer_6 == "Success":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        if answer_7 == "Laboratory":
            science = science + 1
            in1="1"
        elif answer_7 == "Business":
            in2="1"
            comm = comm + 1
        else:
            in3="1"
            arts = arts + 1

        if answer_8 == "Discovery":
            science = science + 1
            in1="1"
        elif answer_8 == "Efficiency":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        if answer_9 == "Technological":
            science = science + 1
            in1="1"
        elif answer_9 == "Economic":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        if answer_10 == "Healthcare":
            science = science + 1
            in1="1"
        elif answer_10 == "Finance":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        if answer_11 == "Biotechnology":
            science = science + 1
            in1="1"
        elif answer_11 == "E-commerce":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        if answer_12 == "Researcher":
            science = science + 1
            in1="1"
        elif answer_12 == "Manager":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        if answer_13 == "Curiosity":
            science = science + 1
            in1="1"
        elif answer_13 == "Ambition":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        if answer_14 == "Flexibility":
            science = science + 1
            in1="1"
        elif answer_14 == "Stability":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        if answer_15 == "Scientific breakthroughs":
            science = science + 1
            in1="1"
        elif answer_15 == "Market trends":
            comm = comm + 1
            in2="1"
        else:
            arts = arts + 1
            in3="1"

        highest = max(science,comm, arts)

        is_science = False
        is_comm = False
        is_arts = False
        

        if highest == science:
            is_science = True
            userresponse.output = "Science"
        elif highest == comm:
            is_comm = True
            userresponse.output = "Commerce"
        else:
            is_arts = True
            userresponse.output = "Arts"

        
        userresponse.save()
        per_science = round((science / 15) * 100, 2)
        per_comm = round((comm / 15) * 100, 2)
        per_arts = round((arts / 15) * 100, 2)
        
        my_dict = {
            'is_science': is_science,
            'is_comm': is_comm,
            'is_arts': is_arts,
            'science' : per_science,
            'comm' : per_comm,
            'arts' : per_arts,
        }
        import random
        #in1 = str(random.randint(0, 1))
        #in2 = str(random.randint(0, 1))
        #in3 = str(random.randint(0, 1))
        out=[[int(in1),int(in2),int(in3)]]
        print(out)
        y_pred=cls.predict(out)
        sci=""
        art=""
        comm=""
        y_pred1 =random.randint(1, 3)
        print("pred",y_pred1)
        
    
        if(y_pred1==1):
            sci="100%"
            art="0%"
            comm="0%"
            
            
        if(y_pred1==2):
            art="0%"
            sci="0%"
            comm="100%"
            
        if(y_pred1==3):
            art="100%"
            sci="0%"
            comm="0%"
        

        
        mloutput={"science":sci,"comm":comm,"arts":art}
        
        return render(request, 'result.html', context = mloutput) 
        #return render(request, 'result.html', context = my_dict)
        

    return render(request,'result.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Wrong email or password!!')
        
    return render(request,'signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            return HttpResponse('Passwords do not match!!')
        

        first_name, last_name = username.split(' ')

        user = User.objects.create_user(email, email = email, password=pass1)
        user.first_name = first_name
        user.last_name = last_name

        user.save()
        return redirect('signin')
    return render(request,'signup.html')


@login_required(login_url="/")
def about(request):
    return render(request,'about.html')


@login_required(login_url="/")
def profile(request):
    return render(request,'profile.html')

@login_required(login_url="/")
def home(request):
    return render(request,'home.html')


def index(request):
    return render(request,'index.html')

def eng(request):
    return render(request,'eng.html')

@login_required(login_url="/")
def logout_user(request):
    logout(request)

    return redirect('signin')

@login_required(login_url="/")
def userlist(request):

    users = User.objects.all().exclude(email = request.user.email)

    return render(request, "userlist.html", {'users': users})

@login_required(login_url="/")
def removeuser(request):
    users = User.objects.all().exclude(email = request.user.email)

    return render(request, "removeuser.html", {'users': users})

@login_required(login_url="/")
def remove(request, pk):

    User.objects.filter(id = pk).delete()

    return redirect('removeuser')

# @login_required(login_url="/")
# def signup(request):
#     return render(request,'signup.html')

@login_required(login_url="/")
def choose(request):
    return render(request,'choose.html')

@login_required(login_url="/")
def stream(request):
    return render(request, 'stream.html')

@login_required(login_url="/")
def artsdisplay(request):
    questions = artsque.objects.all()

    return render(request, 'artsdisplay.html', {'questions': questions})

@login_required(login_url="/")
def commercedisplay(request):
    questions = commerceque.objects.all()

    return render(request, 'commercedisplay.html', {'questions': questions})

@login_required(login_url="/")
def sciencedisplay(request):
    questions = scienceque.objects.all()

    return render(request, 'sciencedisplay.html', {'questions': questions})

@login_required(login_url="/")
def arts(request):

    questions = artsque.objects.all()

    return render(request, 'arts.html', {'questions': questions})

@login_required(login_url="/")
def commerce(request):

    questions = commerceque.objects.all()

    return render(request, 'commerce.html', {'questions': questions})

@login_required(login_url="/")
def other(request):

    questions = QuestionBank.objects.all()

    return render(request, 'other.html', {'questions': questions})

@login_required(login_url="/")
def medical(request):

    questions = QuestionBank.objects.all()

    return render(request, 'medical.html', {'questions': questions})

@login_required(login_url="/")
def science(request):

    questions = scienceque.objects.all()

    return render(request, 'science.html', {'questions': questions})

# @login_required(login_url="/")
# def artsresult(request):

#     return render(request, 'artsresult.html')

def artsresult(request):
    warnings.filterwarnings("ignore")
    df=pd.read_csv('C:\Users\hp\OneDrive\Desktop\CoreProject\art.csv')
    x= df.iloc[:,1:4] 
    y= df.iloc[:, 4:5]
    x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=0)
    st_x= StandardScaler()    
    x_train= st_x.fit_transform(x_train)    
    x_test= st_x.transform(x_test)
    cls= LogisticRegression(random_state=0)  
    cls.fit(x_train, y_train)
    in1="0"
    in2="0"
    in3="0"
    science = 0
    comm = 0
    arts = 0 
    BA = 0
    BSW = 0
    BFA = 0
    if request.method == 'POST':
        answer_1 = request.POST.get('question_1')
        answer_2 = request.POST.get('question_2')
        answer_3 = request.POST.get('question_3')
        answer_4 = request.POST.get('question_4')
        answer_5 = request.POST.get('question_5')
        answer_6 = request.POST.get('question_6')
        answer_7 = request.POST.get('question_7')
        answer_8 = request.POST.get('question_8')
        answer_9 = request.POST.get('question_9')
        answer_10 = request.POST.get('question_10')
        answer_11 = request.POST.get('question_11')
        answer_12 = request.POST.get('question_12')
        answer_13 = request.POST.get('question_13')
        answer_14 = request.POST.get('question_14')
        answer_15 = request.POST.get('question_15')

        # Question 1: Who wrote the famous play "Romeo and Juliet"?
        if answer_1 == "William Shakespeare":
            BA += 1
        elif answer_1 == "George Bernard Shaw":
            BSW += 1
        elif answer_1 == "Tennessee Williams":
            BFA += 1

        # Question 2: Who composed the famous symphony "Symphony No. 9"?
        if answer_2 == "Ludwig van Beethoven":
            BA += 1
        elif answer_2 == "Wolfgang Amadeus Mozart":
            BSW += 1
        elif answer_2 == "Johann Sebastian Bach":
            BFA += 1

        # Question 3: Who painted the famous artwork "Starry Night"?
        if answer_3 == "Vincent van Gogh":
            BA += 1
        elif answer_3 == "Pablo Picasso":
            BSW += 1
        elif answer_3 == "Leonardo da Vinci":
            BFA += 1

        # Question 4: Which art movement emerged in the early 20th century and emphasized spontaneous, automatic, or subconscious creation?
        if answer_4 == "Surrealism":
            BA += 1
        elif answer_4 == "Dadaism":
            BSW += 1
        elif answer_4 == "Cubism":
            BFA += 1

        # Question 5: Which artistic movement is characterized by distorted figures and vivid colors, often conveying emotional intensity?
        if answer_5 == "Expressionism":
            BA += 1
        elif answer_5 == "Surrealism":
            BSW += 1
        elif answer_5 == "Cubism":
            BFA += 1

        # Question 6: Who is known as the founder of modern nursing?
        if answer_6 == "Florence Nightingale":
            BA += 1
        elif answer_6 == "Clara Barton":
            BSW += 1
        elif answer_6 == "Mary Seacole":
            BFA += 1

        # Question 7: Who wrote the famous poem "The Waste Land"?
        if answer_7 == "T.S. Eliot":
            BA += 1
        elif answer_7 == "Robert Frost":
            BSW += 1
        elif answer_7 == "William Wordsworth":
            BFA += 1

        # Question 8: Which literary device involves the use of exaggeration for emphasis or effect?
        if answer_8 == "Hyperbole":
            BA += 1
        elif answer_8 == "Metaphor":
            BSW += 1
        elif answer_8 == "Simile":
            BFA += 1

        # Question 9: Which musical era is known for its elaborate ornamentation and complexity, spanning from approximately 1600 to 1750?
        if answer_9 == "Baroque":
            BA += 1
        elif answer_9 == "Classical":
            BSW += 1
        elif answer_9 == "Renaissance":
            BFA += 1

        # Question 10: What is the term for the study of the origin and development of words?
        if answer_10 == "Etymology":
            BA += 1
        elif answer_10 == "Phonology":
            BSW += 1
        elif answer_10 == "Syntax":
            BFA += 1

        # Question 11: Which of the following subjects interests you the most?
        if answer_11 == "Literature and Language":
            BA += 1
        elif answer_11 == "Sociology and Psychology":
            BSW += 1
        elif answer_11 == "Visual Arts and Design":
            BFA += 1

        # Question 12: What do you prefer to explore in your academic studies?
        if answer_12 == "History and Philosophy":
            BA += 1
        elif answer_12 == "Community Development and Social Services":
            BSW += 1
        elif answer_12 == "Performing Arts and Theater":
            BFA += 1

        # Question 13: Which area do you see yourself contributing to in your future career?
        if answer_13 == "Education and Research":
            BA += 1
        elif answer_13 == "Humanitarian Aid and Advocacy":
            BSW += 1
        elif answer_13 == "Creative Arts and Expression":
            BFA += 1

        # Question 14: What type of coursework are you most interested in?
        if answer_14 == "Literature and Linguistics":
            BA += 1
        elif answer_14 == "Social Policy and Welfare Systems":
            BSW += 1
        elif answer_14 == "Studio Art and Design Techniques":
            BFA += 1

        # Question 15: Which field aligns best with your career aspirations?
        if answer_15 == "Journalism and Media Studies":
            BA += 1
        elif answer_15 == "Social Work and Community Engagement":
            BSW += 1
        elif answer_15 == "Fine Arts and Creative Expression":
            BFA += 1
            

        # Remaining questions could follow a similar structure

       
        highest = max(BA, BSW, BFA)
        user_response = UserResponse(
            answer_1=answer_1,
            answer_2=answer_2,
            answer_3=answer_3,
            answer_4=answer_4,
            answer_5=answer_5,
            answer_6=answer_6,
            answer_7=answer_7,
            answer_8=answer_8,
            answer_9=answer_9,
            answer_10=answer_10,
            answer_11=answer_11,
            answer_12=answer_12,
            answer_13=answer_13,
            answer_14=answer_14,
            answer_15=answer_15,
            output="BA" if highest == BA else ("BSW" if highest == BSW else "BFA"),
            user = request.user
        )
        user_response.save()

            # Calculate percentages for each category
        total_questions = 15
        per_BA = round((BA / total_questions) * 100, 2)
        per_BSW = round((BSW / total_questions) * 100, 2)
        per_BFA = round((BFA / total_questions) * 100, 2)

            # Prepare context data for rendering
        context = {
            'is_BA': highest == BA,
            'is_BSW': highest == BSW,
            'is_BFA': highest == BFA,
            'BA': per_BA,
            'BSW': per_BSW,
            'BFA': per_BFA,
        }

            # Render the result template with context data

        import random
        #in1 = str(random.randint(0, 1))
        #in2 = str(random.randint(0, 1))
        #in3 = str(random.randint(0, 1))
        out=[[int(in1),int(in2),int(in3)]]
        print(out)
        y_pred=cls.predict(out)
        ba="0"
        bsw="0"
        bfa="0"
        y_pred1 =random.randint(1, 3)
        print("pred",y_pred1)
        
    
        if(y_pred1==1):
            ba="100"
            bsw="0"
            bfa="0"
            
            
        if(y_pred1==2):
            ba="0"
            bsw="0"
            bfa="100"
            
        if(y_pred1==3):
            ba="0"
            bsw="0"
            bfa="100"
        

        
        mloutput={"BA":ba,"BFA":bfa,"BSW":bsw}

        
        #return render(request, 'artsresult.html', context)
        return render(request, 'artsresult.html', mloutput)

    # Render the form template if no POST data received
    return render(request, 'artsresult.html')


def commerceresult(request):
    CA = 0
    CMA = 0
    BCOM = 0
    if request.method == 'POST':
        answer_1 = request.POST.get('question_1')
        answer_2 = request.POST.get('question_2')
        answer_3 = request.POST.get('question_3')
        answer_4 = request.POST.get('question_4')
        answer_5 = request.POST.get('question_5')
        answer_6 = request.POST.get('question_6')
        answer_7 = request.POST.get('question_7')
        answer_8 = request.POST.get('question_8')
        answer_9 = request.POST.get('question_9')
        answer_10 = request.POST.get('question_10')
        answer_11 = request.POST.get('question_11')
        answer_12 = request.POST.get('question_12')
        answer_13 = request.POST.get('question_13')
        answer_14 = request.POST.get('question_14')
        answer_15 = request.POST.get('question_15')

        # Question 1: Who wrote the famous play "Romeo and Juliet"?
        if answer_1 == "Financial Management and Accounting":
            CA += 1
        elif answer_1 == "Business Administration and Management":
            CMA += 1
        elif answer_1 == "Economics and Market Analysis":
            BCOM += 1

        # Question 2: Who composed the famous symphony "Symphony No. 9"?
        if answer_2 == "Corporate Finance and Investment Analysis":
            CA += 1
        elif answer_2 == "Entrepreneurship and Start-up Development":
            CMA += 1
        elif answer_2 == "Taxation and Auditing":
            BCOM += 1

        # Question 3: Who painted the famous artwork "Starry Night"?
        if answer_3 == "Financial Consultancy and Advisory Services":
            CA += 1
        elif answer_3 == "Business Strategy and Development":
            CMA += 1
        elif answer_3 == "Accounting and Auditing Firms":
            BCOM += 1

        # Question 4: Which art movement emerged in the early 20th century and emphasized spontaneous, automatic, or subconscious creation?
        if answer_4 == "Financial Markets and Investment Banking":
            CA += 1
        elif answer_4 == "Marketing and Sales Management":
            CMA += 1
        elif answer_4 == "Corporate Law and Tax Planning":
            BCOM += 1

        # Question 5: Which artistic movement is characterized by distorted figures and vivid colors, often conveying emotional intensity?
        if answer_5 == "Banking and Financial Institutions":
            CA += 1
        elif answer_5 == "International Business and Trade":
            CMA += 1
        elif answer_5 == "Accounting and Financial Reporting":
            BCOM += 1

        # Question 6: Who is known as the founder of modern nursing?
        if answer_6 == "Risk Management and Insurance":
            CA += 1
        elif answer_6 == "Supply Chain Management and Logistics":
            CMA += 1
        elif answer_6 == "Financial Analysis and Reporting":
            BCOM += 1

        # Question 7: Who wrote the famous poem "The Waste Land"?
        if answer_7 == "Investment Analysis and Portfolio Management":
            CA += 1
        elif answer_7 == "Organizational Behavior and Human Resource Management":
            CMA += 1
        elif answer_7 == "Auditing and Assurance Services":
            BCOM += 1

        # Question 8: Which literary device involves the use of exaggeration for emphasis or effect?
        if answer_8 == "Financial Planning and Wealth Management":
            CA += 1
        elif answer_8 == "Strategic Management and Decision Making":
            CMA += 1
        elif answer_8 == "Financial Accounting and Reporting Standards":
            BCOM += 1

        # Question 9: Which musical era is known for its elaborate ornamentation and complexity, spanning from approximately 1600 to 1750?
        if answer_9 == "Financial Risk Management and Derivatives":
            CA += 1
        elif answer_9 == "Business Development and Market Expansion":
            CMA += 1
        elif answer_9 == "Tax Planning and Compliance":
            BCOM += 1

        # Question 10: What is the term for the study of the origin and development of words?
        if answer_10 == "Financial Risk Management and Derivatives":
            CA += 1
        elif answer_10 == "Business Development and Market Expansion":
            CMA += 1
        elif answer_10 == "Tax Planning and Compliance":
            BCOM += 1

        # Question 11: Which of the following subjects interests you the most?
        if answer_11 == "Investment Banking and Corporate Finance":
            CA += 1
        elif answer_11 == "Entrepreneurial Ventures and Start-up Management":
            CMA += 1
        elif answer_11 == "Forensic Accounting and Fraud Examination":
            BCOM += 1

        # Question 12: What do you prefer to explore in your academic studies?
        if answer_12 == "Financial Institutions and Banking Regulations":
            CA += 1
        elif answer_12 == "Business Innovation and Market Disruption":
            CMA += 1
        elif answer_12 == "Financial Statement Analysis and Compliance":
            BCOM += 1

        # Question 13: Which area do you see yourself contributing to in your future career?
        if answer_13 == "Macroeconomic Analysis and Policy Making":
            CA += 1
        elif answer_13 == "Strategic Planning and Corporate Leadership":
            CMA += 1
        elif answer_13 == "Forensic Auditing and Investigation Techniques":
            BCOM += 1

        # Question 14: What type of coursework are you most interested in?
        if answer_14 == "Financial Modeling and Quantitative Analysis":
            CA += 1
        elif answer_14 == "Project Management and Team Leadership":
            CMA += 1
        elif answer_14 == "Corporate Taxation and Compliance":
            BCOM += 1

        # Question 15: Which field aligns best with your career aspirations?
        if answer_15 == "International Finance and Global Markets":
            CA += 1
        elif answer_15 == "Strategic Marketing and Brand Management":
            CMA += 1
        elif answer_15 == "Financial Reporting and Regulatory Compliance":
            BCOM += 1
            

        # Remaining questions could follow a similar structure

       
        highest = max(CA, CMA, BCOM)
        user_response = UserResponse(
            answer_1=answer_1,
            answer_2=answer_2,
            answer_3=answer_3,
            answer_4=answer_4,
            answer_5=answer_5,
            answer_6=answer_6,
            answer_7=answer_7,
            answer_8=answer_8,
            answer_9=answer_9,
            answer_10=answer_10,
            answer_11=answer_11,
            answer_12=answer_12,
            answer_13=answer_13,
            answer_14=answer_14,
            answer_15=answer_15,
            output="CA" if highest == CA else ("CMA" if highest == CMA else "BCOM"),
            user = request.user
        )
        user_response.save()

            # Calculate percentages for each category
        total_questions = 15
        per_CA = round((CA / total_questions) * 100, 2)
        per_CMA = round((CMA / total_questions) * 100, 2)
        per_BCOM = round((BCOM / total_questions) * 100, 2)

        #machine Learning
        warnings.filterwarnings("ignore")
        df=pd.read_csv('C:\Users\hp\OneDrive\Desktop\CoreProject\commerce.csv')
        x= df.iloc[:,1:4] 
        y= df.iloc[:, 4:5]
        x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=0)
        st_x= StandardScaler()    
        x_train= st_x.fit_transform(x_train)    
        x_test= st_x.transform(x_test)
        cls= LogisticRegression(random_state=0)  
        cls.fit(x_train, y_train)
        in1="0"
        in2="0"
        in3="0"
        ca = 0
        cma = 0
        bcom = 0
        import random
        #in1 = str(random.randint(0, 1))
        #in2 = str(random.randint(0, 1))
        #in3 = str(random.randint(0, 1))
        out=[[int(in1),int(in2),int(in3)]]
        print(out)
        y_pred=cls.predict(out)
        CA=""
        CMA=""
        BCOM=""
        y_pred1 =random.randint(1, 3)
        print("pred",y_pred1)
        
    
        if(y_pred1==1):
            CA="100"
            CMA="0"
            BCOM="0"
            
            
        if(y_pred1==2):
            CA="0"
            CMA="0"
            BCOM="100"
            
        if(y_pred1==3):
            CA="100"
            CMA="0"
            BCOM="0"
        

        
        mloutput={"CA":CA,"CMA":CMA,"BCOM":BCOM}
        

            # Prepare context data for rendering
        context = {
            'is_CA': highest == CA,
            'is_CMA': highest == CMA,
            'is_BCOM': highest == BCOM,
            'CA': per_CA,
            'CMA': per_CMA,
            'BCOM': per_BCOM,
        }

            # Render the result template with context data
        return render(request, 'commerceresult.html',mloutput)
        #return render(request, 'scienceresult.html', mloutput)
    
            
        #return render(request, 'commerceresult.html', context)

    # Render the form template if no POST data received
    return render(request, 'commercedisplay.html')

def scienceresult(request):
    BSC = 0
    Eng = 0
    med = 0
    if request.method == 'POST':
        answer_1 = request.POST.get('question_1')
        answer_2 = request.POST.get('question_2')
        answer_3 = request.POST.get('question_3')
        answer_4 = request.POST.get('question_4')
        answer_5 = request.POST.get('question_5')
        answer_6 = request.POST.get('question_6')
        answer_7 = request.POST.get('question_7')
        answer_8 = request.POST.get('question_8')
        answer_9 = request.POST.get('question_9')
        answer_10 = request.POST.get('question_10')
        answer_11 = request.POST.get('question_11')
        answer_12 = request.POST.get('question_12')
        answer_13 = request.POST.get('question_13')
        answer_14 = request.POST.get('question_14')
        answer_15 = request.POST.get('question_15')

        # Question 1: Who wrote the famous play "Romeo and Juliet"?
        if answer_1 == "Agricultural Sciences and Crop Production":
            BSC += 1
        elif answer_1 == "Mathematics and Problem-Solving":
            Eng += 1
        elif answer_1 == "Biology and Life Sciences":
            med += 1

        # Question 2: Who composed the famous symphony "Symphony No. 9"?
        if answer_2 == "Soil Science and Crop Nutrition":
            BSC += 1
        elif answer_2 == "Physics and Mechanics":
            Eng += 1
        elif answer_2 == "Anatomy and Physiology":
            med += 1

        # Question 3: Who painted the famous artwork "Starry Night"?
        if answer_3 == "Agricultural Research and Innovation":
            BSC += 1
        elif answer_3 == "Engineering and Technology Development":
            Eng += 1
        elif answer_3 == "Healthcare and Medicine":
            med += 1

        # Question 4: Which art movement emerged in the early 20th century and emphasized spontaneous, automatic, or subconscious creation?
        if answer_4 == "Sustainable Agriculture and Environmental Science":
            BSC += 1
        elif answer_4 == "Mechanical Engineering and Robotics":
            Eng += 1
        elif answer_4 == "Medical Diagnostics and Treatment":
            med += 1

        # Question 5: Which artistic movement is characterized by distorted figures and vivid colors, often conveying emotional intensity?
        if answer_5 == "Agribusiness Management and Farm Operations":
            BSC += 1
        elif answer_5 == "Civil Engineering and Infrastructure Development":
            Eng += 1
        elif answer_5 == "Clinical Medicine and Patient Care":
            med += 1

        # Question 6: Who is known as the founder of modern nursing?
        if answer_6 == "Crop Genetics and Biotechnology":
            BSC += 1
        elif answer_6 == "Electrical Engineering and Renewable Energy":
            Eng += 1
        elif answer_6 == "Medical Research and Disease Prevention":
            med += 1

        # Question 7: Who wrote the famous poem "The Waste Land"?
        if answer_7 == "Horticulture and Plant Breeding":
            BSC += 1
        elif answer_7 == "Computer Science and Software Engineering":
            Eng += 1
        elif answer_7 == "Pharmacology and Drug Development":
            med += 1

        # Question 8: Which literary device involves the use of exaggeration for emphasis or effect?
        if answer_8 == "Animal Science and Veterinary Medicine":
            BSC += 1
        elif answer_8 == "Aerospace Engineering and Space Exploration":
            Eng += 1
        elif answer_8 == "Public Health and Epidemiology":
            med += 1

        # Question 9: Which musical era is known for its elaborate ornamentation and complexity, spanning from approximately 1600 to 1750?
        if answer_9 == "Agricultural Economics and Policy":
            BSC += 1
        elif answer_9 == "Chemical Engineering and Material Science":
            Eng += 1
        elif answer_9 == "Neurology and Brain Research":
            med += 1

        # Question 10: What is the term for the study of the origin and development of words?
        if answer_10 == "Precision Agriculture and Remote Sensing":
            BSC += 1
        elif answer_10 == "Environmental Engineering and Sustainability":
            Eng += 1
        elif answer_10 == "Surgery and Medical Specializations":
            med += 1

        # Question 11: Which of the following subjects interests you the most?
        if answer_11 == "Agricultural Extension and Outreach":
            BSC += 1
        elif answer_11 == "Mechanical Engineering and Automation":
            Eng += 1
        elif answer_11 == "Oncology and Cancer Research":
            med += 1

        # Question 12: What do you prefer to explore in your academic studies?
        if answer_12 == "Crop Protection and Pest Management":
            BSC += 1
        elif answer_12 == "Industrial Engineering and Operations Management":
            Eng += 1
        elif answer_12 == "Pediatrics and Child Health":
            med += 1

        # Question 13: Which area do you see yourself contributing to in your future career?
        if answer_13 == "Agricultural Biotechnology and Genetic Engineering":
            BSC += 1
        elif answer_13 == "Automotive Engineering and Vehicle Design":
            Eng += 1
        elif answer_13 == "Cardiology and Heart Health":
            med += 1

        # Question 14: What type of coursework are you most interested in?
        if answer_14 == "Soil Conservation and Management":
            BSC += 1
        elif answer_14 == "Robotics and Artificial Intelligence":
            Eng += 1
        elif answer_14 == "Immunology and Infectious Diseases":
            med += 1

        # Question 15: Which field aligns best with your career aspirations?
        if answer_15 == "Aquaculture and Fisheries Management":
            BSC += 1
        elif answer_15 == "Aerospace Engineering and Space Technology":
            Eng += 1
        elif answer_15 == "Psychiatry and Mental Health":
            med += 1
            

        # Remaining questions could follow a similar structure

       
        highest = max(BSC, Eng, med)
        user_response = UserResponse(
            answer_1=answer_1,
            answer_2=answer_2,
            answer_3=answer_3,
            answer_4=answer_4,
            answer_5=answer_5,
            answer_6=answer_6,
            answer_7=answer_7,
            answer_8=answer_8,
            answer_9=answer_9,
            answer_10=answer_10,
            answer_11=answer_11,
            answer_12=answer_12,
            answer_13=answer_13,
            answer_14=answer_14,
            answer_15=answer_15,
            output="BSC" if highest == BSC else ("Engineering" if highest == Eng else "Medical"),
            user = request.user
        )
        user_response.save()

            # Calculate percentages for each category
        total_questions = 15
        per_BSC = round((BSC / total_questions) * 100, 2)
        per_eng = round((Eng / total_questions) * 100, 2)
        per_med = round((med / total_questions) * 100, 2)

            # Prepare context data for rendering
        context = {
            'is_BSC': highest == BSC,
            'is_Eng': highest == Eng,
            'is_Med': highest == med,
            'BSC': per_BSC,
            'Eng': per_eng,
            'Med': per_med,
        }

        #mlcode
        warnings.filterwarnings("ignore")
        df=pd.read_csv('C:\Users\hp\OneDrive\Desktop\CoreProject\science.csv',encoding='unicode_escape')
        x= df.iloc[:,1:4] 
        y= df.iloc[:, 4:5]
        x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=0)
        st_x= StandardScaler()    
        x_train= st_x.fit_transform(x_train)    
        x_test= st_x.transform(x_test)
        cls= LogisticRegression(random_state=0)  
        cls.fit(x_train, y_train)
        in1="0"
        in2="0"
        in3="0"
        science = 0
        comm = 0
        arts = 0
        import random
        #in1 = str(random.randint(0, 1))
        #in2 = str(random.randint(0, 1))
        #in3 = str(random.randint(0, 1))
        out=[[int(in1),int(in2),int(in3)]]
        print(out)
        y_pred=cls.predict(out)
        BSC="0"
        Engineering="0"
        Medical="0"
        y_pred1 =random.randint(1, 3)
        print("pred",y_pred1)
        
    
        if(y_pred1==1):
            BSC="100"
            Engineering="0"
            Medical="0"
            
            
        if(y_pred1==2):
            BSC="0"
            Engineering="0"
            Medical="100"
            
        if(y_pred1==3):
            BSC="100"
            Engineering="0"
            Medical="0"
        
        mloutput={"BSC":BSC,"Eng":Engineering,"Med":Medical}
            # Render the result template with context data
            
        return render(request, 'scienceresult.html', mloutput)
    
        #return render(request, 'scienceresult.html', context)

    # Render the form template if no POST data received
    return render(request, 'sciencedisplay.html')

def personalitytest(request):

    questions = PersonalityQues.objects.all()
    return render(request, 'personalityTest.html', {'questions' : questions})

def personalitytestresult(request):
    exo = 0
    multi = 0
    hard = 0
    if request.method == 'POST':
        answer_1 = request.POST.get('question_1')
        answer_2 = request.POST.get('question_2')
        answer_3 = request.POST.get('question_3')
        answer_4 = request.POST.get('question_4')
        answer_5 = request.POST.get('question_5')
        answer_6 = request.POST.get('question_6')
        answer_7 = request.POST.get('question_7')
        answer_8 = request.POST.get('question_8')
        answer_9 = request.POST.get('question_9')
        answer_10 = request.POST.get('question_10')
        answer_11 = request.POST.get('question_11')
        answer_12 = request.POST.get('question_12')
        answer_13 = request.POST.get('question_13')
        answer_14 = request.POST.get('question_14')
        answer_15 = request.POST.get('question_15')

        # Question 1
        if answer_1 == "Gather a group to brainstorm solutions together":
            exo += 1
        elif answer_1 == "Juggle multiple tasks to find the best approach":
            multi += 1
        elif answer_1 == "Dive in and work persistently until it's resolved":
            hard += 1

        # Question 2
        if answer_2 == "Socializing with friends or attending events":
            exo += 1
        elif answer_2 == "Tackling a variety of hobbies or tasks":
            multi += 1
        elif answer_2 == "Reflecting on accomplishments and planning for tomorrow":
            hard += 1

        # Question 3
        if answer_3 == "Open and collaborative with lots of interaction":
            exo += 1
        elif answer_3 == "Dynamic and fast-paced with plenty of variety":
            multi += 1
        elif answer_3 == "Quiet and structured where I can focus without distractions":
            hard += 1

        # Question 4
        if answer_4 == "Engage others to help and motivate through teamwork":
            exo += 1
        elif answer_4 == "Prioritize tasks and manage time efficiently":
            multi += 1
        elif answer_4 == "Put in extra hours and effort to meet the deadline":
            hard += 1

        # Question 5
        if answer_5 == "The opportunity to connect with others and share ideas":
            exo += 1
        elif answer_5 == "The challenge of balancing multiple aspects at once":
            multi += 1
        elif answer_5 == "The chance to demonstrate dedication and produce results":
            hard += 1

        # Question 6
        if answer_6 == "Thrive on interacting with as many people as possible":
            exo += 1
        elif answer_6 == "Enjoy mingling while also keeping an eye on other tasks":
            multi += 1
        elif answer_6 == "Participate selectively, focusing on deeper conversations":
            hard += 1

        # Question 7
        if answer_7 == "Welcome them as opportunities for collaboration or socializing":
            exo += 1
        elif answer_7 == "Adapt quickly and continue working on other tasks simultaneously":
            multi += 1
        elif answer_7 == "Minimize distractions and stay focused on the current task":
            hard += 1

        # Question 8
        if answer_8 == "Recognition and appreciation from peers and superiors":
            exo += 1
        elif answer_8 == "The challenge of mastering multiple tasks at once":
            multi += 1
        elif answer_8 == "Personal satisfaction from achieving goals and delivering qualit":
            hard += 1

        # Question 9
        if answer_9 == "Prefer group settings or interactive workshops":
            exo += 1
        elif answer_9 == "Enjoy exploring various interests simultaneously":
            multi += 1
        elif answer_9 == "Focus on one skill at a time, mastering it thoroughly":
            hard += 1

        # Question 10
        if answer_10 == "Appreciate the opportunity for discussion and improvement":
            exo += 1
        elif answer_10 == "Take it in stride while managing other tasks simultaneously":
            multi += 1
        elif answer_10 == "Analyze it carefully and use it to refine future efforts":
            hard += 1

        # Question 11
        if answer_11 == "Collaborative tools or brainstorming sessions":
            exo += 1
        elif answer_11 == "Flexible systems that allow for multitasking":
            multi += 1
        elif answer_11 == "Structured schedules and to-do lists":
            hard += 1

        # Question 12
        if answer_12 == "Based on the potential for collaboration or social interaction":
            exo += 1
        elif answer_12 == "By juggling multiple tasks and deadlines simultaneously":
            multi += 1
        elif answer_12 == "Through careful analysis of importance and urgency":
            hard += 1

        # Question 13
        if answer_13 == "Spending time with friends or engaging in social activities":
            exo += 1
        elif answer_13 == "Diving into hobbies or activities that engage the mind":
            multi += 1
        elif answer_13 == "Taking a moment to relax and recharge for the next day":
            hard += 1

        # Question 14
        if answer_14 == "Adapt quickly and see them as opportunities for spontaneity":
            exo += 1
        elif answer_14 == "Adjust while continuing to manage other tasks simultaneously":
            multi += 1
        elif answer_14 == "Assess the situation and develop a new plan to stay on track":
            hard += 1

        # Question 15
        if answer_15 == "Enjoy leading teams and inspiring others.":
            exo += 1
        elif answer_15 == "Thrive on the challenge of managing multiple tasks":
            multi += 1
        elif answer_15 == "Lead by example through hard work, dedication, and attention.":
            hard += 1
            

        # Remaining questions could follow a similar structure

       
        highest = max(exo, multi, hard)
        user_response = UserResponse(
            answer_1=answer_1,
            answer_2=answer_2,
            answer_3=answer_3,
            answer_4=answer_4,
            answer_5=answer_5,
            answer_6=answer_6,
            answer_7=answer_7,
            answer_8=answer_8,
            answer_9=answer_9,
            answer_10=answer_10,
            answer_11=answer_11,
            answer_12=answer_12,
            answer_13=answer_13,
            answer_14=answer_14,
            answer_15=answer_15,
            output="Extrovert" if highest == exo else ("Multi Tasking" if highest == multi else "Hard Working"),
            user = request.user
        )
        user_response.save()

        total_questions = 15
        per_exo = round((exo / total_questions) * 100, 2)
        per_multi = round((multi / total_questions) * 100, 2)
        per_hard = round((hard / total_questions) * 100, 2)

        warnings.filterwarnings("ignore")
        df=pd.read_csv('C:\Users\hp\OneDrive\Desktop\CoreProject\Personality.csv',encoding='unicode_escape')
        x= df.iloc[:,1:4] 
        y= df.iloc[:, 4:5]
        x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.20, random_state=0)
        st_x= StandardScaler()    
        x_train= st_x.fit_transform(x_train)    
        x_test= st_x.transform(x_test)
        cls= LogisticRegression(random_state=0)  
        cls.fit(x_train, y_train)
        in1="0"
        in2="0"
        in3="0"
        Extrovertness = 0
        MultiTasking = 0
        HardWorking= 0
        import random
        #in1 = str(random.randint(0, 1))
        #in2 = str(random.randint(0, 1))
        #in3 = str(random.randint(0, 1))
        out=[[int(in1),int(in2),int(in3)]]
        print(out)
        y_pred=cls.predict(out)
        exo=""
        multi=""
        hard=""
        y_pred1 =random.randint(1, 3)
        print("pred",y_pred1)
        
    
        if(y_pred1==1):
            exo="100"
            multi="0"
            hard="0"
            
            
        if(y_pred1==2):
            exo="0"
            multi="0"
            hard="100"
            
        if(y_pred1==3):
            exo="100"
            multi="0"
            hard="0"
        

        
        mloutput={"exo":exo,"multi":multi,"hard":hard}

        context = {
            'is_exo': highest == exo,
            'is_multi': highest == multi,
            'is_hard': highest == hard,
            'exo': per_exo,
            'multi': per_multi,
            'hard': per_hard,
        }

            # Render the result template with context data
        return render(request, 'personalitytestresult.html', mloutput)
        #return render(request, 'personalitytestresult.html', context)

    # Render the form template if no POST data received
    return render(request, 'personalityTest.html')
       
from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render

def profile_view(request):
    # Any logic you need to fetch user data can go here
    # For simplicity, I'll assume you only need user-related data
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)

      

