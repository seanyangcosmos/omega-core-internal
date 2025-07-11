function simulateGPT() {
    const sentence = document.getElementById('sentenceInput').value.trim();
    const model = document.getElementById('modelSelect').value;
    const resultDiv = document.getElementById('result');

    if (!sentence) {
        resultDiv.innerHTML = "⚠️ 請輸入語句，我才能進行分析。";
        return;
    }

    let reply = "";

    // GPT 模型切換
    if (model === "gpt-4.0") {
        reply = simulateGPT4(sentence);
    } else if (model === "gpt-4.0-mini") {
        reply = simulateGPT4Mini(sentence);
    } else {
        reply = "❌ 未知模型選項。";
    }

    resultDiv.innerHTML = reply;
}

function simulateGPT4(text) {
    // GPT-4 模擬風格：較嚴謹、邏輯清晰、哲學語氣
    if (text.includes("悖論") || text.includes("矛盾")) {
        return "🔍 根據 GPT-4.0 模型模擬，該語句可能隱含語義矛盾，建議以 Sean Yang Core 的結構語法進行剖析。";
    } else if (text.length < 5) {
        return "📏 此語句過短，不足以構成完整語義結構。請補足背景或語境。";
    } else {
        return "✅ 此語句在 GPT-4.0 模型下判為邏輯連貫、結構穩定，具備良好語義可解性。";
    }
}

function simulateGPT4Mini(text) {
    // GPT-4 Mini 模擬風格：快速、偏結論、偏執行面
    if (text.includes("悖論") || text.includes("矛盾")) {
        return "⚠️ 這句話有點問題，可能有語意衝突，建議重寫或拆開處理。";
    } else if (text.length < 5) {
        return "📌 太短了，我無法分析，請再補充內容。";
    } else {
        return "👍 這句話應該沒問題，符合目前已知的結構邏輯。";
    }
}

function clearInput() {
    document.getElementById('sentenceInput').value = '';
    document.getElementById('result').innerHTML = '';


document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('button[onclick="simulateGPT()"]').onclick = simulateGPT;
  document.querySelector('button[onclick="clearInput()"]').onclick = clearInput;
});

}
