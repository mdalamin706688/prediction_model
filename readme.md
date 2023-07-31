#copd

alamin@localhost ~ $ curl -X POST -H "Content-Type: application/json" -d '{
    "AGE": 60,
    "PackHistory": 0,
    "MWT1": 200,
    "MWT2": 400,
    "FEV1": 2.5,
    "FVC": 3.0,
    "CAT": 2,
    "HAD": 0,
    "SGRQ": 30.0,
    "copd": 1,
    "gender": 1,
    "smoking": 1
}' http://localhost:8000/api/v1/disease/prediction/copd_prediction/
{"prediction":3}alamin@localhost ~ $ 



#heart_failure

curl -X POST -H "Content-Type: application/json" -d '{
    "age": 60,
    "sex": 1,
    "cp": 1,
    "trestbps": 120,
    "chol": 240,
    "fbs": 0,
    "restecg": 1,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 2.0,
    "slope": 1,
    "ca": 0,
    "thal": 3
}' http://localhost:8000/api/v1/disease/prediction/heart_failure_prediction/
