import pytest
from pydantic import ValidationError
from app.models.employee import EmployeeCreate
def test_valid_employee():
    e=EmployeeCreate(name="Sanjai",email="sanjai@example.com",department="IT",job_title="Python Developer")
    assert e.name=="Sanjai"
def test_invalid_email():
    with pytest.raises(ValidationError):
        EmployeeCreate(name="Sanjai",email="bad-email",department="IT",job_title="Python Developer")
