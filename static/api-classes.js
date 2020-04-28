async function submitForm(name, year, email, color){
    const resp = await axios.post("/api/get-lucky-num", {name, year, email,color});
    return resp.data
}