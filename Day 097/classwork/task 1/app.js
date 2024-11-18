const form = document.querySelector('#form');

const accounts = [];

class Account {
    constructor(firstname, lastname, email, city, password) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.email = email;
        this.city = city;
        this.password = password;
    }

    printDetails() {
        console.log(`Firstname: ${this.firstname}`);
        console.log(`Lastname: ${this.lastname}`);
        console.log(`Email: ${this.email}`);
        console.log(`City: ${this.city}`);
        console.log(`Password: ${this.password}`)
    }
}

form.addEventListener('submit', (e) => {
    e.preventDefault();

    const firstname = form.name.value;
    const lastname = form.lastname.value;
    const email = form.email.value;

    const account = new Account(firstname, lastname, email);
    account.printDetails();
    accounts.push(account);
})
