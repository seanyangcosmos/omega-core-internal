function analyzeSentence() {
  const input = document.getElementById('sentenceInput').value.trim();
  const resultBox = document.getElementById('result');

  if (!input) {
    resultBox.innerHTML = "<strong>請輸入語句。</strong>";
    return;
  }

  // 範例：簡易回應模擬，可替換為 GPT 判準或模組解析
  let response = '';
  if (input.includes('矛盾')) {
    response = '【判準結果】：包含邏輯矛盾 ❌';
  } else if (input.includes('封閉')) {
    response = '【判準結果】：封閉語義結構 ✅';
  } else {
    response = '【判準結果】：尚無模組命中 ⚠️';
  }

  resultBox.innerHTML = `
    <p><strong>【輸入語句】：</strong>${input}</p>
    <p>${response}</p>
  `;
}

function clearInput() {
  document.getElementById('sentenceInput').value = '';
  document.getElementById('result').innerHTML = '';
}

