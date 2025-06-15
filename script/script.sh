#!/usr/bin/env bash
INPUT="/home/hatim/Downloads/api_methods.csv"
OUTPUT="live-epi.txt"
: > "$OUTPUT"

MAXJ=20
DELAY=0.2

while IFS=',' read -r method host path; do
  # 1) Remove *all* double‑quotes
  host=${host//\"/}
  path=${path//\"/}

  # 2) Trim any leading/trailing whitespace
  host=$(echo $host | xargs)
  path=$(echo $path | xargs)

  # Skip blank or still‑invalid entries
  if [[ -z "$host" || "$path" == *"{"* ]]; then
    echo "[SKIP] bad entry: '$host$path'" >&2
    continue
  fi

  url="https://${host}${path}"
  echo "[DEBUG] Scanning: $method $url" >&2

  (
    httpx "$url" -m "$method" >> "$OUTPUT"
  ) &

  sleep "$DELAY"

  while (( $(jobs -rp | wc -l) >= MAXJ )); do
    wait -n
  done
done < "$INPUT"

wait
echo "Done – results in $OUTPUT"