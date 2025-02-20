console.log("Hello from script.js");

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("uploadForm").addEventListener("submit", async function (event) {
        event.preventDefault();
        const formData = new FormData();
        formData.append("fruit", document.getElementById("fruit").files[0]);

        const response = await fetch("/predict", {
            method: "POST",
            body: formData,
        });

        const result = await response.json();
        document.querySelector(".predicted_name").textContent =
            result.predicted_fruit;
        document.querySelector(".confidence").textContent =
            result.confidence_level;
    });

    document.getElementById("fruit").addEventListener("change", function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function () {
                document.querySelector(".fruit_image").src = reader.result;
                document.querySelector(".fruit_image").style.display = "flex";
            };
            reader.readAsDataURL(file);
        }
    });
});