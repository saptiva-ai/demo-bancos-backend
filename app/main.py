from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from io import BytesIO

from ocr.ocr import ocr_pdf

app = FastAPI(docs_url='/')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ocr/")
async def ocr_endpoint(files: List[UploadFile] = File(...), doc_types: List[str] = Form(...)):
    try:
        response_data = []
        for file, doc_type in zip(files, doc_types):
            text = ocr_pdf(file, doc_type)
            response_data.append({
                "doc_type": doc_type,
                "filename": file.filename,
                "content": text
            })
        return JSONResponse(content={"responses": response_data})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
