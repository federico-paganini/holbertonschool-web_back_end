console.log("Welcome to Holberton School, what is your name?");

process.stdin.on("data", (data) => {
  process.write("Your name is: ");
  process.write(data);
  process.exit();
});

process.on("exit", () => {
  console.log("This important software is now closing");
});
