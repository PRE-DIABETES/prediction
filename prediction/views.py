from pyexpat import model
from django.shortcuts import  render, redirect
from .models import *

from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
import csv
from django.contrib.auth.models import auth
from django.db.models import Q
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'prediction/index.html')

def signin(request):
    return render(request,'prediction/login.html')

def Viewpred(request):
    predictions = PredictionTable.objects.all()
    context = {
        'predictions': predictions
    }
    return render(request,'prediction/Viewpred.html', context)



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				print(user.is_staff)
				if user.is_staff == False:
					return redirect("inner")
				else:
					return redirect("/admin/")

			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="prediction/login.html", context={"login_form":form})

def registration(request):
    context = {}
    context['form'] = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('login')
        else:
            context['form'] = form
    return render(request,'prediction/register1.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
def inner(request):
    return render(request,'prediction/prediction.html')

	# def home(request):
    # return django.shortcuts.render(request, 'home.html')



@login_required(login_url = 'login')
def result(request):
    cell_df = pd.read_csv('diabetes_data_upload.csv')

    cell_df['Gender'] = cell_df['Gender'].replace(['Male', 'Female'], [0, 1])
    cell_df['class'] = cell_df['class'].replace(['Negative', 'Positive'], [0, 1])
    cell_df["Polyuria"] = cell_df["Polyuria"].astype(int)
    cell_df["Polydipsia"] = cell_df["Polydipsia"].astype(int)
    cell_df["sudden weight loss"] = cell_df["sudden weight loss"].astype(int)
    cell_df["weakness"] = cell_df["weakness"].astype(int)
    cell_df["Polyphagia"] = cell_df["Polyphagia"].astype(int)
    cell_df["Genital thrush"] = cell_df["Genital thrush"].astype(int)
    cell_df["visual blurring"] = cell_df["visual blurring"].astype(int)
    cell_df["Itching"] = cell_df["Itching"].astype(int)
    cell_df["Irritability"] = cell_df["Irritability"].astype(int)
    cell_df["delayed healing"] = cell_df["delayed healing"].astype(int)
    cell_df["partial paresis"] = cell_df["partial paresis"].astype(int)
    cell_df["muscle stiffness"] = cell_df["muscle stiffness"].astype(int)
    cell_df["Alopecia"] = cell_df["Alopecia"].astype(int)
    cell_df["Obesity"] = cell_df["Obesity"].astype(int)

    # cell_df.columns

    feature_df = cell_df[['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',
                          'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
                          'Itching', 'Irritability', 'delayed healing', 'partial paresis',
                          'muscle stiffness', 'Alopecia', 'Obesity']]
    # Independent Variables
    X = np.asarray(feature_df)
    # Dependent variable
    y = np.asarray(cell_df['class'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=5)
    

    classifier = svm.SVC(kernel='linear', gamma='auto', C=2)
    classifier.fit(X_train, y_train)

    val1 = request.GET['n1']
    val2 = request.GET['n2']
    val3 = request.GET['n3']
    val4 = request.GET['n4']
    val5 = request.GET['n5']
    val6 = request.GET['n6']
    val7 = request.GET['n7']
    val8 = request.GET['n8']
    val9 = request.GET['n9']
    val10 = request.GET['n10']
    val11 = request.GET['n11']
    val12 = request.GET['n12']
    val13 = request.GET['n13']
    val14 = request.GET['n14']
    val15 = request.GET['n15']
    val16 = request.GET['n16']

    
    data = PredictionTable.objects.create(
        
        Age= val1,
        Sex = val2,
        Excessive_urine= val3,
        Excessive_thirst = val4,
        Sudden_Weight_loss= val5,
        Weakness = val6,
        Excessive_eating= val7,
        Yeast_infection = val8,
        Visual_blurring = val9,
        Itching= val10,
        Irritability = val11,
        Delaed_healing= val12,
        Partial_paresis = val13,
        Muscle_stiffiness= val14,
        Hair_loss = val15,
        Obesity= val16
     )
    
    data.save()

    
    pred = classifier.predict(
        [[val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13, val14, val15, val16]])

    result1 = ""

    if pred == [1]:
        result1 = "You have 93% risks of having diabetes,You can reach to your nearest hospital to take a test! "
    else:
        result1 = "You have no risk of diabetes "
    
    
    context = {
       
        'result2': result1
    }
    return render(request, 'prediction/prediction.html', context)


@login_required(login_url = 'login')
def predict(request):
    form = PredictionTable()

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }
    return render(request, 'prediction/prediction.html', context)


    # @app.route('/', methods=['GET', 'POST'])

    # def index():
    #     if request.method == 'POST':
    #         name = request.form['name']
    #     email = request.form['email']
    #     message = request.form['message']
    #     user_input = UserInput(name=name, email=email, message=message)
    #     db.session.add(user_input)
    #     db.session.commit()
    #     return 'Success!'
    # return render_template('index.html')



    
