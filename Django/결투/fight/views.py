from django.shortcuts import render
from .models import Game

# Create your views here.
def create(request):
    
    name = request.POST.get("name")
    attack = request.POST.get("attack")
    defense = request.POST.get("defense")
    gs1 = request.POST.get("gs1")
    gs2 = request.POST.get("gs2")
    gs3 = request.POST.get("gs3")
    gs4 = request.POST.get("gs4")
    Game.objects.create(name=name, attack=attack, defense=defense, gs1=gs1, gs2=gs2, gs3=gs3,gs4=gs4)

    type_list = {
        "불꽃": "flame",
        "물": "water",
        "풀": "grass",
        }

    context = {
        "type_list": type_list,
        "attack": attack,
        "defense": defense,
        "name": name,
        "gs1":gs1,
        "gs2":gs2,
        "gs3":gs3,
        "gs4":gs4,
    }
    return render(request, "fight/create.html", context)