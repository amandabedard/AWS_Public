def get_type(pokelist, res):
    res['response']['outputSpeech']['text'] = ''
    for poke in pokelist:
        if len(poke['type']) > 1:
            rtext = ' and '.join(poke['type'])
        else:
            rtext = ''.join(poke['type'])
        if poke['alolan'] == 'yes': 
            res['response']['outputSpeech']['text'] += ('The type of Alolan %s is %s. ' % (poke['name'], rtext))
        else:
            res['response']['outputSpeech']['text'] += ('The type of %s is %s. ' % (poke['name'], rtext))
            
    return res

def get_moves(pokelist, res):
    res['response']['outputSpeech']['text'] = ''
    for poke in pokelist:
        if len(poke['moves']) > 1:
            rtext = ', '.join(poke['moves'])
        else:
            rtext = ''.join(poke['moves'])
        if poke['alolan'] == 'yes': 
            res['response']['outputSpeech']['text'] += ('The TM moves of Alolan %s are %s. ' % (poke['name'], rtext))
        else:
            res['response']['outputSpeech']['text'] += ('The TM moves of %s are %s. ' % (poke['name'], rtext))
            
    return res
    
def get_number(poke, res):
    res['response']['outputSpeech']['text'] = ''
    res['response']['outputSpeech']['text'] += ('%s is number %s in the pokedex. ' % (poke['name'], poke['number']))
            
    return res
    
def get_evolutions(poke, res):
    res['response']['outputSpeech']['text'] = ''
    if poke['evolution'] == {} and poke['mega'] == 'no':
        res['response']['outputSpeech']['text'] = '%s does not evolve' % poke['name']
        return res
    elif poke['evolution'] == {} and poke['mega'] == 'yes':
        res['response']['outputSpeech']['text'] = '%s mega evolves with a mega stone' % poke['name']
        return res
    else:
        res['response']['outputSpeech']['text'] = '%s evolves into ' % poke['name']
    for evo, by in poke['evolution'].items():
        res['response']['outputSpeech']['text'] += '%s by %s, ' % (evo, by)
    return res
    
def get_ability(pokelist, res):
    res['response']['outputSpeech']['text'] = ''
    for poke in pokelist:
        if len(poke['ablities']['normal']) > 1:
            rtext = ', '.join(poke['ablities']['normal'])
        else:
            rtext = ''.join(poke['ablities']['normal'])
        if poke['alolan'] == 'yes': 
            res['response']['outputSpeech']['text'] += ('The abilities of Alolan %s are %s. ' % (poke['name'], rtext))
        else:
            res['response']['outputSpeech']['text'] += ('The abilities of %s are %s. ' % (poke['name'], rtext))
            
        if len(poke['ablities']['hidden']) > 0:
            res['response']['outputSpeech']['text'] += ('Hidden ability %s. ' % (', '.join(poke['ablities']['hidden'])))
            
    return res
    