export default function guardrail(mathFunction) {
  let queue = [];
  try {
    const result = mathFunction();
    queue.push(result);
  } catch (e) {
    queue.push(e.message);
  } finally {
    queue.push("Guardrail was processed");

    return queue;
  }
}
