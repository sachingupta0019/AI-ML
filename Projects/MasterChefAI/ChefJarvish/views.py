from django.shortcuts import render, redirect
from django.views import View
from ChefJarvish.forms import RecipeForm
from ChefJarvish.langchain import askMasterChef

# Create your views here.
class home(View):
    def get(self, request):
        AI_Response = request.session.get('AI_Recipe_Response', '')
        form = RecipeForm()
        return render(request, 'index.html/',{'form' : form, 'AI_Response' : AI_Response})
    
    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data.get('recipe_message')
            AI_Response = askMasterChef(recipe_message)
            request.session['AI_Recipe_Response'] = AI_Response
        form = RecipeForm()
        return redirect('/')