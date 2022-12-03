export default function extractDecimalNumber(fieldName: string): any {
  return {
    $substr: [fieldName, 0, 999]
  };
}
