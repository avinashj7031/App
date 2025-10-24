from app import create_app

def test_hello():
    app = create_app()
    client = app.test_client()
    res = client.get("/api/hello")
    assert res.status_code == 200
    assert res.json["message"] == "Hello from backend!"
