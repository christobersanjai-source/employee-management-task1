from pydantic import BaseModel, ConfigDict, EmailStr, Field
class EmployeeFields(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: EmailStr
    department: str = Field(min_length=1, max_length=100)
    job_title: str = Field(min_length=1, max_length=120)
class EmployeeCreate(EmployeeFields):
    pass
class EmployeeUpdate(EmployeeFields):
    pass
class Employee(EmployeeFields):
    id: int
    model_config = ConfigDict(from_attributes=True)
