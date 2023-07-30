import pickle
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import load_model_from_file

# Endpoint for making predictions
@csrf_exempt
@require_POST
def predict(request):
    try:
        data = request.POST.get('data')
        data = json.loads(data)  # Assuming the data is in JSON format

        # Assuming your input data is in the format of a list of dictionaries
        # where each dictionary represents a row in the CSV
        predictions = []
        model = load_model_from_file('models/model.pkl')  # Load the model from the prediction_app folder
        for row in data:
            # Preprocess the input data (You may need to adjust this based on your actual data)
            input_data = [
                int(row['AGE']), int(row['PackHistory']),
                int(row['MWT1']), int(row['MWT2']), float(row['FEV1']), float(row['FVC']),
                int(row['CAT']), int(row['HAD']), float(row['SGRQ']),
                int(row['copd']), int(row['gender']), int(row['smoking'])
            ]
            # Make prediction using the loaded model
            prediction = model.predict([input_data])
            predictions.append(int(prediction[0]))

        return JsonResponse({'predictions': predictions})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
