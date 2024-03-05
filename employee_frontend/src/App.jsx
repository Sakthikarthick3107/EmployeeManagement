import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const[employees , setEmployees] = useState([]);
  const[depts,setDepts] = useState([]);
  const[selectDept , setSelectDept] = useState('');

  const fetchEmployees = async () => {
    try {
      const employees = await fetch('http://127.0.0.1:8000/api/employees/');
      const employeeData =await employees.json();
      //console.log(employeeData);
      setEmployees(employeeData)
    } catch (error) {
      console.error('Error while fetching data',error)
    }
  }

  const fetchDepartments = async() =>{
    try {
      const depts = await fetch('http://127.0.0.1:8000/api/departments/');
      const deptData = await depts.json();
      setDepts(deptData);
    } catch (error) {
      console.error('Error while fetching data',error)
    }
  }

  useEffect(() =>{
    fetchEmployees();
    fetchDepartments();
  },[])


  return (
    <div className="App">
        <table>
          <tr>
            <th>Name</th>
            <th>Salary</th>
            <th>Native</th>
            <th>Department</th>
          </tr>
          {employees.map((employee , index) => (
            <tr key={index}>
              <td>{employee.name}</td>
              <td>{employee.salary}</td>
              <td>{employee.native}</td>
              

              {depts.filter((dept) => dept.id === employee.dept).map((value,id)=>(
                <td> {value.dept}
                  </td>
              ))}
            </tr>
          ))}
        </table>

        <select name="Department" value={selectDept} onChange={(e) =>setSelectDept(e.target.value)}>
          <option value="" >All</option>
          {depts.map((dept,index) => (
            <option key={index} value={dept.id}>{dept.dept}</option>
          ))}
        </select>
    </div>
  );
}

export default App;
