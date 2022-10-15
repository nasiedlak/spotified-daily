from analysis import analysis

from fastapi import FastAPI

app = FastAPI()


@app.post("/refresh")
async def refresh():
    users = []  # TODO from MongoDB

    for user in users:
        user.song = analysis  # TODO update doc in MongoDB

    # TODO send email/text notification

    return {"message": "Songs of the Day generated!"}
