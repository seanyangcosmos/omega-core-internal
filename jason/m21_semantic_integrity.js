// jason/m21_semantic_integrity.js
export default function checkSemanticIntegrity(results) {
  let modules = results.map(r => r.module);
  let issues = [];

  // 基本一致性規則：若有矛盾（M16）則不應同時為封閉成立（M3）
  const hasContradiction = results.some(r => r.module === 'M16' && r.status !== 'clean');
  const hasClosedStatus = results.some(r => r.module === 'M3' && r.status === 'closed-true');

  if (hasContradiction && hasClosedStatus) {
    issues.push('Conflict: M16 detects paradox while M3 claims closure');
  }

  // M11（角色）與 M2（語義區塊）缺一不可
  const hasM11 = modules.includes('M11');
  const hasM2 = modules.includes('M2');

  if (!hasM11 || !hasM2) {
    issues.push('Missing essential module: M11 or M2 absent');
  }

  if (issues.length > 0) {
    return {
      module: 'M21',
      status: 'integrity-error',
      issues: issues
    };
  } else {
    return {
      module: 'M21',
      status: 'integrity-ok',
      message: 'All semantic modules coherent'
    };
  }
}



