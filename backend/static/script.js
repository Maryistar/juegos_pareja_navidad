async function play() {
    const name = document.getElementById("name").value;

    const response = await fetch("/jugar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            real_name: name
        })
    });

    const result = document.getElementById("result");

    const data = await response.json();

    if (!response.ok) {
        result.innerText = data.detail;
        return;
    }

    result.innerText = `💘 Tu pareja es: ${data.pareja}` + "\nMuchas gracias por participar, te recuerdo que el detalle es de: $5000 hasta $10000" +
        "\npuede ser dulce o cualquier detallito" +
        "\nY sobre todas estas cosas, vístanse de amor, que es el vínculo perfecto" + "\nColosenses 3:14";
}

