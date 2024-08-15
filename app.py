from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
import uvicorn
from services.ats_service import ATS_Service
import traceback
import aiofiles
app = FastAPI()


# Mount the `docs/images` directory as static files
app.mount("/images", StaticFiles(directory="docs/images"), name="static")

@app.get("/health")
async def health_check():
    return {"message": "Service is up and running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Specify the directory to save the file
        save_directory = "docs"
        file_location = f"{save_directory}/{file.filename}"

        # Save the file asynchronously
        async with aiofiles.open(file_location, "wb") as buffer:
            while content := await file.read(1024):  # Read the file in chunks
                await buffer.write(content)  # Use await with buffer.write

        ats_service = ATS_Service(file_location)
        result = ATS_Service.parser(ats_service)
        
        return {"message": "File uploaded and processed successfully", "result": result}
    except Exception as e:
        traceback.print_exc()
        return {"message": "An error occurred while processing the file"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)