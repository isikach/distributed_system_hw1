from fastapi import FastAPI


app = FastAPI()

replicated_messages = []

# GET method - returns all replicated messages from the in-memory list
@app.get("/show_messages")
async def show_msgs():
    return {"messages": replicated_messages}
