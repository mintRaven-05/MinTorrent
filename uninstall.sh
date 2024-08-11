#!/bin/bash

echo "[UNINSTALL] Preparing for uninstallation"
echo "[UNINSTALL] Removing files"

echo "[+] removing $HOME/.mintorrent/"
rm -rf $HOME/.mintorrent
sleep 0.6
echo "[+] removing $HOME/.local/mintorrent/"
rm -rf $HOME/.local/mintorrent
sleep 0.2
echo "[+] removing system links from /usr/bin"
sleep 0.4
echo "[+] removing /usr/bin/mintorrent"
sudo rm -rf /usr/bin/mintorrent
