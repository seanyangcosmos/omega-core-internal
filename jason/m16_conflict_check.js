// jason/m16_conflict_check.js
export default function detectConflict(input) {
  const paradoxPhrases = [
    'this statement is false',
    'i know that i know nothing',
    'can an omnipotent being create a rock he cannot lift',
    'self-reference',
    'circular logic',
    'simultaneously true and false',
    '既封閉又開放',
    '容誖'
  ];

  const contradictionPatterns = [
    /\btrue\b.*\bfalse\b/,
    /\b永遠成立\b.*\b但也不成立\b/,
    /\b無限\b.*\b邊界\b/,
    /\b不能定義\b.*\b仍成立\b/
  ];

  const lowerInput = input.toLowerCase();

  for (let phrase of paradoxPhrases) {
    if (lowerInput.includes(phrase.toLowerCase())) {
      return {
        module: 'M16',
        status: 'paradox',
        message: `Detected paradoxical phrase: "${phrase}"`
      };
    }
  }

  for (let pattern of contradictionPatterns) {
    if (pattern.test(input)) {
      return {
        module: 'M16',
        status: 'contradiction',
        message: 'Detected internal contradiction pattern'
      };
    }
  }

  return {
    module: 'M16',
    status: 'clean',
    message: 'No clear contradiction or paradox detected'
  };
}



