document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("inputSentence");
  const result = document.getElementById("result");

  document.getElementById("analyzeBtn").addEventListener("click", function () {
    const sentence = input.value.trim();
    if (sentence === "") {
      result.textContent = "請輸入語句。";
      return;
    }

    // 測試輸出（未連 GPT）
    result.textContent = "這是一個測試解析結果：語句長度是 " + sentence.length + " 字元。";
  });

  document.getElementById("clearBtn").addEventListener("click", function () {
    input.value = "";
    result.textContent = "";
  });
});
