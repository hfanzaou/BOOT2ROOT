#!/bin/bash

REMOTE_USER="laurie"
REMOTE_HOST="192.168.56.101"
PASSWORD="330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4"
REMOTE_PATH="/tmp/rootbash"
LOCAL_PATH="./rootbash_copy"
SLEEP_INTERVAL=5

while true; do
    echo "[*] Checking at $(date)..."
    sshpass -p "$PASSWORD" ssh -o StrictHostKeyChecking=no "${REMOTE_USER}@${REMOTE_HOST}" "[ -f ${REMOTE_PATH} ]" && {
        echo "[+] /tmp/rootbash found!"
        echo "[*] Downloading file via scp..."
        sshpass -p "$PASSWORD" scp -o StrictHostKeyChecking=no "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}" "${LOCAL_PATH}" && echo "[+] Download complete!"
        break
    }
    sleep "$SLEEP_INTERVAL"
done
