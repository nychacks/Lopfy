from django.shortcuts import render, get_object_or_404
from .models import Mentor, Logs

# Create your views here.
def index(request):
    users = Mentor.objects.all()
    data = {}
    for user in users:
        field = user.role.field.name
        if field not in data:
            data[field] = []
        data[field].append({
            'id': user.id,
            'name': user.name,
            'role': user.role.name
        })
        
    return render(request, 'index.html', {
        'data': data
    })

def user(request, id):
    user = get_object_or_404(Mentor, pk=id)
    logs = Logs.objects.filter(mentor=id)
    formattedData = []
    for log in logs:
        formattedData.append({
            'day': log.day,
            'hour': log.hour,
            'category': log.category,
            'description': log.description
        })
    return render(request, 'user.html', {
        'user': user,
        'formattedData': formattedData
    })