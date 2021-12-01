import { readFile } from "fs/promises";

const countIncrements = (nums) => {
  let counter = 0;

  for (let i = 1; i < nums.length; i++) {
    const previousValue = nums[i - 1];
    const currentValue = nums[i];

    if (currentValue > previousValue) {
      ++counter;
    }
  }

  return counter;
};

try {
  const file = await readFile("./input.txt", "utf-8");
  const lines = file.split("\n");

  const increments = countIncrements(lines);
  console.log(increments);
} catch (error) {
  console.error(error);
}
