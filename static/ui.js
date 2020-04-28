
async function processForm(evt) {
    evt.preventDefault()

    //** clear all of our text fields upon submit */ 
    $('#name-err').text("")
    $('#year-err').text("")
    $('#email-err').text("")
    $('#color-err').text("") 
    $('#lucky-results').text("")

    //** takes data from form */ 
    const name = $('#name').val()
    let year = $('#year').val()
    const email = $('#email').val()
    const color = $('#color').val()

    //** verfies if year */ 
    if (!$.isNumeric(year)){
        year = 0
    }
    //** console.log(name, year, email, color) */ 
    resp = await submitForm(name, year, email, color)
    handleResponse(resp)
}

/** handleResponse: deal with response from our lucky-num API. */
function handleResponse(resp) {
   
    if(resp.hasOwnProperty("errors")){
        keyArr = Object.keys(resp.errors)
        for (i = 0; i <= keyArr.length; i++){
            $('#' + `${keyArr[i]}`+'-err').text(resp.errors[keyArr[i]])
        }
    }else{
        $('#lucky-results').text(resp.num.fact + " "  + resp.year.fact);
    }
}
$("#lucky-form").on("submit", processForm);
