import fastapi as fa
import httpx
import uvicorn

app = fa.FastAPI()

API_BASE_URL = "https://jsonplaceholder.typicode.com"

@app.get("/{resource}")
async def get_resource(resource: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE_URL}/{resource}")
        return response.json()

@app.post("/posts")
async def create_post(title: str, body: str, user_id: int):
    data = {"title": title, "body": body, "userId": user_id}
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{API_BASE_URL}/posts", json=data)
        return response.json()

@app.put("/posts/{post_id}")
async def update_post(post_id: int, title: str, body: str, user_id: int):
    data = {"title": title, "body": body, "userId": user_id}
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{API_BASE_URL}/posts/{post_id}", json=data)
        return response.json()

@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{API_BASE_URL}/posts/{post_id}")
        return {"message": "Post deleted"}

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)