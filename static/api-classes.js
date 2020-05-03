// 'Access-Control-Allow-Origin': '*'
// 'Access-Control-Allow-Credentials': true,
const BASE_URL = "https://app.drchrono.com/api";

async function getPatientId(patient_id) {
  console.log(patient_id,"patient_id")
  const headers = {
    'headers':{
      "Authorization":`Bearer ${access_token}`, 
      "Content-type":"application/json"
    }
  }
  const patient = {"data":{
    "patient": patient_id
  }}
  const response = await axios.get(`https://cors-anywhere.herokuapp.com/${BASE_URL}/medications`,headers,patient)
  console.log(response)
};
