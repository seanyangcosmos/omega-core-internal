// jason/core_judge.js

function analyzeSentence() {
    const sentence = document.getElementById('sentenceInput').value.trim();
    const resultDiv = document.getElementById('result');

    if (!sentence) {
        resultDiv.innerHTML = "⚠️ 請輸入語句。";
        return;
    }

    // Demo 回傳結果
    if (sentence.includes("不確定") || sentence.includes("不存在")) {
        resultDiv.innerHTML = "【判準結果】：❓ 無法確定或矛盾語句";
    } else {
        resultDiv.innerHTML = "【判準結果】：✅ 語句可接受，無明顯矛盾";
    }
}

function clearInput() {
    const input = document.getElementById('sentenceInput');
    const result = document.getElementById('result');

    if (input) input.value = '';
    if (result) result.innerHTML = '';
}


