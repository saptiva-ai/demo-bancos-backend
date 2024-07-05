from typing import List
from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .utils.dictamen import get_dictamen_template
from .ocr.ocr import ocr_pdf
from .llm.get_responses import responses

app = FastAPI(docs_url='/')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ocr")
def ocr_endpoint(files: List[UploadFile] = File(...), doc_types: List[str] = Form(...)):
    try:
        response_data = []
        for file, doc_type in zip(files, doc_types):
            text = ocr_pdf(file, doc_type)
            dictamen = get_dictamen_template(doc_type)
            for key, value in dictamen.items():
                dictamen[key]['answer'] = responses(prompt=text, question=value["question"])

            response_data.append({
                "doc_type": doc_type,
                "filename": file.filename,
                "content": dictamen
            })
        return JSONResponse(content={"responses": response_data})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"detail": str(e)})
