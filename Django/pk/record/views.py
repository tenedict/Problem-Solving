from django.shortcuts import render, redirect
from .models import Pokemon


# Create your views here.
def book(request):
    pokemons = Pokemon.objects.all()
    context = {
        "pokemons": pokemons,
    }
    return render(request, "record/book.html", context)


# def create(request):
#     if request.method == 'POST':
#         pokemon_form = PokemonForm(request.POST)
#         if pokemon_form.is_valid():
#             pokemon_form.save()
#             return redirect('record:book')
#     else:
#         pokemon_form = PokemonForm()
#     context = {
#         'pokemon_form' : pokemon_form,
#     }
#     return render(request, 'record/create.html', context)


def create(request):
    number = 0
    name = ""
    types = []
    if request.method == "POST":
        number = request.POST.get("number")
        name = request.POST.get("name")
        types = request.POST.getlist("types")
        if len(number) > 0 and len(name) > 0 and types != []:
            Pokemon.objects.create(number=number, name=name, types=types)
            return redirect("record:book")

    type_list = {
        "노말": "normal",
        "격투": "fight",
        "바위": "rock",
        "불꽃": "flame",
        "독": "poison",
        "고스트": "ghost",
        "물": "water",
        "땅": "earth",
        "드래곤": "dragon",
        "풀": "grass",
        "비행": "flight",
        "악": "evil",
        "전기": "electricity",
        "에스퍼": "esper",
        "강철": "steel",
        "얼음": "ice",
        "벌레": "bug",
        "페어리": "fairy",
    }

    context = {
        "type_list": type_list,
        "number": number,
        "types": types,
        "name": name,
    }
    return render(request, "record/create.html", context)


def detail(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    x = (pokemon.types).strip("[""]""\'"",")
    x = x.replace(",", "")
    x = x.replace("\'", "")
    types1 =  list(x.split())
    context = {
        "pokemon": pokemon,
        "types1" : types1,
    }
    return render(request, "record/detail.html", context)


def update(request, pk):
    pokemon = Pokemon.objects.get(pk=pk)
    number = pokemon.number
    name = pokemon.name
    types = []
    if request.method == "POST":
        number = request.POST.get("number")
        name = request.POST.get("name")
        types = request.POST.getlist("types")
        if len(number) > 0 and len(name) > 0 and types != []:
            pokemon.number = number
            pokemon.name= name
            pokemon.types= types
            pokemon.save()
            return redirect("record:book")
    type_list = {
        "노말": "normal",
        "격투": "fight",
        "바위": "rock",
        "불꽃": "flame",
        "독": "poison",
        "고스트": "ghost",
        "물": "water",
        "땅": "earth",
        "드래곤": "dragon",
        "풀": "grass",
        "비행": "flight",
        "악": "evil",
        "전기": "electricity",
        "에스퍼": "esper",
        "강철": "steel",
        "얼음": "ice",
        "벌레": "bug",
        "페어리": "fairy",
    }

    context = {
        "type_list": type_list,
        "number": number,
        "types": types,
        "name": name,
        "pokemon":pokemon,
        
    }
    return render(request, "record/update.html", context)
