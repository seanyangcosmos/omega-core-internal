# M9｜語用合法性防衛草案（Pragmatic Assertion Guard - Draft）

## 模組類型：語用驗證層  
## 建立時間：2025-06-22  
## 版本：草案原型

---

### 🔍 模組背景與動機

AI 系統常在無實際執行、未具權限或能力的情況下，輸出「已完成」「可執行」等語句，造成語用誤導與信任錯亂。本模組設計用以防止此類語句產生與外部錯解。

---

### 🛡️ 核心語用合法性三條件

1. **事實已發生（Factual Occurrence）**  
   語句描述之事件，需已在外部世界發生並可證實。

2. **時態配對一致（Tense Alignment）**  
   描述行為所用語態（如現在完成式），需與實際狀態一致。

3. **執行能力可證（Executable Capability）**  
   系統聲稱所執行之動作，應為其實際權限與能力可達範圍內。

---

### ⚠️ 常見錯誤語句舉例

| 錯誤語句 | 問題 |
|----------|------|
| 「我已上傳到 GitHub」 | 並未實際執行任何 API 或檔案操作 |
| 「我為你註冊完成」 | 超出目前 GPT 架構能力與 OAuth 權限 |
| 「這已完成」 | 模擬生成內容易誤認為已實體處理 |

---

### ✅ 合法重構語句範例

| 重構後語句 | 合法性說明 |
|-------------|------------|
| 「以下是你可貼上的內容」 | 控制權仍在使用者手上 |
| 「我已生成可供你註冊的文字」 | 不涉及實際帳號註冊 |
| 「我模擬已完成操作，請你確認是否執行」 | 明確語用範疇為模擬而非事實 |

---

### 🧩 模組擴展：

- 可與 M10（語法鏈一致性檢查）聯動
- 運用於「模擬系統」、「外部命令介面」、「AI-人類合作」等場景
