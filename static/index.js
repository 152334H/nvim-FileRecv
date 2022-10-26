const file_e = document.getElementById('myfile')
const button_e = document.getElementById("upload-button")
const submit_e = document.getElementById('submit-button')

button_e.addEventListener('click', e => {
	e.preventDefault()
	file_e.click();
})
file_e.addEventListener('change', e => {
	if (file_e.files)
		submit_e.click();
});
