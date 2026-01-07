from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Django Demo Task – REST API",
        "available_endpoints": {
            "products": "/api/products/",
            "external_api": "/api/external-posts/",
            "reporting": "/api/report/summary/",
            "admin": "/admin/"
        }
    })
