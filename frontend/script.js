function play() {
  const name = document.getElementById("name").value;

  fetch("http://localhost:8000/jugar", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ real_name: name })
  })
  .then(res => res.json())
  .then(data => {
    if (data.detail) {
      document.getElementById("result").innerText = data.detail;
    } else {
      document.getElementById("result").innerText =
        "Tu pareja es: " + data.pareja + 
        "\nMuchas gracias por participar, te recuerdo que el detalle es de: $5000 hasta $10000" +
        "\npuede ser dulce o cualquier detallito" +
        "\nY sobre todas estas cosas, vístanse de amor, que es el vínculo perfecto" + "\nColosenses 3:14";
    }
  })
  .catch(() => {
    document.getElementById("result").innerText =
      "No se pudo conectar con el servidor";
  });
}
