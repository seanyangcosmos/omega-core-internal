function processInput() {
  const input = document.getElementById("inputArea").value.trim();

  let type = "結構語法";
  let result = "尚未定義的語法結構";
  let explanation = "";
  let note = "";

  if (input.includes("如果") && input.includes("那麼")) {
    type = "封閉語義";
    result = "條件式語法結構（If...then）";
    explanation = "這類語句表示邏輯上的封閉推導";
    note = "可轉換為邏輯蘊含 A ⇒ B";
  } else if (input.includes("也許") || input.includes("可能")) {
    type = "開放語義";
    result = "不確定或模糊語義結構";
    explanation = "這類語句暗示語義空間尚未封閉";
    note = "屬於 Sean Yang Core 的容悖類語句";
  } else if (input === "") {
    result = "(請輸入語句)";
    note = "輸入為空";
  }

  document.getElementById("typeOutput").innerText = type;
  document.getElementById("resultOutput").innerText = result;
  document.getElementById("explanationOutput").innerText = explanation;
  document.getElementById("noteOutput").innerText = note;
}
