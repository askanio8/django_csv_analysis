document.addEventListener("DOMContentLoaded", function () {
  const fileInput = document.getElementById("myFile");
  const uploadLabel = document.getElementById("uploadLabel");

  fileInput.addEventListener("change", function () {
    uploadLabel.textContent = "Please wait...";
    fileInput.form.submit();
  });
});
