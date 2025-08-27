export default function hasValuesFromArray(mySet, myArray) {
  return myArray.every((element) => mySet.has(element));
}
