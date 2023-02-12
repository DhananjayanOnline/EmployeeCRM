
let employeeDiv = document.querySelector('#employee-subdetail');



function addEmployee(event) {
    let id = event.target.getAttribute('data-id');

    let getPhoto = document.querySelector('#emp_photo' + id);
    let photo = getPhoto.innerHTML;

    let getName = document.querySelector('#emp_name' + id);
    let name = getName.textContent;

    let getDept = document.querySelector('#emp_dept' + id);
    let dept = getDept.textContent;

    let getSd = document.querySelector('#emp_sd' + id);
    let sd = getSd.textContent;

    employeeDiv.innerHTML = "";

    let employeeSubDetails = `
    
    <div class="card shadow mb-4">
        <!-- Card Header - Dropdown -->
        <div class="mt-3">
            ${photo}
        </div>
        <!-- Card Body -->
        <div class="card-body" style="margin-top: -6em">
            <div class=" text-left">
                <p class="mr-2">
                    <i class="fas fa-circle text-primary"></i> <span class="">Name : ${name}</span>
                </p>
                <p class="mr-2">
                    <i class="fas fa-circle text-success"></i> <span class="">Department : ${dept}</span>
                </p>
                <p class="mr-2">
                    <i class="fas fa-circle text-secondary"></i> <span class="">Start Date : ${sd}</span>
                </p>

                
            </div>
            <a href="emp/${id}" class="btn btn-info form-control">view profile</a>
        </div>
    </div>

    `

    employeeDiv.insertAdjacentHTML('beforeend', employeeSubDetails);

    console.log("addEmployee function executed");
}

