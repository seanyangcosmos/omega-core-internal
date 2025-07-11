// GPT 模式的模擬判準引擎

function analyzeInputGPT() {
  const input = document.getElementById("inputText").value.trim();
  const output = document.getElementById("output");

  if (input === "") {
    output.innerHTML = "<p>請輸入語句進行分析。</p>";
    return;
  }

  // ✅ 模擬 GPT 模式的語義回應
  const result = simulateGPTAnalysis(input);

  output.innerHTML = `
    <div class="result-block">
      <h3>【模擬回應（GPT 模式）】</h3>
      <p><strong>語句：</strong>${input}</p>
      <p><strong>語義類型：</strong>${result.type}</p>
      <p><strong>判斷結果：</strong>${result.judgment}</p>
      <p><strong>補充說明：</strong>${result.note}</p>
    </div>
  `;
}

function clearInput() {
  document.getElementById("inputText").value = "";
  document.getElementById("output").innerHTML = "";
}

// ✅ 模擬 GPT 分析函數，可根據語句特徵調整
function simulateGPTAnalysis(text) {
  // 🔍 簡單示例：根據關鍵詞判斷語義類型
  const lower = text.toLowerCase();

  if (lower.includes("如果") && lower.includes("那麼")) {
    return {
      type: "邏輯條件句",
      judgment: "語法完整，結構清晰。",
      note: "這是一個典型的 if-then 結構，可進一步做邏輯分析。"
    };
  } else if (lower.includes("悖論") || lower.includes("矛盾")) {
    return {
      type: "悖論指涉句",
      judgment: "具有內部矛盾潛在性。",
      note: "建議以封閉語義系統進行交叉驗證。"
    };
  } else {
    return {
      type: "一般陳述句",
      judgment: "無明顯結構錯誤。",
      note: "未觸發已知判準模組，可進一步加入自定義模組擴充。"
    };
  }
}


