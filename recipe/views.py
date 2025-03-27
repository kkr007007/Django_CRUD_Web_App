from django.shortcuts import render,redirect
from .models import *


def home(request):
    return render(request,'home.html')

def recipes(request):
    if request.method == "POST":
        # Getting data from form
        recipe_name = request.POST.get("recipe_name")
        recipe_description = request.POST.get("recipe_description")
        image = request.FILES.get("recipe_image")

        # Print received data in terminal
        print("Recipe Name:", recipe_name)
        print("Recipe Description:", recipe_description)
        print("Image File:", image)

        recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            image=image
        )
        return redirect('/recipes/')
        
    return render(request, 'recipe.html')



def viewrecipes(request):
    queryset=(recipe.objects.all())
    return render(request,'viewrecipe.html',{'recipes': queryset})

def delete_recipe(request,id):
    queryset=(recipe.objects.get(id=id))
    queryset.delete()
    return redirect('viewrecipes')

def update_recipe(request, id):
    queryset = recipe.objects.get(id=id)

    if request.method == "POST":
        queryset.recipe_name = request.POST["recipe_name"]
        queryset.recipe_description = request.POST["recipe_description"]
        if "recipe_image" in request.FILES:
            queryset.image = request.FILES["recipe_image"]
        queryset.save()
        return redirect('viewrecipes')

    context = {"recipe": queryset}  
    return render(request, 'update_recipe.html', context)