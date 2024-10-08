from fastapi import FastAPI, Body
from starlette.responses import JSONResponse


app = FastAPI()

messages = []

# appends a message into the in-memory list
@app.post("/append_msg")
async def append_msg(data=Body()):
    msg = data["msg"]
    messages.append(msg)
    return JSONResponse(f"Message \"{msg}\" successfully appended", status_code=200)


# returns all messages from the in-memory list
@app.get("/show_messages")
async def show_msgs():
    return {"messages": messages}
