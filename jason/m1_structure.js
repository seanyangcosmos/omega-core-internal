// jason/m1_structure.js
export default function checkStructure(input) {
  if (typeof input !== 'string' || input.trim() === '') {
    return { module: 'M1', status: 'invalid', reason: 'Empty or invalid input structure' };
  }

  const hasVerb = /\b(is|are|was|were|be|being|been|do|does|did|have|has|had|will|shall|can|may|must|might)\b/i.test(input);
  const hasSubject = /\b(I|you|he|she|it|we|they|this|that|these|those|Sean|Yang)\b/i.test(input);

  if (hasVerb && hasSubject) {
    return { module: 'M1', status: 'valid', message: 'Basic structure OK' };
  } else {
    return { module: 'M1', status: 'warn', message: 'Structure incomplete' };
  }
}

