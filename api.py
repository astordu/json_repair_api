from json_repair import repair_json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/repair")
async def repair_endpoint(request: Request):
    raw_body = await request.body()
    raw_json = raw_body.decode("utf-8")
    return repair_json(raw_json, ensure_ascii=False)
        


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)