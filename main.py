"""Analyse workstation boot times and flag slow boots.

Usage: python3 main.py boots.csv [--slow-seconds 120]
CSV columns: workstation,boot_date,boot_seconds.
- SLOW: boot took more than --slow-seconds (default 120 s) - check
  startup programs, disk health and pending updates.
- OK: boot at or under the limit.
Slowest boot first, then the average boot time across all boots.
"""
import argparse, csv, sys

def analyse(rows, slow_seconds=120):
    out = []
    for row in rows:
        seconds = int(row["boot_seconds"])
        verdict = "SLOW" if seconds > slow_seconds else "OK"
        out.append((row["workstation"].strip(), row["boot_date"].strip(),
                    seconds, verdict))
    return sorted(out, key=lambda r: (-r[2], r[0]))

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--slow-seconds", type=int, default=120)
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        results = analyse(list(csv.DictReader(f)), args.slow_seconds)
    for workstation, boot_date, seconds, verdict in results:
        print(f"{workstation}: {verdict} ({seconds} s, booted {boot_date})")
    average = round(sum(r[2] for r in results) / len(results), 1) if results else 0.0
    print(f"Average boot time: {average:.1f} s across {len(results)} boot(s); "
          f"{sum(1 for *_, v in results if v == 'SLOW')} slow boot(s) over {args.slow_seconds} s.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
