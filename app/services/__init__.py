def document_update(document: dict, request_json: dict) -> None:
    document_keys = document.keys()

    for key in document_keys:
        if key in request_json and request_json[key] is not None:
            try:
                document[key] = request_json[key]
            except Exception:
                setattr(document, key, request_json[key])

    if request_json.get("email"):
        try:
            document["email"] = request_json.get("email").lower()  # type: ignore
        except Exception:
            setattr(document, "email", request_json.get("email").lower())  # type: ignore
