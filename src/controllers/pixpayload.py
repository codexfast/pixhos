import urllib3
import json
import colorama

def pixPayload(key_type: str, key:str, name: str, city: str, amount=None, reference=None) -> json:
    URL = "https://www.gerarpix.com.br/emvqr-static"
    http = urllib3.PoolManager()
    
    encoded_data = json.dumps({
        "key_type": key_type,
        "key": key,
        "name": name,
        "city": city,
        "amount": amount if amount != None else amount,
        "reference": reference if reference != None else ""
    })

    try: 
        r = http.request(
            'POST',
            URL,
            body=encoded_data,
            headers={'Content-Type':'application/json'}
        )

        print(colorama.Fore.GREEN)
        print(f'<STATUS {r.status}>')
        print(colorama.Style.RESET_ALL)
        
        return json.loads(r.data.decode('utf-8'))
    except:
        return None;


if __name__=="__main__":
    print(pixPayload("CPF", "463.380.088-40", "Gilberto", "Santa Branca"))