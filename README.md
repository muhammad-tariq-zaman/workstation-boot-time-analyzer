# workstation-boot-time-analyzer

Analyse workstation boot times from a CSV: SLOW when a boot takes more than --slow-seconds (default 120 s), otherwise OK — slowest boot first, with the average boot time across all boots.

Sample input is included (boots.csv with four workstation boots).

## How to run

```sh
python3 main.py boots.csv
```

## Example output

```
WS-2: SLOW (210 s, booted 2026-11-10)
WS-4: SLOW (130 s, booted 2026-11-10)
WS-1: OK (95 s, booted 2026-11-10)
WS-3: OK (45 s, booted 2026-11-10)
Average boot time: 120.0 s across 4 boot(s); 2 slow boot(s) over 120 s.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
