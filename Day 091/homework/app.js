const inputDay = document.getElementById('day');
const inputMonth = document.getElementById('month');
const inputYear = document.getElementById('year');
const box = document.querySelector('.box')
let numMonth = Math.floor(Math.random() * 12);
const btn = document.getElementById('btn');
const result = document.querySelector('.result');

btn.addEventListener('click', (e)=>{
    e.preventDefault();
    const date = new Date();
    if(inputDay > 31 || inputMonth > 12){
        const alert = document.createElement('span');
        alert.innerHTML = 'Incorrect date';
        alert.style.position = 'absolute'
        alert.style.top = '100px'
        alert.style.color = 'red'
        box.appendChild(alert)
        
    }
   
    
})

