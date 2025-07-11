// jason/m6_openness.js
export default function checkOpenness(input) {
  const closedIndicators = [
    'therefore', 'hence', 'proved', 'Q.E.D.', 'must be', 'necessarily', '唯一解'
  ];

  const openIndicators = [
    'perhaps', 'might', 'could be', 'one possibility', '無限', '任意', '開放結構'
  ];

  const lowerInput = input.toLowerCase();

  for (let term of closedIndicators) {
    if (lowerInput.includes(term.toLowerCase())) {
      return {
        module: 'M6',
        status: 'closed',
        message: `Detected closed-system language: "${term}"`
      };
    }
  }

  for (let term of openIndicators) {
    if (lowerInput.includes(term.toLowerCase())) {
      return {
        module: 'M6',
        status: 'open',
        message: `Detected open-system language: "${term}"`
      };
    }
  }

  return {
    module: 'M6',
    status: 'neutral',
    message: 'No strong open/closed indicators found'
  };
}


