from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.db import connection
from collections import namedtuple
from itertools import izip
import csv, sqlite3, os

from .models import Population, StateCode, Sex, Race, Economy, Business, Employment, HealthInsurance, Housing, Income

def index(request):
    states = []
    states = returnstates("test")
    years = range(2010, 2015)
    context = {'states': states, 'years': years}
    return render(request, 'dbproject/index.html', context)


def singlequery(request):
    table_name = request.POST['table']
    state = StateCode.objects.get(state_name=request.POST['state'])
    if table_name == "Population":
        single = Population.objects.get(year=request.POST['year'], state=state.numeric_code)
        context = {'single': single, 'state': request.POST['state']}
    if table_name == "Sex":
        single = Sex.objects.get(year=request.POST['year'], state=state.numeric_code)
        context = {'single': single, 'state': request.POST['state']}
    if table_name == "Race":
        single = Race.objects.get(year=request.POST['year'], state=state.numeric_code)
        context = {'single': single, 'state': request.POST['state']}
    if table_name == "Economy":
        try:
            single = Economy.objects.get(year=request.POST['year'], state=state.numeric_code)
            context = {'single': single, 'state': request.POST['state']}
        except Economy.DoesNotExist:
            error_message = "Sorry, no information for this year."
            context = {'error_message': error_message}
    if table_name == "Business":
        try:
            single = Business.objects.get(year=request.POST['year'], state=state.numeric_code)
            context = {'single': single, 'state': request.POST['state']}
        except Business.DoesNotExist:
            error_message = "Sorry, no information for this year."
            context = {'error_message': error_message}
    if table_name == "Employment":
        single = Employment.objects.get(year=request.POST['year'], state=state.numeric_code)
        context = {'single': single, 'state': request.POST['state']}
    if table_name == "HealthInsurance":
        try:
            single = HealthInsurance.objects.get(year=request.POST['year'], state=state.numeric_code)
            context = {'single': single, 'state': request.POST['state']}
        except HealthInsurance.DoesNotExist:
            error_message = "Sorry, no information for this year."
            context = {'error_message': error_message}
    if table_name == "Housing":
        single = Housing.objects.get(year=request.POST['year'], state=state.numeric_code)
        context = {'single': single, 'state': request.POST['state']}
    if table_name == "Income":
        single = Income.objects.get(year=request.POST['year'], state=state.numeric_code)
        context = {'single': single, 'state': request.POST['state']}
    
    return render(request, 'dbproject/single.html', context)

def customquery(request):
    try:
        query = request.POST['query_sentence']
        cursor = connection.cursor()
        cursor.execute(query)
        results = namedtuplefetchall(cursor)
        p = results[0]
        names = p._fields
        row = 0
        col = 0
        values = [[0 for x in range(len(names))] for x in range(len(results))] 
        for p in results:
            for name in p._fields:
                if name == "state":
                    state = StateCode.objects.get(numeric_code=getattr(p, name))
                    values[row][col] = state.state_name
                    col += 1
                else:
                    values[row][col] = getattr(p, name)
                    col += 1
            row += 1
            col = 0
        print(values[0])
        context = {'names': names, 'values': values}
        return render(request, 'dbproject/customquery.html', context)
    except :
        context = {'error_message': "There may be some error in the query sentence."}
        return render(request, 'dbproject/customquery.html', context)

def prediction(request):
    try:
        pGDP = float(request.POST['gdp'])
        mHIncome = pGDP * 0.88818
        context = {'mHIncome': mHIncome, 'pGDP': pGDP}
        return render(request, 'dbproject/prediction.html', context)
    except :
        context = {'error_message': "Please type in valid float number."}
        return render(request, 'dbproject/prediction.html', context)
    
def returnstates(params):
    states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
    "Connecticut", "Delaware", "District Of Columbia", "Florida", "Georgia", "Hawaii", 
    "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", 
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", 
    "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", 
    "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", 
    "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", 
    "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", 
    "Wyoming"]
    return states

def impcsv(request):
    states=[]
    states = returnstates("test")
    years = range(2010, 2015)
    context = {'states': states, 'years': years, 'imported': "imported"}

    StateCode.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'StateCode.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            StateCode.objects.create(
                state_name=row[0],
                alpha_code=row[1],
                numeric_code=row[2]
                )

    Population.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Population.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Population.objects.create(
                state=row[0],
                year=row[1],
                age0_5=row[2],
                age6_17=row[3],
                age18_64=row[4],
                age65=row[5],
                agetotal=row[6],
                )

    Sex.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Sex.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Sex.objects.create(
                state=row[0],
                year=row[1],
                male=row[2],
                female=row[3]
                )

    Race.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Race.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Race.objects.create(
                state=row[0],
                year=row[1],
                white=row[2],
                black=row[3],
                asian=row[4],
                native_american=row[5],
                other=row[6]
                )

    Economy.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Economy.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Economy.objects.create(
                state=row[0],
                year=row[1],
                gdp=row[2]
                )

    Business.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Business.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Business.objects.create(
                state=row[0],
                year=row[1],
                num_firms=row[2],
                num_employees=row[3],
                payroll=row[4],
                )

    Employment.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Employment.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Employment.objects.create(
                state=row[0],
                year=row[1],
                unemployment=row[2],
                )

    HealthInsurance.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'HealthInsurance.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            HealthInsurance.objects.create(
                state=row[0],
                year=row[1],
                uninsured_rate=row[2],
                )

    Housing.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Housing.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Housing.objects.create(
                state=row[0],
                year=row[1],
                homeownership_rate=row[2],
                )

    Income.objects.all().delete()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Income.csv'))
    with open(file_path) as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Income.objects.create(
                state=row[0],
                year=row[1],
                median_hhincome=row[2],
                poverty_rate=row[3],
                )
    return render(request, 'dbproject/index.html', context)

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    print(nt_result)
    return [nt_result(*row) for row in cursor.fetchall()]
