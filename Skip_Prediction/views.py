from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import numpy as np
import pandas as pd
from datetime import datetime


# Create your views here.

#request handler
result=[]
Track_Features_df=pd.read_csv('tf_mini.csv')
model = pickle.load(open('DT.pkl', 'rb'))

def prepare_data_for_model(request_list):
    track_id=request_list[0]
    Track_Features=Track_Features_df[Track_Features_df['track_id']==track_id][['duration', 'release_year',
       'us_popularity_estimate', 'acousticness', 'beat_strength', 'bounciness',
       'danceability', 'dyn_range_mean', 'energy', 'flatness',
       'instrumentalness', 'key', 'liveness', 'loudness', 'mechanism', 'mode',
       'organism', 'speechiness', 'tempo', 'time_signature', 'valence',
       'acoustic_vector_0', 'acoustic_vector_1', 'acoustic_vector_2',
       'acoustic_vector_3', 'acoustic_vector_4', 'acoustic_vector_5',
       'acoustic_vector_6', 'acoustic_vector_7']].values[0]
    
    date_time_str = request_list[12]
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
    day=date_time_obj.day
    month=date_time_obj.month
    year=date_time_obj.year    

    if (Track_Features[15]=='major'):
        Track_Features[15]=0
    else:
        Track_Features[15]=1


    datatofeedmodel=np.concatenate((request_list[1:-1],[day,month,year],Track_Features))
    return datatofeedmodel

def say_hello(request):
    return render(request,'Home.html',{'name':'aboda'})

def secondpage(request):
    return render(request,'EnterFeaures.html')

@csrf_exempt
def resultpage(request):
    if request.method == 'POST':
        Data=list(request.POST.dict().values())
        state=valid(Data)
        if  state=='valid':
            result=predict(prepare_data_for_model(Data))
            return render(request,'resultpage.html',{'name':result})
        else:     return render(request,'EnterFeaures.html',{'message':state})



def predict(Data):
    prediction = model.predict(np.array(Data).reshape(1, -1))
    if prediction==1:
        return 'skipped'
    if prediction==0:
        return 'not skipped'

def valid(Data):

    track_id=Data[0]
    Track_Features_df[Track_Features_df['track_id']==track_id]
    if len(Track_Features_df[Track_Features_df['track_id']==track_id].values)==0 :
        return 'please enter valid Track ID'
    sesseion_lenght=Data[1]
    session_position=Data[2]
    hourofday=Data[7]
    if sesseion_lenght =='' or session_position=='' or hourofday=='':
        return 'please complete the form'
    return 'valid'
