from fastapi import FastAPI
#app is variable
app = FastAPI()
# create decorator - this tells fastapi whenever anyone visits your url 
@app.get("/") 
def home():
    return {"Message": "welcome to our app"}
# reload - auto restart your sever 
