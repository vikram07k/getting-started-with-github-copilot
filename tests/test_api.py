def test_get_activities(client):
    # Arrange
    # (client fixture provides a TestClient)

    # Act
    r = client.get("/activities")

    # Assert
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_signup_and_duplicate(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act: signup first time
    r = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert successful signup
    assert r.status_code == 200
    assert "Signed up" in r.json().get("message", "")

    # Act: attempt duplicate signup
    r2 = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert duplicate is rejected
    assert r2.status_code == 400


def test_unregister_flow(client):
    # Arrange
    activity = "Programming Class"
    email = "temp@mergington.edu"

    # Act: signup
    r = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert signup succeeded
    assert r.status_code == 200

    # Act: unregister
    r2 = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert removal succeeded
    assert r2.status_code == 200
    assert "Unregistered" in r2.json().get("message", "")

    # Act: unregister again
    r3 = client.delete(f"/activities/{activity}/participants?email={email}")

    # Assert participant is no longer found
    assert r3.status_code == 404
