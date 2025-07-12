function analyzeSentence() {
  const input = document.getElementById('sentenceInput').value.trim();
  let result = '';

  if (input === '') {
    result = '請輸入語句後再分析。';
  } else if (input.endsWith('。') || input.endsWith('！') || input.endsWith('？')) {
    result = '分類結果：封閉語句 ✅';
  } else if (input.includes('悖') || input.includes('矛盾')) {
    result = '分類結果：容悖語句 ⚠️';
  } else {
    result = '分類結果：開放語句 ⭕️';
  }

  document.getElementById('resultArea').innerText = result;
  document.getElementById('gptResponse').innerText = ''; // 清除 GPT 區
}

function clearResults() {
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

