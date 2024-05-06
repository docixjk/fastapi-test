from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# 임시 데이터베이스로 사용할 딕셔너리
fake_db: dict[int, dict] = {}


class User(BaseModel):
    username: str
    email: str

# 회원 생성 (Create)
@app.post("/users/")
async def create_user(user: User):
    user_id = len(fake_db) + 1
    fake_db[user_id] = dict(user)
    return {"status": "Success", "user": fake_db[user_id],"user_id":user_id}


# 특정 회원 조회 (Read)
@app.get("/users/{user_id}")
async def read_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_db[user_id]


# 회원 정보 업데이트 (Update)
@app.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    fake_db[user_id] = dict(user)
    return {"status": "Success", "user": fake_db[user_id]}


# 회원 삭제 (Delete)
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")
    del fake_db[user_id]
    return {"status": "Success", "message": f"deleted id : {user_id}"}