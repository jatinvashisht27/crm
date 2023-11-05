// Login page password toggle button

let pswrd = document.getElementById('floatingPassword')
let toggleBtn = document.getElementById('toggleBtn');

toggleBtn.onclick = function () {
    if (pswrd.type === 'password') {
        pswrd.setAttribute('type', 'text');
        toggleBtn.classList.add('hide');
    } else {
        pswrd.setAttribute('type', 'password');
        toggleBtn.classList.remove('hide');
    }
}