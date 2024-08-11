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

echo "[INIT] starting installer"
echo "[INIT] preparing the files. . ."
echo "[INIT] preparing to download dependencies. . ."
sleep 0.8

package_1=libtorrent
if pacman -Qs $package_1 >/dev/null; then
  echo "[+] The package $package_1 is installed"
  echo "[+] Skipping libtorrent installation"
else
  echo "[!] The package $package_1 is not installed"
  echo "[+] Preparing to install $package_1. . . "

  sudo pacman -S libtorrent
fi

package_2=libtorrent-rasterbar
if pacman -Qs $package_2 >/dev/null; then
  echo "[+] The package $package_2 is installed"
  echo "[+] Skipping libtorrent installation"
else
  echo "[!] The package $package_2 is not installed"
  echo "[+] Preparing to install $package_2. . . "
  sudo pacman -S libtorrent-rasterbar
fi

if [ -d "$HOME/.local/mintorrent" ]; then
  cp update.sh $HOME/.local/mintorrent
  cp VERSION $HOME/.local/mintorrent
else
  mkdir $HOME/.local/mintorrent
  cp update.sh $HOME/.local/mintorrent
  cp VERSION $HOME/.local/mintorrent
fi

sleep .5

echo "[BUILD] mintorrent build file exists"
echo "[BUILD] moving build files"

transfer_files() {
  for file in *; do
    if [ -f "$file" ]; then
      cp $file $HOME/.mintorrent/backup/
      echo "[!] copying $file to $HOME/.mintorrent/backup/"
      sleep .3
    elif [ -d "$file" ]; then
      cp -r $file $HOME/.mintorrent/backup/
      echo "[!] copying ./$file to $HOME/.mintorrent/backup/"
    else
      echo "[*] unexpected error caused while installation!"
      exit 1
    fi
  done
}
