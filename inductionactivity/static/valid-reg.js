	//Validation Code For Inputs

var fname = document.forms['form-reg']['fname'];
var lname = document.forms['form-reg']['lname'];
var dob = document.forms['form-reg']['dob'];	
var email = document.forms['form-reg']['email'];
var password = document.forms['form-reg']['password'];
var pattern = /^\d{1,2}\/\d{1,2}\/\d{4}$/;

var fname_error = document.getElementById('fname_error');
var lname_error = document.getElementById('lname_error');
var dob_error = document.getElementById('dob_error');
var email_error = document.getElementById('email_error');
var pass_error = document.getElementById('pass_error');

fname.addEventListener('textInput', fname_Verify);
lname.addEventListener('textInput', lname_Verify);
dob.addEventListener('textInput', dob_Verify);
email.addEventListener('textInput', email_Verify);
password.addEventListener('textInput', pass_Verify);

function validated(){
	if (fname.value.length < 6) {
		fname.style.border = "3px solid red";
		fname_error.style.display = "block";
		fname.focus();
		console.log("fnameif",fname.value.length)
		return false;
	}
	if (lname.value.length < 6) {
		lname.style.border = "3px solid red";
		lname_error.style.display = "block";
		lname.focus();
		return false;
	}
	if (dob.value.length == 0) {
		dob.style.border = "3px solid red";
		dob_error.style.display = "block";
		dob.focus();
		console.log("dobif",dob.value.length)
		return false;
	}
	if (email.value.length < 6) {
		email.style.border = "3px solid red";
		email_error.style.display = "block";
		email.focus();
		return false;
	}
	if (password.value.length < 6) {
		password.style.border = "3px solid red";
		pass_error.style.display = "block";
		password.focus();
		return false;
	}

}

function fname_Verify(){
	if (fname.value.length > 4) {
		fname.style.border = "1px solid silver";
		fname_error.style.display = "none";
		console.log("fnameverify",fname.value.length)
		return true;
	}
}

function lname_Verify(){
	if (lname.value.length > 4) {
		lname.style.border = "1px solid silver";
		lname_error.style.display = "none";
		return true;
	}
}
function dob_Verify(){
	if (dob.value.length == 0) {
		dob.style.border = "1px solid silver";
		dob_error.style.display = "none";
		console.log("dobverify",dob.value.length)
		return true;
	}
}
function email_Verify(){
	if (email.value.length > 4) {
		email.style.border = "1px solid silver";
		email_error.style.display = "none";
		return true;
	}
}
function pass_Verify(){
	if (password.value.length > 4) {
		password.style.border = "1px solid silver";
		pass_error.style.display = "none";
		return true;
	}
}

