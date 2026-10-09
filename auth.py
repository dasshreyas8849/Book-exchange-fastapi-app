from fastapi import Header, HTTPException 

#in production 
API_KEY="mysecretapikey"

def verify_api_key(x_api_key:str=Header()):
    if x_api_key!=API_KEY:
        raise HTTPException(status_Code=401,detail="Invalid API KEY")
    return x_api_key
    