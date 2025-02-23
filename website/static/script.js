console.log("Hello from script.js");


fruits_colors = {
    "apple": "#d32f2f",
    "avocado": "#388e3c",
    "banana": "#fbc02d",
    "blueberry": "#303f9f",
    "cherry": "#c2185b",
    "dragonfruit": "#e91e63",
    "grape": "#7b1fa2",
    "guava": "#d32f2f",
    "kiwi": "#689f38",
    "lychee": "#d32f2f",
    "mango": "#f57c00",
    "orange": "#f57c00",
    "papaya": "#f57c00",
    "pear": "#f57c00",
    "pineapple": "#f57c00",
    "pomegranate": "#d32f2f",
    "raspberry": "#d32f2f",
    "strawberry": "#d32f2f",
    "watermelon": "#388e3c",
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("uploadForm").addEventListener("submit", async function (event) {
        event.preventDefault();
        const sumbitBtn = document.getElementById("submitBtn");
        sumbitBtn.disabled = true;
        sumbitBtn.innerText = "Predicting...";
        console.log(sumbitBtn);
        const formData = new FormData();
        formData.append("fruit", document.getElementById("fruit").files[0]);

        const response = await fetch("/predict", {
            method: "POST",
            body: formData,
        });

        const result = await response.json();
        sumbitBtn.disabled = false;
        sumbitBtn.innerText = "Predict";
        const predictedLabel = document.querySelector(".predicted_name");
        const predictedProb = document.querySelector(".confidence");

        predictedLabel.style.color = fruits_colors[result.predicted_fruit];

        predictedLabel.innerText = result.predicted_fruit.charAt(0).toUpperCase() + result.predicted_fruit.slice(1);
        predictedProb.innerText = (result.confidence_level * 100).toFixed(3) + "%";


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