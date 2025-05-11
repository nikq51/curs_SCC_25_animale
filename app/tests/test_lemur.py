from lemur import app

def test_homepage():
    tester = app.test_client()
    response = tester.get("/lemur", content_type='html/text')
    assert response.status_code == 200
