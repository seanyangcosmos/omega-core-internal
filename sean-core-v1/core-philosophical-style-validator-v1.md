# M42｜哲學風格一致性驗證器模組  
**Module M42: Philosophical Style Coherence Validator Module**

---

## 📌 模組定義

哲學風格一致性驗證器模組專門分析輸入文本是否維持一致的語氣、邏輯傾向與哲學主體性。支援風格範本比對、風格跳脫警示與多階層交叉風格分析，是 M40–M41 的驗證後續模組。

---

## 🧩 功能元件

1. **風格範本匹配器（Style Template Matcher）**  
   - 根據 M40 提供的風格語法進行對應比對。

2. **邏輯傾向分析器（Logical Orientation Analyzer）**  
   - 檢測語句是否一致地採用歸納／演繹／詮釋型邏輯。

3. **角色語氣穩定性測試器（Persona Tone Stability Tester）**  
   - 分析多角色對話中語氣是否一致或產生語用破綻。

4. **語風跳脫偵測器（Style Drift Detector）**  
   - 自動標記語風偏移句並建議修正。

---

## 📂 YAML 標頭

```yaml
id: M42
title: 哲學風格一致性驗證器模組
eng_title: Philosophical Style Coherence Validator Module
type: core-module
version: 1.0
requires:
  - M40
  - M41
provides:
  - 語風一致性驗證
  - 多角色語氣穩定測試
  - 模擬語境中風格偏移標記


