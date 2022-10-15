from dataclasses import dataclass

from analysis import analysis

from fastapi import FastAPI

app = FastAPI()


@dataclass
class User:  # TODO remove temporary class to represent MongoDB doc
    username: str
    password: str
    email: str
    song: str
    liked: list
    disliked: list


@app.post("/register")
async def register(user: { "username": str, "password": str, "email": str }) -> { "message": str }:
    # TODO create doc in MongoDB
    # TODO send confirmation email
    return {"message": "Confirmation email sent!"}


@app.post("/refresh")
async def refresh() -> { "message": str }:
    users: list[User] = []  # TODO from MongoDB

    for user in users:
        user["song"] = analysis(user["username"], user["password"])  # TODO update doc in MongoDB
        # TODO send email/text notification

    return {"message": "Songs of the Day generated!"}
