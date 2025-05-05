async function analizza() {
    const fileInput = document.getElementById("imgInput");
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);
  
    const res = await fetch("http://localhost:8000/analizza/", {
      method: "POST",
      body: formData
    });
  
    const json = await res.json();
    document.getElementById("output").textContent = JSON.stringify(json, null, 2);
  }
  