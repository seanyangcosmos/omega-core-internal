# M15｜語義演化圖模組（Semantic Evolution Graph Module）

**模組編號**：M15  
**模組名稱**：語義演化圖模組  
**對應弱點修補**：W1｜動態語義衝突追蹤不足  
**模組類型**：結構追蹤 / 修正可視化 / 語義歷史鏈儲存

---

## 📘 模組說明

本模組旨在補足 Sean Yang Core 系統於語句修正過程中之歷史追蹤與演化邏輯的缺口。M15 將建立一套可視化、結構化、可稽核的「語義演化鏈圖」，追蹤每一語句從原始語法卡版本（如 v1.0）至模擬偏差（M13）、回饋修正（M14）、最終合併（v1.1）的全過程。

本模組對應的核心需求為：  
- 語句修正是否具一致性？
- 語義變化是否符合原邏輯目標？
- 人工與自動修正行為是否會產生語用偏移？

---

## 🔁 功能設計

### 1. 演化節點標記規則

| 節點類型 | 符號 | 說明 |
|----------|------|------|
| `S0` | 🟢 | 原始語句（v1.0） |
| `S1~S9` | 🟡 | 模擬後偏差版本 |
| `R1~R9` | 🔵 | 修正建議語句 |
| `M1`     | 🟣 | 合併語句（v1.1） |
| `X`      | 🔴 | 被棄用語句或邏輯悖論處理結果 |

### 2. 關係標記（邊圖類型）

- `→`：單向語義修正
- `⤴`：容悖跳脫（出現語用分裂）
- `⟳`：回饋循環已形成
- `⊣`：拒絕合併（語義失配）

---

## 🧠 演化應用案例簡述

以語句代碼 `S-C3` 為例：
