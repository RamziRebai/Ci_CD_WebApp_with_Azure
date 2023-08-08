from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
from pydantic import BaseModel

from transformers import pipeline

app=FastAPI()

generator= pipeline('text-generation', model='gpt2')

class Inputss(BaseModel):
    text: str 

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1> Everything is going well, please add '/docs' at the end to interact with the model
            </h1>
        </body>
    </html>
    """

@app.post("/generate")
def predict(phrase:Inputss):
    result= generator(phrase.text, min_length=10, max_length=100, num_return_sequences=1)
    return result[0]["generated_text"]

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)



