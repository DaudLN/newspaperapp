let div_id_username = document.getElementById("div_id_username");
let div_id_password = document.getElementById("div_id_password");

let username = document.getElementById("id_username");
let password = document.getElementById("id_password");

const invalid_div = document.createElement("div");

invalid_div.setAttribute("class", "invalid-feedback");
invalid_div.innerHTML = "This field can not be empty";

console.log(invalid_div);
console.log(div_id_password);

username.addEventListener("blur", validateUsername);
password.addEventListener("blur", validatePassword);

function validateUsername() {
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
  div_id_password.appendChild(invalid_div);
  password.classList.add("invalid-feedback");

  const pass = /^[a-zA-Z]{1,30}$/;
  if (!pass.test(password.value)) {
    password.classList.remove("invalid-feedback");
    password.classList.add("is-invalid");
  } else {
    password.classList.remove("is-invalid", "invalid-feedback");
  }
}
