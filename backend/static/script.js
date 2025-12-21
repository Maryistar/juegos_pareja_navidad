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

    result.innerText = `💘 Tu pareja es: ${data.pareja}`;
}

