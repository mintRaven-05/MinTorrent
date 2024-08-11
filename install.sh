#!/bin/bash

echo "        .__     ___________                                 __   "
echo "  _____ |__| ___\__    ___/_________________   ____   _____/  |_ "
echo " /     \|  |/    \|    | /  _ \_  __ \_  __ \_/ __ \ /    \   __\ "
echo "|  Y Y  \  |   |  \    |(  <_> )  | \/|  | \/\  ___/|   |  \  |  "
echo "|__|_|  /__|___|  /____| \____/|__|   |__|    \___  >___|  /__|  "
echo "      \/        \/                                \/     \/      "

chmod +x uninstall.sh
chmod +x update.sh

if [ -f "/usr/bin/curl" ]; then
  echo ""
else
  echo "[*] install curl using your package manager after installation"
  echo "[*] The update feature will not work if curl is not installed"
fi

sleep 1
