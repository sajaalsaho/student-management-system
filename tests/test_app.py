import pytest
from app import create_app, services


@pytest.fixture
def app(tmp_path):
    return create_app(
        {"DATABASE": str(tmp_path / "test.db"), "TESTING": True, "SECRET_KEY": "test"}
    )


@pytest.fixture
def client(app):
    return app.test_client()


def test_add_and_list_students(app):
    with app.app_context():
        services.add_student("Ali Veli", "1001")
        students = services.list_students()
        assert len(students) == 1
        assert students[0]["name"] == "Ali Veli"


def test_duplicate_student_number_rejected(app):
    with app.app_context():
        services.add_student("Ali Veli", "1001")
        with pytest.raises(ValueError):
            services.add_student("Ayşe Kaya", "1001")


def test_delete_student(app):
    with app.app_context():
        services.add_student("Ali Veli", "1001")
        student_id = services.list_students()[0]["id"]
        services.delete_student(student_id)
        assert services.list_students() == []


def test_average_calculation(app):
    with app.app_context():
        services.add_student("Ali Veli", "1001")
        services.add_course("MYM101", "Yazılım Mühendisliği")
        services.add_course("MYM102", "Veritabanı")
        sid = services.list_students()[0]["id"]
        c1, c2 = [c["id"] for c in services.list_courses()]
        services.set_grade(sid, c1, 80)
        services.set_grade(sid, c2, 90)
        assert services.calculate_average(sid) == 85.0


def test_invalid_grade_rejected(app):
    with app.app_context():
        services.add_student("Ali Veli", "1001")
        services.add_course("MYM101", "Yazılım Mühendisliği")
        sid = services.list_students()[0]["id"]
        cid = services.list_courses()[0]["id"]
        with pytest.raises(ValueError):
            services.set_grade(sid, cid, 150)


def test_pages_load(client):
    for url in ["/students", "/courses", "/grades", "/report"]:
        assert client.get(url).status_code == 200
def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}        