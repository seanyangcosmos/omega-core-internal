function classifySemantics(text) {
  if (text.includes("唯一") || text.includes("絕對")) {
    return { type: "封閉語義", module: "M9", note: "主張結構已封閉，預設可驗證" };
  }
  if (text.includes("可能") || text.includes("開放") || text.includes("未定")) {
    return { type: "開放語義", module: "M17", note: "語句內含開放結構，預期容納新解" };
  }
  if (text.includes("矛盾") || text.includes("同時") || text.includes("悖論")) {
    return { type: "容悖語義", module: "M17", note: "語句含邏輯衝突，可能具容悖結構" };
  }
  return { type: "普通語義", module: "B3", note: "未明顯偏向開放或封閉，屬語義模擬區" };
}

function analyze() {
  const input = document.getElementById("input-text").value.trim();
  const model = document.getElementById("gpt-model").value;
  const resultDiv = document.getElementById("result");

  if (!input) {
    resultDiv.innerHTML = "<p>⚠️ 請輸入語句。</p>";
    return;
  }

  const classification = classifySemantics(input);

  const mockGPT = simulateGPTReply(input, model, classification.type);

  resultDiv.innerHTML = `
    <div class="result-block">
      <p><strong>【語義類型】</strong> ${classification.type}</p>
      <p><strong>【判斷模組】</strong> ${classification.module}</p>
      <p><strong>【結構註解】</strong> ${classification.note}</p>
      <hr/>
      <p><strong>【模擬回應｜${model}】</strong><br/>${mockGPT}</p>
    </div>
  `;
}

function simulateGPTReply(text, model, type) {
  if (type === "封閉語義") {
    return "此語句呈現封閉結構，若假設成立，推理將導向單一解。";
  }
  if (type === "開放語義") {
    return "此語句顯示開放性，推論可延展，無需立即收斂。";
  }
  if (type === "容悖語義") {
    return "此語句潛藏邏輯衝突，建議進行語法層拆解與容悖模擬。";
  }
  return `${model} 模擬語氣：這是一段需進一步語義判準的描述，建議交由內核處理。`;
}

function clearResult() {
  document.getElementById("result").innerHTML = "";
}
