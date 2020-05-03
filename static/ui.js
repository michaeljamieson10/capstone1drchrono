
$('.patient').click(async function() {
    console.log(access_token)
    patient_id = $(this).attr('id')
    const med = await getPatientId(patient_id)
    console.log(med)
});
