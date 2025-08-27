export default function cleanSet(mySet, startString) {
  const newArray = [];
  mySet.forEach((value) => {
    if (value && value.startsWith(startString)) {
      newArray.push(value.slice(startString.length));
    }
  });
  return newArray.join("-");
}
