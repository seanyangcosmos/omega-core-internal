document.getElementById("submitButton").addEventListener("click", async () => {
  const inputText = document.getElementById("inputText").value.trim();
  const resultDiv = document.getElementById("result");

  if (!inputText) {
    resultDiv.innerHTML = "⚠️ 請輸入語句後再點擊分析。";
    return;
  }

  resultDiv.innerHTML = "⏳ 分析中… 請稍候";

  try {
    const response = await fetch("http://202.182.124.69:3001/semantic", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ sentence: inputText })
    });

    if (!response.ok) {
      throw new Error(`伺服器回應錯誤：${response.status}`);
    }

    const result = await response.json();

    resultDiv.innerHTML = `
      <strong>【語義類型】</strong>：${result.semanticType}<br>
      <strong>【判斷結果】</strong>：${result.judgement}<br>
      <strong>【補充說明】</strong>：${result.comment}<br>
      <strong>【系統語義備註】</strong>：${result.systemNote}
    `;
  } catch (error) {
    console.error("❌ 錯誤：", error);
    resultDiv.innerHTML = "🚫 無法與後端伺服器連線，請稍後再試或確認伺服器已啟動。";
  }
});


