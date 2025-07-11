// jason/m11_semantic_roles.js
export default function analyzeRoles(input) {
  const agentPattern = /\b(I|we|you|he|she|they|Sean|Yang)\b/i;
  const actionPattern = /\b(thinks|proves|defines|creates|writes|constructs|analyzes|explores)\b/i;
  const objectPattern = /\b(structure|system|theory|model|truth|AI|language|core)\b/i;

  const hasAgent = agentPattern.test(input);
  const hasAction = actionPattern.test(input);
  const hasObject = objectPattern.test(input);

  if (hasAgent && hasAction && hasObject) {
    return {
      module: 'M11',
      status: 'complete-role',
      message: 'Agent-Action-Object roles clearly identified'
    };
  } else if (hasAgent && hasAction) {
    return {
      module: 'M11',
      status: 'partial-role',
      message: 'Agent and Action detected, object missing'
    };
  } else {
    return {
      module: 'M11',
      status: 'insufficient',
      message: 'Semantic roles not clearly established'
    };
  }
}



