from fastapi import APIRouter, HTTPException, status
from psycopg import IntegrityError
from app.db import repository
from app.models.employee import EmployeeCreate, EmployeeUpdate
router=APIRouter(prefix="/employees",tags=["Employees"])
def duplicate_email():
    raise HTTPException(status_code=409,detail="This email address already exists.")
@router.post("/",status_code=status.HTTP_201_CREATED)
def add_employee(employee:EmployeeCreate):
    try: return repository.create_employee(employee)
    except IntegrityError: duplicate_email()
@router.get("/")
def list_employees(): return repository.get_all_employees()
@router.get("/{employee_id}")
def get_employee(employee_id:int):
    e=repository.get_employee_by_id(employee_id)
    if e is None: raise HTTPException(status_code=404,detail="Employee not found")
    return e
@router.put("/{employee_id}")
def edit_employee(employee_id:int,employee:EmployeeUpdate):
    try: e=repository.update_employee(employee_id,employee)
    except IntegrityError: duplicate_email()
    if e is None: raise HTTPException(status_code=404,detail="Employee not found")
    return e
@router.delete("/{employee_id}",status_code=status.HTTP_204_NO_CONTENT)
def remove_employee(employee_id:int):
    if not repository.delete_employee(employee_id): raise HTTPException(status_code=404,detail="Employee not found")
    return None
