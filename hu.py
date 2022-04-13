import requests
import urllib


def imgflip(param:str):
    name='OrganicOx'
    psw='imgflipkick'
    ids={'bang':[275497783,'KidFlySwatbyMrShark']}
    c=ids[param]
    print(c[0])
    URL = 'https://api.imgflip.com/caption_image'
    params = {
        'username':name,
        'password':psw,
        'template_id':c[0],
        'text0':'abcsde',
        'text1':'Nesamani'
    }
    response = requests.request('POST',URL,params=params).json()
    if response['success'] in ('true',True):
        print(response['data']['url'])
    else:
        print(response)
        
imgflip('bang')
