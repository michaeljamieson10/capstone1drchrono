
$('.patient').click(async function() {
    console.log(access_token)
    patient_id = $(this).attr('id')
    const med = await getPatientId(patient_id)
    console.log(med)
});
// $(async function() {
//     const $mainMedication = $(".main");
//     const result = await generateMedicationHTML();
//     $mainMedication.append(result)
//     // const storyListInstance = await 


//     function generateMedicationHTML(story) {
    
//         // render medication markup
//         // {% for datas in data %}try to add these flask loops 
//         const medicationMarkup = $(`
//         {% for datas in data %}
//             <div class="card">
//                 <h5 class="card-header">Featured</h5>
//                 <div class="card-body">
//                     <h5 class="card-title">Special title treatment</h5>
//                     <p class="card-text">{{datas['name']}}</p>
//                     <a href="#" class="btn btn-primary">Give</a>
//                 </div>
//             </div>
//         {% endfor %}
//         `);
//         return medicationMarkup;
//     };    
// });