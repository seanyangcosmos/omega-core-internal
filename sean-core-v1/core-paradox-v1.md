# V1 語法範例：容悖語法核心集（Paradox-Compatible Syntax）

## 語法 040｜合法語句可包含悖論而不導致崩潰

【語句】：語言系統可容納特定類型的悖論而不破壞整體一致性。  
【語義】：容悖性是語義系統的容錯機制而非邏輯錯誤。  
【形式表示】：Paradoxical(x) ∧ Structured(x) ⇒ Stable(Language)

---

## 語法 041｜悖論需在封閉與開放架構中對位

【語句】：悖論的合法性依其所處架構之開放性與封閉性而定。  
【語義】：開放架構可包容未解的悖論，封閉架構則需局部封環解釋。  
【形式表示】：Paradox(x) ⇒ Valid(x) ⇔ Open(x) ∨ LocallyClosed(x)

---

## 語法 042｜悖論語句需附帶語用說明層

【語句】：所有悖論語句需標示其產生條件與語用邊界。  
【語義】：容悖語句無法脫離語用層而單獨成立。  
【形式表示】：Paradox(x) ⇒ Requires(PragmaticContext(x))
