def simple_structure_check(sentence):
    """
    基礎結構檢查，僅示意：
    - 檢查句尾標點
    - 可擴展更多規則
    """
    if sentence.endswith("。") or sentence.endswith(".") or sentence.endswith("!"):
        return True, "結構檢查通過"
    else:
        return False, "結構檢查未通過：缺少結尾標點"

