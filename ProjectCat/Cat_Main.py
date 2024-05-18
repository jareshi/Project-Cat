# This will be the main file that will be used to run the game.

from random import randint
from Cat_AI import LLM_generation # Importing the LLM generation function
from datasheet import Character # Importing the character class
import armory

intro_ASCII = r"""
       _                        
      \`*-.                    
       )  _`-.                 
      .  : `. .                
      : _   '  \               
      ; *` _.   `*-._          
      `-.-'          `-.       
        ;       `       `.     
        :.       .        \    
        . \  .   :   .-'   .   
        '  `+.;  ;  '      :   
        :  '  |    ;       ;-. 
        ; '   : :`-:     _.`* ;
    .*' /  .*' ; .*`- +'  `*' 
    `*-*   `*-*  `*-*'
    """
print(intro_ASCII)

# Initializing the character
print("Welcome to the region of Wolfspine. What is your name?")