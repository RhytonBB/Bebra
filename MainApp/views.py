from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 4, "name": "Картофель фри" ,"quantity":1},
{"id": 5, "name": "Кепка" ,"quantity":124},
]


def about(reqest):
    context={"name": "Rhyton","surname": "Ivan","email": "iosirotkin@yandex.ru"}

    return render(reqest, "about.html",context)
def home(request):

    return render(request, "index.html")
# def item_page(request, id):
#     for item in items:
#         if item["id"] == id:
#             item_str = f"товар {item['name']} количество {item['quanity']}"
#             return HttpResponse(item_str)
#         else:
#             raise Http404(f"Товар с id = {id} не найден")
def item_list(reqest):
    items=Item.objects.all()
    context={"items": items}
    return render(reqest,"items.html",context)

def item1(reqest):
    context={"items": items}
    return render(reqest,"item1.html",context)
def item2(reqest):
    context={"items": items}
    return render(reqest,"item2.html",context)
def item3(reqest):
    context={"items": items}
    return render(reqest,"item3.html",context)
def item4(reqest):
    context={"items": items}
    return render(reqest,"item4.html",context)
def item5(reqest):
    context={"items": items}
    return render(reqest,"item5.html",context)
def test(reqest):
    return render(reqest,"test.html")
# items = [
# {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
# {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
# {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
# {"id": 4, "name": "Картофель фри" ,"quantity":1},
# {"id": 5, "name": "Кепка" ,"quantity":124},
# ]
