const form = document.querySelector("form");
const items = [];
const div = document.getElementById("items")
form.addEventListener("submit", (e)=>{
    e.preventDefault()
    
    const item = form.item.value;
    div.innerHTML += `<li>${item}</li>`

    
})
div.addEventListener('click', (e) =>{
    if(e.target.tagName === 'LI'){
        e.target.remove();

    }
})