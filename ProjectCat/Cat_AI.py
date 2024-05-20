# This is the driving force of the game. It will be using Ollama to generate the paths
# and Chroma to store the vector data of the game so that the AI "remembers" what the
# player has already done.

# These are the main dependencies.
from langchain_community.llms import Ollama # This allows the Python code to use Ollama
from langchain_community.vectorstores import Chroma # This is for the Chroma DB
from langchain_community import embeddings # This is for creating the embeddings for the Chroma DB
from langchain_core.prompts import ChatPromptTemplate # This is a template that will be used for prompting the AI
from langchain_core.runnables import RunnablePassthrough # To feed the AI the input
from langchain_core.output_parsers import StrOutputParser # To receive the output as a string

from Cat_Main import adventurer
from monsters import elementalDragon

def LLM_generation(adventurerHistory, adventurerQuery):
    try:
        localModel = Ollama(model = "mistral") # Sets the model as Mistral-7b-Instruct-v0.2

        adventureText = f"""
        You are now the guide of an epic journey in the region of Wolfspine.
        An adventurer named {adventurer.name}, who is a {adventurer.characterClass},
        is traveling in search of the legendary beast {elementalDragon.name}.
        You must navigate the {adventurer.name} through challenges, choices, battles,
        and consequences, dynamically adapting the tale based on the adventurer's
        decisions. Your goal is to create a branching narrative experience where each
        choice leads to a new path, ultimately determining {adventurer.name}'s fate.\n
        """
        
        adventureTemplate = adventureText + """
        Here are some rules to follow:
        1. Have a few paths that lead to success
        2. Have a few paths that lead to death. If the adventurer dies generate a response that explains the death and ends in the text: "The End.", I will search for this text to end the game
        3. There are only a few monsters that can be encountered, they are the following: goblin, fire drake, ogre, giant spider, and shadow mage, during an encounter, generate a response that says "You have encountered a..." and include the name of one of the aforementioned monsters, I will search for this text to start a battle
        4. If the adventurer's health reaches 0, generate a response that explains the death and ends in the text: "The End.", I will search for this text to end the game
        
        Here is the journey so far, use this to understand what to say next: {history}
        Human: {query}
        AI: 
        """

        prompt = ChatPromptTemplate.from_template(adventureTemplate)
        chain = (
            {"history": adventurerHistory, "query": RunnablePassthrough()}
            | prompt
            | localModel
            | StrOutputParser()
        )

        return(chain.invoke(adventurerQuery))
    
    except Exception as e:
        # If there is an error, an error message will be displayed
        # This is for debugging purposes, and will be removed later
        print(f"There was an error in LLM_generation:\n{e}")