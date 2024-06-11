from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StartScrapingView(APIView):
    def post(self, request):
        # Logic to start scraping tasks
        return Response({"message": "Scraping tasks started successfully"}, status=status.HTTP_200_OK)

class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        # Logic to retrieve scraping status for the given job_id
        return Response({"message": f"Scraping status for job_id {job_id}"}, status=status.HTTP_200_OK)
