from django.http import HttpResponse, JsonResponse

def home_page(request):
    friend=[
        'ankit',
        'rahul',
        'sonam',
        'sarika',
        'satyarth',
    ]
    return JsonResponse({'friends':friend})