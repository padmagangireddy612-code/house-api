from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI()

# Define a homepage endpoint
@app.get("/")
def home():
 return {"message": "Welcome to my first API"}

# Define an endpoint that adds two numbers
@app.get("/add")
def add_numbers(a: int, b: int):
 result = a + b
 return {"result": result}