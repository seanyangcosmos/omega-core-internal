document.getElementById('analyzeBtn').addEventListener('click', function() {
  const sentence = document.getElementById('inputSentence').value.trim();
  let resultText = '';

  // 語義判斷範例：初階封閉語句檢查
  const isClosed = /。|！|？|；/.test(sentence.slice(-1)); // 檢查結尾是否為中文句號類

  const result = {
    "語義類型": "封閉語句",
    "判斷結果": isClosed ? "是" : "否",
    "補充說明": isClosed
      ? "語句具明確結尾標點，初步視為封閉語句。"
      : "語句未含結尾標點，可能為開放語句或不完整語句。",
    "系統語義備註": "此為初階句尾封閉檢查，尚未進入結構語法層分析。"
  };

  resultText += `<pre>${JSON.stringify(result, null, 2)}</pre>`;
  document.getElementById('result').innerHTML = resultText;
});

document.getElementById('clearBtn').addEventListener('click', function() {
  document.getElementById('inputSentence').value = '';
  document.getElementById('result').innerHTML = '';
});

