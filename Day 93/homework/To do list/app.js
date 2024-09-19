const btn = document.querySelector('#btn');
const form = document.querySelector('#form');
const box = document.querySelector('.box');
let counter = 0;
 
btn.addEventListener('click', (e) =>{
    e.preventDefault();
    counter ++
    const task = form.task.value;
     
    
    const el = document.createElement('p');
    el.innerHTML =  `${counter}.  ${task}`;
    el.style.color = 'white';
    el.style.height = 'fit-content'
    el.style.fontSize = '30px'
    box.appendChild(el);
    if(e.target.id === 'P'){
        e.target.remove()
    }
  
})


 
 