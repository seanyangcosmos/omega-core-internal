function simulateGPT() {
  const input = document.getElementById('sentenceInput').value.trim();
  let response = '';

  if (input === '') {
    response = '請輸入語句後再啟動模擬。';
  } else {
    response = `🧠 GPT 模擬回應：根據目前語義模型，句子「${input}」可能具有潛在語用開放性。建議進一步語境分析。`;
  }

  document.getElementById('gptResponse').innerText = response;
}




