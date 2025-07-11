// jason/core_judge.js
import parseSemanticBlocks from './m2_blocks.js';
import assignSemanticRoles from './m11_semantic_roles.js';
import detectConflict from './m16_conflict_check.js';
import checkSemanticIntegrity from './m21_semantic_integrity.js';

export async function evaluateInput(input) {
  let results = [];

  const blockResult = parseSemanticBlocks(input);
  results.push(blockResult);

  const roleResult = assignSemanticRoles(input);
  results.push(roleResult);

  const conflictResult = detectConflict(input);
  results.push(conflictResult);

  const integrityResult = checkSemanticIntegrity(results);
  results.push(integrityResult);

  // 主回應產出邏輯（簡化版）
  let mainStatus = 'undecided';
  if (conflictResult.status === 'paradox') {
    mainStatus = '容誖語句';
  } else if (integrityResult.status === 'integrity-error') {
    mainStatus = '語義錯亂';
  } else if (blockResult.status === 'structured' && roleResult.status === 'complete') {
    mainStatus = '結構良好，具備語義意識';
  }

  return {
    input,
    mainStatus,
    modules: results
  };
}
