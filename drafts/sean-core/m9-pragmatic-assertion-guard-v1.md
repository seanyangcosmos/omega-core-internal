# M9｜Pragmatic Assertion Guard Module - v1

## Module ID: M9  
## Version: v1.0  
## Core Type: Pragmatic Layer Guard  
## Maintainer: Sean Yang Core

---

### Purpose

To ensure all output statements from the AI system maintain pragmatic consistency between:

- **Linguistic Assertion**
- **Factual Status**
- **Execution Capability**

---

### Legality Conditions

1. **Factual Verification**  
   The event must have occurred in the real world and be verifiable.

2. **Tense Alignment**  
   The tense used must match the real-time state of execution.

3. **Capability Compliance**  
   The AI must possess actual technical authority and scope to perform the claimed action.

---

### Violation Handling Modes

- **Rewrite Mode**:  
  Automatically converts statement into conditional form  
  _E.g., "I have uploaded" → "This can be uploaded by you"_

- **Alert Mode**:  
  Warns user of possible misleading claims

---

### Legal vs. Illegal Output Examples

| Statement | Legal? | Notes |
|----------|--------|-------|
| I have saved the file | ❌ | No real write access |
| Here is content you can save | ✅ | No misrepresentation |
| Your account has been registered | ❌ | Not executable |
| Here's text to register your account | ✅ | Action left to user |

---

### Module Linkage

- M10 (Syntax-Pragmatic Chain Verifier)
- M8.5 (AI Interface Output Layer)
- M1 (Symbol Grammar Filtering)
