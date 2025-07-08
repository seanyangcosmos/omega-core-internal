# M12｜語義驗證器模組（Semantic Validator Module）

## 🧩 模組名稱
語義驗證器模組（Semantic Validator Module）

## 🧭 模組代碼
M12

## 🧠 功能說明
此模組負責對 Sean Yang Core 中的語義規則、語句生成與語法結構進行一致性與合法性檢查。它是語義自洽系統的關鍵防線，用以保證每一語句在邏輯推演與語法產生過程中的語義合法性與上下文一致性，並與 M9（語用合法性判斷模組）協同工作。

## 📌 核心職責
- 對語義規則（由 M11 產生）進行邏輯結構驗證
- 確認語句在語法層與語義層的正當性
- 偵測語義模糊、不一致或衝突
- 記錄驗證結果以供 M13 語義模擬器引用
- 可支援自動回饋機制，啟動語義修正（M14）

## 🔧 功能模組構成
- `rule_checker`: 驗證語義規則結構與邏輯連貫性
- `syntax_semantic_mapper`: 映射語法與語義的結構一致性
- `error_flagger`: 偵測語義衝突與模糊語句
- `validation_reporter`: 匯出驗證報告供模擬器使用

## 🧬 模組相依
- 🔗 依賴：M9（語用合法性）、M11（語義規則生成器）
- 📤 輸出：提供語義模擬模組 M13 驗證資料
- 🔁 將回饋予 M14 進行修正

## 🧪 測試與示例
| 語句                         | 驗證結果 | 問題說明                       |
|------------------------------|----------|--------------------------------|
| 「封閉系統必然導向一統結論。」 | ✅ 合法   | 結構一致，語義明確             |
| 「封閉結構開放時並不一統。」 | ⚠️ 可疑  | 語義矛盾但形式正確，需交叉檢查 |

## 🗂️ YAML Metadata

```yaml
module: M12
name: Semantic Validator Module
depends_on: [M9, M11]
outputs_to: [M13]
keywords:
  - semantic validation
  - legality check
  - inconsistency detection
  - pragmatic logic

