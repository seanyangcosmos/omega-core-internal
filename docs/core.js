function analyzeSentence() {
  const input = document.getElementById('sentenceInput').value.trim();
  let result = '';

  if (input === '') {
    result = '請輸入語句後再分析。';
  } else if (/悖|矛盾|自相矛盾/.test(input)) {
    result = '分類結果：容悖語句 ⚠️';
  } else if (/因為|所以|如果|但是|然而|可是/.test(input)) {
    result = '分類結果：開放語句 ⭕️（含邏輯連接詞）';
  } else if (/[。！？]$/.test(input)) {
    result = '分類結果：封閉語句 ✅';
  } else {
    result = '分類結果：開放語句 ⭕️';
  }

  document.getElementById('resultArea').innerText = result;
  document.getElementById('gptResponse').innerText = '';
}

function simulateGPT() {
  const input = document.getElementById('sentenceInput').value.trim();
  if (input === '') {
    document.getElementById('gptResponse').innerText = '請先輸入語句。';
    return;
  }

  // 模擬 GPT 的解釋
  const simulated = `🔍 GPT 模擬回應：根據目前語義模型，句子「${input}」可能具有潛在語用開放性。建議進一步語境分析。`;
  document.getElementById('gptResponse').innerText = simulated;
}

function clearFields() {
  document.getElementById('sentenceInput').value = '';
  document.getElementById('resultArea').innerText = '';
  document.getElementById('gptResponse').innerText = '';
}

window.onscroll = function() {
  const btn = document.getElementById('scrollTopBtn');
  btn.style.display = (document.documentElement.scrollTop > 200) ? 'block' : 'none';
};

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' });
}


