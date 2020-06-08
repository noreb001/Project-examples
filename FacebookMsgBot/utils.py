from wit import Wit

access_token = "ECV5MRDN3HAUEEPVYYNHXNDND5WY77RN"


client = Wit(access_token = access_token)

def wit_response(msgtxt):

    resp = client.message(msgtxt)
    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']

    except:
        pass
    return (entity, value)




