// jason/semantic-core.js
import checkStructure from './m1_structure.js';
import checkOpenness from './m6_openness.js';
import analyzeRoles from './m11_semantic_roles.js';
import detectConflict from './m16_conflict_check.js';
import reflectLayers from './m21_reflection.js';
import evaluateComposition from './m31_compositional.js';
import checkMetaAwareness from './m41_meta_aware.js';

export default function runSemanticEngine(input) {
  const results = [];

  results.push(checkStructure(input));
  results.push(checkOpenness(input));
  results.push(analyzeRoles(input));
  results.push(detectConflict(input));
  results.push(reflectLayers(input));
  results.push(evaluateComposition(input));
  results.push(checkMetaAwareness(input));

  return results.filter(r => r !== null);
}


