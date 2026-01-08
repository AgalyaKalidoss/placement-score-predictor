async function predict() {
  const cgpaVal = parseFloat(document.getElementById("cgpa").value);
  const techVal = parseInt(document.getElementById("tech").value);
  const domainVal = parseInt(document.getElementById("domain").value);
  const internVal = parseInt(document.getElementById("intern").value);

  // Frontend validation
  if (
    isNaN(cgpaVal) || isNaN(techVal) ||
    isNaN(domainVal) || isNaN(internVal)
  ) {
    document.getElementById("result").innerText =
      "⚠️ Please fill all fields correctly";
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        cgpa: cgpaVal,
        tech_skills: techVal,
        domain_knowledge: domainVal,
        internships: internVal
      })
    });

    const data = await response.json();

    // Handle backend errors
    if (data.error) {
      document.getElementById("result").innerText =
        "❌ " + data.error;
      return;
    }

    document.getElementById("result").innerHTML =
      `✅ Score: <b>${data.placement_score}</b> / 100<br>
       📊 Status: <b>${data.status}</b><br>
       💡 Advice: ${data.advice}`;

  } catch (err) {
    document.getElementById("result").innerText =
      "❌ Server not reachable. Is Flask running?";
  }
}
