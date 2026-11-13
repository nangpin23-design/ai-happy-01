# Make the AI judge happy — ai-happy-01

Entry for https://make.fun/bounty/ai-happy-01

`main.py` copies `entry.png` (a joyful golden retriever puppy smiling in a
sunny wildflower meadow at golden hour) to `/output/entry.png`.
Deterministic, no network, no randomness — both runs write the same bytes.

Image: PNG, 800x800, under 1 MiB.

Run locally:

```sh
python3 main.py
ls -lh /output/entry.png
```
