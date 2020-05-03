const BASE_URL = "https://app.drchrono.com/api";

async function getPatientId(patient) {
  
  const headers = {
    'headers':{
      'Authorization':`Bearer ${access_token}`, 
      'Content-type':"application/json",
      'Access-Control-Allow-Origin': 'http://127.0.0.1:5000',
      'Access-Control-Allow-Credentials': true
      }
  }
  const response = await axios.get(`${BASE_URL}/medications`,{
    patient: patient
  },headers)
  // patient is patient_id
  console.log(response)
};
