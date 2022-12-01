let div_id_username = document.getElementById("div_id_username");
let div_id_password = document.getElementById("div_id_password");

let username = document.getElementById("id_username");
let password = document.getElementById("id_password");

const invalid_div = document.createElement("div");

invalid_div.setAttribute("class", "invalid-feedback");

console.log(invalid_div);
console.log(div_id_password);

username.addEventListener("blur", validateUsername);
password.addEventListener("blur", validatePassword);

function validateUsername() {
  invalid_div.innerHTML = "Username can not be empty";
  div_id_username.appendChild(invalid_div);
  username.classList.add("invalid-feedback");

  const name = /^[a-zA-Z]{1,30}$/;
  if (!name.test(username.value)) {
    username.classList.remove("invalid-feedback");
    username.classList.add("is-invalid");
  } else {
    username.classList.remove("is-invalid", "invalid-feedback");
  }
}

function validatePassword() {
  invalid_div.innerHTML = "Password can not be empty";
  div_id_password.appendChild(invalid_div);
  password.classList.add("invalid-feedback");

  const pass = /^[a-zA-Z0-9\.\-@]{1,30}$/;
  if (!pass.test(password.value)) {
    password.classList.remove("invalid-feedback");
    password.classList.add("is-invalid");
  } else {
    password.classList.remove("is-invalid", "invalid-feedback");
  }
}
