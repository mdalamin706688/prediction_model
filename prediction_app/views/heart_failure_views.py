import pickle
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..models.heart_failure_models import HeartDiseaseData
from ..models.heart_failure_models import load_model_from_file

class HeartFailurePredictionView(APIView):
    @method_decorator(csrf_exempt)  # Add the CSRF exemption decorator
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        try:
            data = json.loads(request.body)  # Convert request body to JSON

            # Preprocess the data to match the input format for the model
            # For simplicity, I assume the data is preprocessed correctly here

            # Convert string values to float or int
            data = {key: float(value) if isinstance(value, str) and value.replace('.', '', 1).isdigit() else int(value) for key, value in data.items()}

            # Load the pre-trained model for Heart Disease
            model = load_model_from_file('pkl/heart_failure.pkl')

            # Perform prediction using the loaded model
            input_data = [list(data.values())]  # Pass the values as a list of lists
            prediction = model.predict(input_data)

            response_data = {
                'prediction': int(prediction[0])
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except ValueError as ve:
            return Response({'error': 'Invalid JSON data format.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
