
let employeeDiv = document.querySelector('#employee-subdetail');

// document.getElementById('view-subdetail').addEventListener('click', subDetailEmployee);


function addEmployee(){

    let getPhoto = document.getElementById('emp_photo');
    let photo = getPhoto.textContent;
    let getName = document.getElementById('emp_name');
    let name = getName.textContent;
    let getDept = document.getElementById('emp_dept');
    let dept = getDept.textContent;

    let employeeSubDetails = `
    
    <div class="card shadow mb-4">
        <!-- Card Header - Dropdown -->
        <div>
            <img src="${photo}"  width="10%" alt="">
        </div>
        <!-- Card Body -->
        <div class="card-body">
            <div class="chart-pie pt-4 pb-2">
                <canvas id="myPieChart"></canvas>
            </div>
            <div class="mt-4 text-center small">
                <p class="mr-2">
                    <i class="fas fa-circle text-primary"></i> ${name}
                </p>
                <p class="mr-2">
                    <i class="fas fa-circle text-success"></i> ${dept}
                </p>
                
            </div>
        </div>
    </div>

    `

    employeeDiv.insertAdjacentHTML('beforeend', employeeSubDetails);
}