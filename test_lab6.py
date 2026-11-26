from emp import emp
def test_emp():
    result = emp("Aru", "emp101", "IT", "40000")
    expected = "Name: Aru, Employee ID: emp101, Department: IT, salary: 40000"
    assert result == expected