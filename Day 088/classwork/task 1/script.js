const form = document.getElementById("my-form");

form.addEventListener("submit", function(e){
    e.preventDefault();
    const fullname = form.fullname.value;
    const email = form.email.value;
    const tel = form.tel.value;
    
    const tr = document.createElement("tr");
    const fullanmeTd = document.createElement("td");
    fullanmeTd.textContent = fullname;
    
    const emailTd = document.createElement("td");
    emailTd.innerHTML = email;

    const telTd = document.createElement("td");
    telTd.innerHTML = tel;
    
    tr.appendChild(fullanmeTd);
    tr.appendChild(emailTd);
    tr.appendChild(telTd);
    
    form.nextElementSibling.children[1].appendChild(tr);
})