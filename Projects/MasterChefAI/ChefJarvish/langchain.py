from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate,ChatPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from decouple import config


def askMasterChef(recipe_message):
    SECRET_KEY = config('Key') # Replace your API KEY Here
    chat = ChatOpenAI(openai_api_key = SECRET_KEY)
    systemMessagePrompt = SystemMessagePromptTemplate.from_template(
        "You are a Master Chef. Your Name is ChefJarvish. First Introduce yourself as ChefJarvish - Your Personal MsterChef.You can write recipe and follow-on questions of any kind of dish which can be ready in 5-15 minutes. you are allowed to answer food related queries only. if you don not know the answer, write I do not he answer. Please ask another Question."      
    )
    humanMessagePrompt = HumanMessagePromptTemplate.from_template("{asked_recipe}")

    chatPrompt = ChatPromptTemplate.from_messages([
        systemMessagePrompt,
        humanMessagePrompt,
    ]).format(
        asked_recipe = recipe_message
    )
    # print("Chat Prompt :",chatPrompt)
    response = chat.invoke(chatPrompt)
    return response.content