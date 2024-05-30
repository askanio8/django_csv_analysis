document.addEventListener("DOMContentLoaded", function () {
  let currentIndex = 0;
  const graphs = graphsList; // graphsList должен быть определен в вашем шаблоне
  const imgElement = document.getElementById("graphImage");
  const imageCounter = document.getElementById("imageCounter");

  function updateImage() {
    imgElement.src = graphs[currentIndex];
    updateCounter();
  }

  function updateCounter() {
    const currentDisplayIndex = currentIndex + 1;
    const displayIndex =
      currentDisplayIndex < 10
        ? `&nbsp;${currentDisplayIndex}`
        : `${currentDisplayIndex}`;
    imageCounter.innerHTML = `${displayIndex}(${graphs.length})`;
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

  // Инициализация первого изображения и счетчика
  updateImage();
});
