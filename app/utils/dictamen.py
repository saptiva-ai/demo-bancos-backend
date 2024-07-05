from typing import Dict, Any, List

def get_dictamen_template(doc_type: str) -> Dict[str, Any]:
    if doc_type == "acta_constitutiva":
        return {
            "rfc": {"question": "¿Cuál es el RFC de la empresa?", "answer": None},
            "estatus": {"question": "¿Cuál es el estatus en el padrón?", "answer": None},
            "actividad": {"question": "¿Cuál es su actividad económica principal?", "answer": None},
            "empresa": {"question": "¿Cuál es el nombre de la empresa?", "answer": None},
            "shareholders": {"question": "¿Quienes son los accionistas de la empresa y qué porcentaje tiene cada uno?", "answer": None},
            "representative": {"question": "¿Quién es el representante legal de la empresa?", "answer": None},
            "fecha": {"question": "¿Cual es la fecha de constitución de la empresa?", "answer": None},
            "duracion": {"question": "¿Cual es la duración de la empresa?", "answer": None},
            "folio": {"question": "¿Cuál es el número de folio mercantil?", "answer": None},
            "notario": {"question": "¿Qué notario oficializó el acta?", "answer": None},
            "notaria": {"question": "¿Dónde se oficializó el acta?", "answer": None},
            "comercial": {"question": "¿Cuál es el domicilio comercial?", "answer": None},
            "legal": {"question": "¿Cuál es el domicilio legal?", "answer": None},
            "credito": {"question": "¿Cuál es su condición crediticia?", "answer": None},
            "socios": {"question": "¿Quienes son los socios?", "answer": None},
            "firmantes": {"question": "¿Quienes son los firmantes?", "answer": None}
        }
    elif doc_type == "csf":
        return {
            "rfc": {"question": "¿Cuál es el RFC?", "answer": None},
            "nombre": {"question": "¿Cuál es el nombre del contribuyente?", "answer": None},
            "domicilio": {"question": "¿Cuál es el domicilio fiscal?", "answer": None},
            "regimen": {"question": "¿Cuál es el régimen fiscal?", "answer": None},
            "estatus": {"question": "¿Cuál es el estatus del contribuyente?", "answer": None}
        }
    elif doc_type == "ine":
        return {
            "nombre": {"question": "¿Cuál es el nombre completo del elector?", "answer": None},
            "clave_elector": {"question": "¿Cuál es la clave de elector?", "answer": None},
            "curp": {"question": "¿Cuál es la CURP?", "answer": None},
            "domicilio": {"question": "¿Cuál es el domicilio?", "answer": None},
            "seccion": {"question": "¿Cuál es la sección electoral?", "answer": None},
            "vigencia": {"question": "¿Cuál es la vigencia?", "answer": None}
        }
    return {}
