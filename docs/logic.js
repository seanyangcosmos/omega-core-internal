const inputTextArea = document.getElementById("inputText");
const resultOutput = document.getElementById("resultOutput");

function analyzeText() {
  const text = inputTextArea.value.trim();

  if (text === "") {
    resultOutput.innerHTML = "（等待輸入）";
    return;
  }

  resultOutput.innerHTML = `
【語義類型 A】：此句話為封閉語義，主張為確定。<br><br>
【語義類型 B】：此句話為容悖語義，包含邏輯例外。<br><br>
【語義類型 C】：此句話為開放語義，暗示探索可能性。
  `;
}

function clearText() {
  inputTextArea.value = "";
  resultOutput.innerHTML = "（等待輸入）";
}
