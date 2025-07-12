const inputEl = document.getElementById("inputText");
const clearBtn = document.getElementById("clearButton");
const outputA = document.getElementById("outputA");
const outputB = document.getElementById("outputB");
const outputC = document.getElementById("outputC");

inputEl.addEventListener("input", () => {
  const text = inputEl.value.trim();
  if (!text) {
    outputA.innerText = "（等待輸入）";
    outputB.innerText = "（等待輸入）";
    outputC.innerText = "（等待輸入）";
    return;
  }

  // 類型 A 分析模擬
  outputA.innerText = `【語義類型】：A\n【判斷結果】：合法\n【補充說明】：句式清晰\n【系統語義備註】：正常結構`;

  // 類型 B 分析模擬
  outputB.innerText = `【語義類型】：B\n【判斷結果】：容悖語句\n【補充說明】：邏輯存在潛在衝突\n【系統語義備註】：需要人工審查`;

  // 類型 C 分析模擬
  outputC.innerText = `【語義類型】：C\n【判斷結果】：開放結構\n【補充說明】：語意待定，開放詮釋\n【系統語義備註】：具創造潛能`;
});

clearBtn.addEventListener("click", () => {
  inputEl.value = "";
  outputA.innerText = "（等待輸入）";
  outputB.innerText = "（等待輸入）";
  outputC.innerText = "（等待輸入）";
});


