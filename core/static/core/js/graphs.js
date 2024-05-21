document.addEventListener("DOMContentLoaded", function () {
  let currentIndex = 0;
  const graphs = JSON.parse(document.getElementById("graphs-data").textContent);
  const imgElement = document.getElementById("graphImage");

  function updateImage() {
    imgElement.src = graphs[currentIndex];
  }

  document.getElementById("prevButton").addEventListener("click", function () {
    if (currentIndex > 0) {
      currentIndex--;
      updateImage();
    }
  });

  document.getElementById("nextButton").addEventListener("click", function () {
    if (currentIndex < graphs.length - 1) {
      currentIndex++;
      updateImage();
    }
  });

  // Инициализация первого изображения
  updateImage();
});
