#!/bin/bash

current_elf_no=1
current_elf_sum=0
fattest_elf=0
fattest_elf_sum=0

while read -r line; do
  if [ -z "$line" ]; then
    if [[ $current_elf_sum -gt $fattest_elf_sum ]]; then
      fattest_elf_sum=$current_elf_sum
      fattest_elf=$current_elf_no
    fi
    echo "elf ${current_elf_no} sum: ${current_elf_sum}"
    current_elf_sum=0
    current_elf_no=$((current_elf_no + 1))
    continue
  fi
  current_elf_sum=$((current_elf_sum + line))
done < input.txt

echo "fattest_elf: ${fattest_elf}, calories: ${fattest_elf_sum}"
