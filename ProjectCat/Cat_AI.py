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

from monsters import elementalDragon

def LLM_generation(adventurerHistory, adventurerAction):
    """
    This function uses the Ollama model to generate paths for the adventurer to follow based
    on the decisions that they make. It also sets the rules for the AI to follow.

    Parameters:
    adventurerHistory (list): List of the adventurer's previous actions
    adventurerQuery (str): The adventurer's current query

    Returns:
    str: The AI's response to the adventurer's query
    """
    try:
        # Set the model to use, in this case, Mistral-7b-Instruct-v0.2
        localModel = Ollama(model = "mistral")

        # Separate this from the template so that the variables can be dynamically set
        adventureText = f"""
        You are now the guide of an epic journey in the region of Wolfspine.
        An adventurer is traveling in search of the legendary beast {elementalDragon.name}.
        You must navigate the adventurer through challenges, choices, battles,
        and consequences, dynamically adapting the tale based on the adventurer's
        decisions. Your goal is to create a branching narrative experience where each
        choice leads to a new path, ultimately determining adventurer's fate.
        """
        
        # Create the adventure template that will be used by the AI to generate responses
        adventureTemplate = adventureText + """
        Here are some rules to follow:
        1. Have a few paths that lead to success. If the adventurer wins against the elemental dragon, generate a response that explains the victory and ends in the text: "You have won". We will search for this text to end the game.
        2. Have a few paths that lead to death. If the adventurer dies, generate a response that explains the death and ends in the text: "You have died". We will search for this text to end the game.
        3. There are only a few monsters that can be encountered, they are the following: goblin, fire drake, ogre, giant spider, and shadow mage. During an encounter, generate a response that says "You have encountered a..." and include the name of one of the aforementioned monsters. We will search for this text to start a battle.
        4. If the adventurer's health reaches 0, generate a response that explains the death and ends in the text: "You have died". We will search for this text to end the game.
        
        Here is the journey so far, use this to understand what to say next: {history}
        Human: {query}
        AI: 
        """

        # Create a prompt template using the adventure template
        prompt = ChatPromptTemplate.from_template(adventureTemplate)

        # Create a chain of operations that will be applied to the adventurer's query
        chain = (
            {"history": adventurerHistory, "query": RunnablePassthrough()}
            | prompt
            | localModel
            | StrOutputParser()
        )

        # Invoke the chain and return the AI's response
        return(chain.invoke(adventurerAction))
   
    except Exception as e:
        # If there is an error, print the error message
        print(f"There was an error in LLM_generation:\n{e}")