# API Contract
Base URL: http://127.0.0.1:8000
- GET /health -> 200 {"status":"ok"}
- POST /employees/ -> create employee (201)
- GET /employees/ -> list employees (200)
- GET /employees/{employee_id} -> employee (404 if missing)
- PUT /employees/{employee_id} -> update employee (404 if missing)
- DELETE /employees/{employee_id} -> delete employee (204; 404 if missing)
Employee body: name, email, department, job_title. Duplicate email -> 409. Invalid body -> 422.
