import requests
import json
import betadexterlambda as beta

res = {}
################################################################################
# Built-in's
################################################################################
def fallback(res):
    return res
    
def goodbye(res):
    res['response']['outputSpeech']['text'] = "Goodbye, Pokemon master"
    return res
    
def help(res):
    s = "Dexter is the unofficial guide to compettetive pokemon playing!  "\
    "Try asking about anything from the type of a pokemon, it's moves,"\
    "or even where it is located! For more detailed help, say detailed help"
    
    res['response']['outputSpeech']['text'] = s
    res['shouldEndSession'] = False
    return res
    
def detailed_help(event, res):
    res['response']['outputSpeech']['text'] = "Sorry, I couldn't find detailed help for that topic"
    helpselect = event['request']['intent']['slots']['help']['value']
    if helpselect:
        res['response']['outputSpeech']['text'] = "Detailed help will be available in the full version of Dexter."
    
    return res
    
################################################################################
# Helpers
################################################################################

def getPokemon(event):
        name = event['request']['intent']['slots']['name']['value']
        pokemon = requestData(name)
        return pokemon
            
def requestData(name):
    url = 'http://poke-guru.com:5000/poke/%s' % (name)
    response = requests.get(url)
    pokemon = json.loads(response.text)
    return  pokemon['data']
    
################################################################################
# Lambda Skill Call
################################################################################

def lambda_skill(event, context):
    res = {
      "version": "1.0",
      "response": {
        "outputSpeech": {
          "type": "PlainText",
          "text": "There was an error getting the pokemon data. Please try again.",
        },
        "shouldEndSession": True
      }
    }
    
    #Get all the pokemon data
    try:
        #check the invocation
        invocation = event['request']['intent']['name']

        #The built-in's
        if invocation == 'AMAZON.FallbackIntent':
            return fallback(res)
        elif invocation == 'detailed_help':
            return detailed_help(event, res)
        elif invocation == 'AMAZON.CancelIntent' or invocation == 'AMAZON.StopIntent':
            return goodbye(res)
        elif invocation == 'AMAZON.HelpIntent':
             return help(res)
        #If the invocation is for the type
        elif invocation == 'get_type':
            pokemon = getPokemon(event)
            if pokemon == []:
                return res
            return beta.get_type(pokemon, res)
        elif invocation == "get_abilities":
            pokemon = getPokemon(event)
            if pokemon == []:
                return res
            return beta.get_ability(pokemon, res)
            
        elif invocation == 'get_tm_moves':
            pokemon = getPokemon(event)
            if pokemon == []:
                return res
            return beta.get_moves(pokemon, res)
            
        elif invocation == 'get_evo':
            pokemon = getPokemon(event)
            if pokemon == []:
                return res
            return beta.get_evolutions(pokemon[0], res)
            
        elif invocation == 'get_number':
            poke = getPokemon(event)
            return beta.get_number(poke[-1], res)
            
        #Probably an error, return the default error    
        else:
            return res
            
    except Exception as e:
        print("Exception: %s", e)
        return res
    