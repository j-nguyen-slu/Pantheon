#!/usr/bin/env python3

import argparse

def generate_trace(rate_mbps, duration_seconds, output_file):
    # Convert Mbps to bytes/ms
    bytes_per_ms = int((rate_mbps * 1_000_000) / 8 / 1000)  # Mbps -> bits -> bytes -> per ms

    with open(output_file, 'w') as f:
        for _ in range(duration_seconds * 1000):  # one entry per ms
            f.write(f"{bytes_per_ms}\n")

    print(f"Trace generated: {output_file}")
    print(f"Rate: {rate_mbps} Mbps for {duration_seconds} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Mahimahi-compatible .trace file")
    parser.add_argument('--rate', type=float, required=True, help='Bandwidth rate in Mbps')
    parser.add_argument('--duration', type=int, default=60, help='Duration in seconds (default: 60)')
    parser.add_argument('--output', type=str, required=True, help='Output filename')

    args = parser.parse_args()
    generate_trace(args.rate, args.duration, args.output)
