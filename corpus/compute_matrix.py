#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from cc_pathlib import Path

lang = "fr"

def get_letters() :
	return Path("letters.json").load()[lang]

def is_valid(word, letters) :
	for c in word :
		if c not in letters :
			return False
	return True

pth = Path("word.fr.tsv")
letters = Path("letters.json").load()["fr"]

if not pth.is_file() :
	w_set = set()
	with Path("frwiki-latest-all-titles-in-ns0.txt").open('rt') as fid :
		for line in fid.readlines() :
			line = line.strip().strip('"').lower()
			if is_valid(line, letters) :
				w_set.add(line)
	pth.write_text('\n'.join(sorted(w_set)))
	print(len(w_set))

m_arr = np.zeros((len(letters), len(letters)), dtype=np.uint32)
for word in pth.read_text().splitlines() :
	for a, b in zip(word[:-1], word[1:]) :
		i, j = letters.index(a), letters.index(b)
		m_arr[i, j] += 1

print(m_arr)

for i in range(len(letters)) :
	for j in range(len(letters)) :
		if m_arr[i, j] == 0 :
			print(f"{letters[i]} -> {letters[j]}")

plt.imshow(m_arr)
plt.show()