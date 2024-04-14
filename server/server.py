from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import os

app = FastAPI()

SCANS_DIRECTORY = "/home/shilpi/point_lio_unilidar/scans/"

@app.get("/list-files/", response_model=list)
async def list_files():
    files_list = []
    for root, dirs, files in os.walk(SCANS_DIRECTORY):
        for file in files:
            if file.endswith(".pcd"):
                full_path = os.path.join(root, file)
                files_list.append(os.path.relpath(full_path, SCANS_DIRECTORY))
    return files_list

@app.get("/download-file/{file_path:path}")
async def download_file(file_path: str):
    full_file_path = os.path.join(SCANS_DIRECTORY, file_path)
    if not os.path.exists(full_file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(full_file_path, filename=os.path.basename(full_file_path))

@app.delete("/delete-file/{file_path:path}")
async def delete_file(file_path: str):
    full_file_path = os.path.join(SCANS_DIRECTORY, file_path)
    if not os.path.exists(full_file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    # Attempt to delete the file
    try:
        os.remove(full_file_path)
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder({"detail": "File deleted successfully"}))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
