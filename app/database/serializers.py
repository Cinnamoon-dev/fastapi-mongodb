from typing import Any

def document_serial(document: dict[str, Any]) -> dict[str, Any]:
    keys = document.keys()
    id_keys = [key for key in keys if "id" in key]

    for id_key in id_keys:
        document[id_key] = str(document[id_key])
        del document[id_key]

    return document

def list_documents(documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [document_serial(document) for document in documents]
