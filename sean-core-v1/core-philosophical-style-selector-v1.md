# M40｜哲學人格風格選擇器模組  
**Module M40: Philosophical Persona Style Selector Module**

---

## 📌 模組定義

哲學人格風格選擇器模組負責管理多種哲學角色風格設定，提供語用語氣、邏輯結構偏好與語義表達習慣的風格化參數，支援在多角色、多語境下的哲學人格生成與一致性維持。

---

## 🎭 風格構成要素

1. **語用語氣層（Pragmatic Tone Layer）**  
   - 包含語調（冷靜／激進）、禮貌層級、質疑與肯定頻率等。

2. **邏輯偏好層（Logical Preference Layer）**  
   - 偏好使用歸納／演繹、分析／綜合、閉環／開放等風格。

3. **語義結構層（Semantic Syntax Layer）**  
   - 包含語法結構、名詞化密度、關係詞使用頻率等。

---

## 🔧 樣式範本（Style Profiles）

| 樣式名稱 | 描述 | 風格參數範例 |
|----------|------|----------------|
| 古典理性主義 | 強調演繹與結構嚴謹性 | 冷靜、邏輯閉環、低質疑頻率 |
| 開放解構派 | 偏好隱喻與語義遊戲 | 熱烈、語義浮動、高質疑頻率 |
| 溫和詮釋主義 | 強調同理與語用柔性 | 中性、語氣溫和、中頻肯定 |

---

## 📂 YAML 標頭

```yaml
id: M40
title: 哲學人格風格選擇器模組
eng_title: Philosophical Persona Style Selector Module
type: core-module
version: 1.0
requires:
  - M39
  - M15
provides:
  - 風格化人格模板
  - 語氣與語法風格參數
  - 哲學風格一致性管理


