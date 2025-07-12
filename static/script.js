// static/script.js
document.getElementById("predictForm").addEventListener("submit", async function (e) {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);

  try {
    const response = await fetch("/predict", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    document.getElementById("result").innerHTML = `
      🌽 <strong>Predicted Yield:</strong> ${result.predicted_yield_hg_per_ha} hg/ha
    `;
  } catch (error) {
    document.getElementById("result").innerHTML = `
      ❌ Error: Unable to fetch prediction. Check if FastAPI is running.
    `;
  }
});
