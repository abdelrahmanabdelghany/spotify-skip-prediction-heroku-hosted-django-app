# Spotify-Skip-Action-Predition-using-Sequencial-User-Data-and-Acoustic-Features-Data

## Prepared by *TEAM B/RAJA BEN HARRAF*
Raja BEN HARRAF
Noureddine ARAB
Abdelrahman ABDELGHANY
Ramsha KAMRAN
Youness AITHASSOUNE
Mohamed ADEL MOHMOUD MOHAMED GOUDA 
  

## Project description

The skip button plays a large role in the user’s experience, as they are free to abandon songs as they choose. Music providers are also incentivized to recommend songs that their users like in order to increase user experience and time spent on the platform.

The goal of the project is to predict the likelihood of a user skipping any given song during a listening session based on Audio & User features.

## Preprocessing 

Data preprocessing is a data mining technique that involves transforming raw data into an understandable format. Real-world data is often incomplete, inconsistent, and/or lacking in certain behaviors or trends, and is likely to contain many errors. Data preprocessing is a proven method of resolving such issues. Data preprocessing prepares raw data for further processing.
## Why preprocessing?
Real-world data are generally:
- **Incomplete**: lacking attribute values, lacking certain attributes of interest, or containing only aggregate data
- **Noisy**: containing errors or outliers
- **Inconsistent**: containing discrepancies in codes or names
Tasks in data preprocessing:
- **Data cleaning**: fill in missing values, smooth noisy data, identify or remove outliers, and resolve inconsistencies.
- **Data integration**: using multiple databases, data cubes, or files.
- **Data transformation**: normalization and aggregation.
- **Data reduction**: reducing the volume but producing the same or similar analytical results.
- **Data discretization**: part of data reduction, replacing numerical attributes with nominal ones.
## Tools used:
## **Lower casing:**
Lower casing is a common text preprocessing technique. The idea is to convert the input text into same casing format so that 'text', 'Text' and 'TEXT' are treated the same way. We converted all the text of the datasets into lower case.
## **Removal of Punctuations:**
One another common text preprocessing technique is to remove the punctuations from the text data. This is again a text standardization process that will help to treat 'hurray' and 'hurray!' in the same way.
We also need to carefully choose the list of punctuations to exclude depending on the use case. For example, the string.punctuation in python contains the following punctuation symbols
!"#$%&\'()\*+,-./:;<=>?@[\\]^\_{|}~`
We can add or remove more punctuations as per our need

## Removal of stop words:
Stopwords are commonly occuring words in a language like 'the', 'a' and so on. They can be removed from the text most of the times, as they don't provide valuable information for downstream analysis. In cases like Part of Speech tagging, we should not remove them as provide very valuable information about the POS.

These stopword lists are already compiled for different languages and we can safely use them. For example, the stopword list for english language from the nltk package can be seen below.

**Lower casing:**

Lower casing is a common text preprocessing technique. The idea is to convert the input text into same casing format so that 'text', 'Text' and 'TEXT' are treated the same way. We converted all the text of the datasets into lower case.

## **Removal of Punctuations:**
One another common text preprocessing technique is to remove the punctuations from the text data. This is again a text standardization process that will help to treat 'hurray' and 'hurray!' in the same way.

We also need to carefully choose the list of punctuations to exclude depending on the use case. For example, the string.punctuation in python contains the following punctuation symbols

!"#$%&\'()\*+,-./:;<=>?@[\\]^\_{|}~`

## **Removal of Frequent words:**
In the previous preprocessing step, we removed the stop words based on language information. But say, if we have a domain specific corpus, we might also have some frequent words which are of not so much importance to us.

So this step is to remove the frequent words in the given corpus. If we use something like tfidf, this is automatically taken care of.

## **Removal of Rare words:**
This is very similar to previous preprocessing step but we will remove the rare words from the corpus.
## **Stemming:**
Stemming is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form

## **Lemmatization:**
Lemmatization is similar to stemming in reducing inflected words to their word stem but differs in the way that it makes sure the root word (also called as lemma) belongs to the language.

As a result, this one is generally slower than stemming process. So depending on the speed requirement, we can choose to use either stemming or lemmatization.

## EDA && Feature engineering 

Exploratory data analysis (EDA) is an approach of analyzing data sets to summarize their main characteristics, often using statistical graphics and other data visualization methods.

- **merged_data** dataset comprises of 335760 rows and 50 columns.
- Dataset comprises of Continuous variable and integer data type and float data type and object data type (String) 
and Boolean data type. 
- Dataset column variables: 'session_id', 'session_position', 'session_length', 'track_id', 'skip_1', 'skip_2', 'skip_3', 'not_skipped', 'context_switch',
 'no_pause_before_play', 'short_pause_before_play','long_pause_before_play', 'hist_user_behavior_n_seekfwd',
 'hist_user_behavior_n_seekback', 'hist_user_behavior_is_shuffle', 'hour_of_day', 'date', 'premium', 'context_type',
 'hist_user_behavior_reason_start', 'hist_user_behavior_reason_end', 'duration', 'release_year', 'us_popularity_estimate', 'acousticness',
'beat_strength', 'bounciness', 'danceability', 'dyn_range_mean', 'energy', 'flatness', 'instrumentalness', 'key', 'liveness', 'loudness',
'mechanism', 'mode', 'organism', 'speechiness', 'tempo', 'time_signature', 'valence', 'acoustic_vector_0', 'acoustic_vector_1',
'acoustic_vector_2', 'acoustic_vector_3', 'acoustic_vector_4', 'acoustic_vector_5', 'acoustic_vector_6', 'acoustic_vector_7' 
**Information of Dataset:**
- Using describe() function We get the information of data such as mean, count, max, min... etc
 	session_position 	session_length 	context_switch ....       acoustic_vector_7	
count 	335760.000000 	335760.000000 	335760.000000 	335760.000000                
mean 	9.325911 	                  17.651823 	                   0.040904 		0.059859
std 	5.457630 	                  3.422020 	                   0.198069 		0.261958
min 	1.000000 	                  10.000000 	                   0.000000 		-0.975647
25% 	5.000000 	                  15.000000 	                   0.000000 		-0.020752
50% 	9.000000 	                  20.000000 	                   0.000000 		0.143839
75% 	14.000000 	                  20.000000 	                   0.000000 		0.194377
max 	20.000000 	                  20.000000 	                    1.000000 		1.152213

**Correlation Plot of Numerical Variables:**
- Some continuous variables are strong correlation because the value between 0.82 to 1 correlation.
- We find out that the three columns skip1 and skip2 and skip3 can replace them with new column is skipped
which is sum of three columns (skip1,skip2,skip3).
** Drop the features which are weak correlation with output
- Drop the features is:  'skip_1', 'skip_2', 'skip_3', 'session_id', 'session_position', 'session_length', 'track_id'
- Drop column 'not skipped'.
** Using one hot encoder 
- To convert Values of Object data types into Columns Boolean data types 0 if not found or 1 if found.

## Model Building

#### Metrics considered for Model Evaluation
**Accuracy , Precision , Recall and F1 Score**
- Accuracy: What proportion of actual positives and negatives is correctly classified?
- Precision: What proportion of predicted positives are truly positive ?
- Recall: What proportion of actual positives is correctly classified ?
- F1 Score : Harmonic mean of Precision and Recall

#### Logistic Regression
- Logistic Regression helps find how probabilities are changed with actions.
- The function is defined as P(y) = 1 / 1+e^-(A+Bx) 
- Logistic regression involves finding the **best fit S-curve** where A is the intercept and B is the regression coefficient. The output of logistic regression is a probability score.
  precision    recall  f1-score   support

         0.0       0.98      0.96      0.97     11767
         1.0       0.98      0.99      0.98     21809

    accuracy                           0.98     33576
   macro avg       0.98      0.97      0.98     33576
weighted avg       0.98      0.98      0.98     33576

### SVM 
A support vector machine is a supervised learning algorithm that sorts data into two categories. It is trained with a series of data already classified into two categories, building the model as it is initially trained. The task of an SVM algorithm is to determine which category a new data point belongs in. This makes SVM a kind of non-binary linear classifier.
  precision    recall  f1-score   support

         0.0       0.98      0.96      0.97     11819
         1.0       0.98      0.99      0.98     21757

    accuracy                           0.98     33576
   macro avg       0.98      0.97      0.98     33576
weighted avg       0.98      0.98      0.98     33576

### KNN 
A k-nearest-neighbor algorithm, often abbreviated k-nn, is an approach to data classification that estimates how likely a data point is to be a member of one group or the other depending on what group the data points nearest to it are in.

The k-nearest-neighbor is an example of a "lazy learner" algorithm, meaning that it does not build a model using the training set until a query of the data set is performed.
Classification Report:
              precision    recall  f1-score   support

         0.0       0.97      0.95      0.96      5848
         1.0       0.97      0.99      0.98     10940

    accuracy                           0.97     16788
   macro avg       0.97      0.97      0.97     16788
weighted avg       0.97      0.97      0.97     16788

Accuracy: 0.9731355730283536.

### GBT
Gradient boosting is a type of machine learning boosting. It relies heavily on the prediction that the next model will reduce prediction errors when mixed with the previous ones. The main idea is to establish target results for this next model to minimize errors
Accuracy: 0.9864582386621829

### LSTM
Long short-term memory (LSTM) units or blocks are part of a recurrent neural network structure. Recurrent neural networks are made to utilize certain types of artificial memory processes that can help these artificial intelligence programs to more effectively imitate human thought
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 lstm_1 (LSTM)               (None, 100)               40800     
                                                                 
 dense_1 (Dense)             (None, 1)                 101       
                                                                 
=================================================================
Total params: 40,901
Trainable params: 40,901
Non-trainable params: 0
_________________________________________________________________
None
Epoch 1/20
1679/1679 [==============================] - 74s 43ms/step - loss: 7.3347 - accuracy: 0.5561 - val_loss: 0.9554 - val_accuracy: 0.6123
Epoch 2/20
1679/1679 [==============================] - 73s 43ms/step - loss: 0.7205 - accuracy: 0.6111 - val_loss: 0.7124 - val_accuracy: 0.6466
Epoch 3/20
1679/1679 [==============================] - 76s 45ms/step - loss: 0.6664 - accuracy: 0.6324 - val_loss: 0.6971 - val_accuracy: 0.6463
Epoch 4/20
1679/1679 [==============================] - 76s 46ms/step - loss: 0.6316 - accuracy: 0.6616 - val_loss: 0.6018 - val_accuracy: 0.6492
Epoch 5/20
1679/1679 [==============================] - 75s 45ms/step - loss: 0.6662 - accuracy: 0.6389 - val_loss: 0.9150 - val_accuracy: 0.3579
Epoch 6/20
1679/1679 [==============================] - 75s 44ms/step - loss: 5632.7573 - accuracy: 0.6072 - val_loss: 108.5883 - val_accuracy: 0.3535
Epoch 7/20
1679/1679 [==============================] - 76s 45ms/step - loss: 127.5738 - accuracy: 0.5439 - val_loss: 151.6456 - val_accuracy: 0.6466
Epoch 8/20
1679/1679 [==============================] - 77s 46ms/step - loss: 2979.7505 - accuracy: 0.5388 - val_loss: 2.8943 - val_accuracy: 0.6193
Epoch 9/20
1679/1679 [==============================] - 76s 45ms/step - loss: 11.3972 - accuracy: 0.5471 - val_loss: 9.1382 - val_accuracy: 0.3645
Epoch 10/20
1679/1679 [==============================] - 73s 44ms/step - loss: 13.1408 - accuracy: 0.5475 - val_loss: 25.0041 - val_accuracy: 0.3543
Epoch 11/20
1679/1679 [==============================] - 73s 44ms/step - loss: 14.7210 - accuracy: 0.5475 - val_loss: 26.9177 - val_accuracy: 0.6466
Epoch 12/20
1679/1679 [==============================] - 77s 46ms/step - loss: 17.2189 - accuracy: 0.5483 - val_loss: 11.5382 - val_accuracy: 0.6465
Epoch 13/20
1679/1679 [==============================] - 76s 45ms/step - loss: 17585006.0000 - accuracy: 0.5361 - val_loss: 28.0978 - val_accuracy: 0.3796
Epoch 14/20
1679/1679 [==============================] - 75s 45ms/step - loss: 65.6637 - accuracy: 0.5377 - val_loss: 46.0060 - val_accuracy: 0.6339
Epoch 15/20
1679/1679 [==============================] - 74s 44ms/step - loss: 9.9854 - accuracy: 0.5466 - val_loss: 3.1883 - val_accuracy: 0.6381
Epoch 16/20
1679/1679 [==============================] - 73s 43ms/step - loss: 8.3542 - accuracy: 0.5500 - val_loss: 5.4649 - val_accuracy: 0.6424
Epoch 17/20
1679/1679 [==============================] - 73s 44ms/step - loss: 57626.6367 - accuracy: 0.5236 - val_loss: 0.8353 - val_accuracy: 0.6407
Epoch 18/20
1679/1679 [==============================] - 73s 43ms/step - loss: 0.7648 - accuracy: 0.5908 - val_loss: 0.7208 - val_accuracy: 0.5824
Epoch 19/20
1679/1679 [==============================] - 72s 43ms/step - loss: 0.7287 - accuracy: 0.5927 - val_loss: 0.7205 - val_accuracy: 0.6454
Epoch 20/20
1679/1679 [==============================] - 73s 43ms/step - loss: 0.7791 - accuracy: 0.5781 - val_loss: 0.7185 - val_accuracy: 0.6119
Accuracy: 60.99%

### BILSTM
A Bidirectional LSTM, or biLSTM, is a sequence processing model that consists of two LSTMs: one taking the input in a forward direction, and the other in a backwards direction. BiLSTMs effectively increase the amount of information available to the network, improving the context available to the algorithm (e.g. knowing what words immediately follow and precede a word in a sentence).
Epoch 1/20
1679/1679 [==============================] - 122s 71ms/step - loss: 0.7327 - accuracy: 0.6536 - val_loss: 0.4210 - val_accuracy: 0.9522
Epoch 2/20
1679/1679 [==============================] - 114s 68ms/step - loss: 0.1103 - accuracy: 0.9759 - val_loss: 0.1056 - val_accuracy: 0.9764
Epoch 3/20
1679/1679 [==============================] - 116s 69ms/step - loss: 0.2001 - accuracy: 0.9598 - val_loss: 0.1063 - val_accuracy: 0.9761
Epoch 4/20
1679/1679 [==============================] - 116s 69ms/step - loss: 1911.3254 - accuracy: 0.8621 - val_loss: 136.9028 - val_accuracy: 0.6466
Epoch 5/20
1679/1679 [==============================] - 117s 70ms/step - loss: 170.5498 - accuracy: 0.5435 - val_loss: 110.9774 - val_accuracy: 0.6466
Epoch 6/20
1679/1679 [==============================] - 117s 70ms/step - loss: 160.5412 - accuracy: 0.5447 - val_loss: 216.7508 - val_accuracy: 0.3534
Epoch 7/20
1679/1679 [==============================] - 116s 69ms/step - loss: 1336.1438 - accuracy: 0.5441 - val_loss: 52.4965 - val_accuracy: 0.6466
Epoch 8/20
1679/1679 [==============================] - 119s 71ms/step - loss: 224.7240 - accuracy: 0.5433 - val_loss: 88.9539 - val_accuracy: 0.6466
Epoch 9/20
1679/1679 [==============================] - 118s 70ms/step - loss: 259.7024 - accuracy: 0.5470 - val_loss: 237.4538 - val_accuracy: 0.3534
Epoch 10/20
1679/1679 [==============================] - 115s 69ms/step - loss: 140.3589 - accuracy: 0.5456 - val_loss: 264.6967 - val_accuracy: 0.3534
Epoch 11/20
1679/1679 [==============================] - 115s 69ms/step - loss: 65.6149 - accuracy: 0.5450 - val_loss: 23.6122 - val_accuracy: 0.6466
Epoch 12/20
1679/1679 [==============================] - 117s 70ms/step - loss: 94.2172 - accuracy: 0.5435 - val_loss: 82.1486 - val_accuracy: 0.3534
Epoch 13/20
1679/1679 [==============================] - 115s 69ms/step - loss: 21.0985 - accuracy: 0.5393 - val_loss: 1.9774 - val_accuracy: 0.3827
Epoch 14/20
1679/1679 [==============================] - 115s 69ms/step - loss: 3.3314 - accuracy: 0.5448 - val_loss: 2.5085 - val_accuracy: 0.6464
Epoch 15/20
1679/1679 [==============================] - 116s 69ms/step - loss: 1.9823 - accuracy: 0.5557 - val_loss: 0.9374 - val_accuracy: 0.6273
Epoch 16/20
1679/1679 [==============================] - 115s 69ms/step - loss: 2.5404 - accuracy: 0.5589 - val_loss: 3.2449 - val_accuracy: 0.3543
Epoch 17/20
1679/1679 [==============================] - 115s 69ms/step - loss: 0.4760 - accuracy: 0.8953 - val_loss: 0.1123 - val_accuracy: 0.9797
Epoch 18/20
1679/1679 [==============================] - 117s 70ms/step - loss: 0.3055 - accuracy: 0.9677 - val_loss: 1.0442 - val_accuracy: 0.9764
Epoch 19/20
1679/1679 [==============================] - 116s 69ms/step - loss: 0.4145 - accuracy: 0.9630 - val_loss: 0.2981 - val_accuracy: 0.9741
Epoch 20/20
1679/1679 [==============================] - 116s 69ms/step - loss: 0.2343 - accuracy: 0.9745 - val_loss: 0.1539 - val_accuracy: 0.9788
Accuracy: 97.86%

## Deployment

### Django
We created our app by using Django , then deployed it to Heroku.

Django is a framework to create web applications using python code.

Heroku_ is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

The application asks the user to enter some features of the the track needed to be tested for skiping. The application then use these data and the decision tree model to predict if the song will be skipped or not.

The files of this part are located at this repo [Django project](https://github.com/RajaBen/Spotify-Skip-Action-Predition-using-Sequencial-User-Data-and-Acoustic-Features-Data/blob/TEAM_B/RAJA_BEN_HARRAF/spotify-skip-prediction-heroku-hosted-django-app-master.rar/). You can access the app by following this link : [spotify-skip-prediction](https://spotify-skip-prediction-dt.herokuapp.com/)

### Flask 
We also create our app   by using flask , then deployed it to Heroku . The files of this part are located into (Flask_deployment) folder. You can access the app by following this link : [Flask project](https://github.com/RajaBen/Spotify-Skip-Action-Predition-using-Sequencial-User-Data-and-Acoustic-Features-Data/blob/TEAM_B/RAJA_BEN_HARRAF/Flask_deployment.rar/)
