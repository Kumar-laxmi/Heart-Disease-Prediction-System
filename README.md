# Heart-Disease-Prediction-System
Heart Disease Prediction System using Machine Learning

## Abstract 
<p> 
  Now days, Heart disease is the most common disease. But, unfortunately the treatment of heart
disease is somewhat costly that is not affordable by common man. Hence, we can reduce this
problem in some amount just by predicting heart disease before it becomes dangerous
using Heart Disease Prediction System Using Machine Learning and Data mining. If we can
find out heart disease problem in early stages then it becomes very helpful for
treatment. Machine Learning and Data Mining techniques are used for the construction
of Heart Disease Prediction System. In healthcare biomedical field, there is large use of heath
care data in the form of text, images, etc but, that data is hardly visited and is not mined. So,
we can avoid this problem by introducing Heart Disease Prediction System. This system will
help us reduce the costs and to enhance the quality treatment of heart patients. This system can
able to identify complex problems and can able to take intelligent medical decisions. The
system can predict likelihood of patients of getting heart problems by their profiles such as
blood pressure, age, sex, cholesterol and blood sugar. Also, the performance will be compared
by calculation of confusion matrix. This can help to calculate accuracy, precision, and recall.
The overall system provides high performance and better accuracy. 
</p>

## Introduction
<p>
  The health care industries collect huge amounts of data that contain some hidden information,
which is useful for making effective decisions. For providing appropriate results and making
effective decisions on data, some advanced data mining techniques are used. In this study, a
Heart Disease Prediction System (HDPS) is developed using Naives Bayes and Decision Tree
algorithms for predicting the risk level of heart disease. The system uses 13 medical parameters
such as age, sex, blood pressure, cholesterol, and obesity for prediction. The HDPS predicts
the likelihood of patients getting heart disease. It enables significant knowledge. E.g.
Relationships between medical factors related to heart disease and patterns, to be established.
We have employed the multilayer perceptron neural network with back propagation as the
training algorithm. The obtained results have illustrated that the designed diagnostic system
can effectively predict the risk level of heart diseases.
</p>

### Aim
<p> 
  To predict heart disease according to input parameter values provided by user and dataset
stored in database.
</p>

### Objective
<p>
  The main objective of this project is to develop a heart disease prediction system. The system
can discover and extract hidden knowledge associated with diseases from a historical heart data
set Heart disease prediction system aims to exploit data mining techniques on medical data set
to assist in the prediction of the heart diseases.
</p>

### Project Scope
<p>
  The project has a wide scope, as it is not intended to a particular organization. This project is
going to develop generic software, which can be applied by any businesses organization.
Moreover it provides facility to its users. Also the software is going to provide a huge amount
of summary data.
</p>

## System Analysis
### Modules:
- **Patient Login:-** *Patient Login to the system using his ID and Password.*
- **Patient Registration:_** *If Patient is a new user he will enter his personal details and he
will user Id and password through which he can login to the system.*
- **My Details:-** *Patient can view his personal details.*
- **Disease Prediction:-** *- Patient will specify the input parameter values. System will take
input values and predict the disease based on the input data values specified by the
patient and system will also suggest doctors based on the locality*
- **Search Doctor:-** *Patient can search for doctor by specifying name, address or type.*
- **Feedback:-** *Patient will give feedback this will be reported to the admin*
- **Doctor Login:-** *Doctor will access the system using his User ID and Password.*
- **Patient Details:-** *Doctor can view patient’s personal details.*
- **Notification:-** *Admin and doctor will get notification how many people had accessed
the system and what all are the diseases predicted by the system.*
- **Admin Login:-** *Admin can login to the system using his ID and Password.*
- **Add Doctor:-** *Admin can add new doctor details into the database.*
- **Add Dataset:-** *Admin can add dataset file in database.*
- **View Doctor:-** *Admin can view various Doctors along with their personal details.*
- **View Disease:-** *Admin can view various diseases details stored in database.*
- **View Patient:-** *Admin can view various patient details that had accessed the system.*
- **View Feedback:-** *Admin can view feedback provided by various users.*
  
### Technology Used:
- HTML
- CSS
- JAVASCRIPT
- BOOTSTRAP
- DJANGO
- GRADIENT BOOSTING ALGORITHM
- LOGISTIC REGRESSION
- SQLITE3 DATABASE INTERGRITY
- Dataset:https://drive.google.com/file/d/1TeFzjTW_8H78SHFbWrhbf-AGpdUZKJO3/view?usp=sharing

## Run Locally

Clone the project

```bash
  git clone https://github.com/Kumar-laxmi/Heart-Disease-Prediction-System
```

Go to the project directory

```bash
  cd Heart-Disease-Prediction-System
```

Start the server

```bash
  python manage.py runserver
```

## Model Training(Machine Learning)

```javascript
def prdict_heart_disease(list_data):
    csv_file = Admin_Helath_CSV.objects.get(id=1)
    df = pd.read_csv(csv_file.csv_file)

    X = df[['age','sex','cp',  'trestbps',  'chol',  'fbs',  'restecg',  'thalach',  'exang',  'oldpeak',  'slope',  'ca',  'thal']]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=0)
    nn_model = GradientBoostingClassifier(n_estimators=100,learning_rate=1.0,max_depth=1, random_state=0)
    nn_model.fit(X_train, y_train)
    pred = nn_model.predict([list_data])
    print("Neural Network Accuracy: {:.2f}%".format(nn_model.score(X_test, y_test) * 100))
    print("Prdicted Value is : ", format(pred))
    dataframe = str(df.head())
    return (nn_model.score(X_test, y_test) * 100),(pred)
```

## NOTE: GitHub Pages is not working
