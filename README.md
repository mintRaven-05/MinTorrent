<h1 align=center>MinTorrent</h1>
<p align="center">
  <a href="https://github.com/mintRaven-05/MinTorrent/stargazers"><img src="https://img.shields.io/github/stars/mintRaven-05/MinTorrent?colorA=363a4f&colorB=b7bdf8&style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNTYgMjU2Ij4KPHBhdGggZD0iTTIzNS4yNCw4NC4zOGwtMjguMDYsMjMuNjgsOC41NiwzNS4zOWExMy4zNCwxMy4zNCwwLDAsMS01LjA5LDEzLjkxLDEzLjU0LDEzLjU0LDAsMCwxLTE1LC42OUwxNjQsMTM5bC0zMS42NSwxOS4wNmExMy41MSwxMy41MSwwLDAsMS0xNS0uNjksMTMuMzIsMTMuMzIsMCwwLDEtNS4xLTEzLjkxbDguNTYtMzUuMzlMOTIuNzYsODQuMzhhMTMuMzksMTMuMzksMCwwLDEsNy42Ni0yMy41OGwzNi45NC0yLjkyLDE0LjIxLTMzLjY2YTEzLjUxLDEzLjUxLDAsMCwxLDI0Ljg2LDBsMTQuMjEsMzMuNjYsMzYuOTQsMi45MmExMy4zOSwxMy4zOSwwLDAsMSw3LjY2LDIzLjU4Wk04OC4xMSwxMTEuODlhOCw4LDAsMCwwLTExLjMyLDBMMTguMzQsMTcwLjM0YTgsOCwwLDAsMCwxMS4zMiwxMS4zMmw1OC40NS01OC40NUE4LDgsMCwwLDAsODguMTEsMTExLjg5Wm0tLjUsNjEuMTlMMzQuMzQsMjI2LjM0YTgsOCwwLDAsMCwxMS4zMiwxMS4zMmw1My4yNi01My4yN2E4LDgsMCwwLDAtMTEuMzEtMTEuMzFabTczLTEtNTQuMjksNTQuMjhhOCw4LDAsMCwwLDExLjMyLDExLjMybDU0LjI4LTU0LjI4YTgsOCwwLDAsMC0xMS4zMS0xMS4zMloiIHN0eWxlPSJmaWxsOiAjQ0FEM0Y1OyIvPgo8L3N2Zz4="></a>
  <a href="https://github.com/mintRaven-05/MinTorrent/releases/latest"><img src="https://img.shields.io/github/v/release/mintRaven-05/MinTorrent?colorA=363a4f&colorB=a6da95&style=for-the-badge&logo=github&logoColor=cad3f5"></a>
  <a href="https://github.com/mintRaven-05/MinTorrent/issues"><img src="https://img.shields.io/github/issues/mintRaven-05/MinTorrent?colorA=363a4f&colorB=f5a97f&style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNTYgMjU2Ij4KPHBhdGggZD0iTTIxNiwzMlYxOTJhOCw4LDAsMCwxLTgsOEg3MmExNiwxNiwwLDAsMC0xNiwxNkgxOTJhOCw4LDAsMCwxLDAsMTZINDhhOCw4LDAsMCwxLTgtOFY1NkEzMiwzMiwwLDAsMSw3MiwyNEgyMDhBOCw4LDAsMCwxLDIxNiwzMloiIHN0eWxlPSJmaWxsOiAjQ0FEM0Y1OyIvPgo8L3N2Zz4="></a>
</p>

## Purpose

It is a Linux-based CLI torrent client. It serves the purpose of being lightweight, efficient fast and easy to use interface. Works both with magnets and torrent files, and also comes with a magnet searching feature. Ideal for users who prefer CLI over GUI.

> [!IMPORTANT]
> If the mintorrent doesnt work even after installation. Try installing it once again without uninstalling it!
> The installer script is only compatible with Arch and Debian based distros. If you want to install it in any other distros other than arch and debian, you need to install the dependencies manually

## Installation

An installer script is already made. All you need to do is run the script. Copy the following codes and run it in your terminal.
- Clone the repository

```bash
git clone https://github.com/mintRaven-05/MinTorrent.git
```

- Run the installer script

```bash
cd MinTorrent
chmod +x install.sh
./install.sh
```
## Usage

To search for magnets, use the `-s` flag like this.
```bash
mintorrent -s <YOUR_SEARCH_TERM>

OR

mintorrent --search <YOUR_SEARCH_TERM>
```

If you have torrent file downloaded and want to download it from that file, you can use the `-t` flag like this.
```bash
mintorrent -t /path/to/your/<TORRENT_FILE>.torrent

OR

mintorrent --torrent /path/to/your/<TORRENT_FILE>.torrent
```

If you have magnet file saved in your system and dont want to use the search feature, in that case you can use the `-m` flag like this.
```bash
mintorrent -m /path/to/your/<MAGNET_FILE>

OR

mintorrent --magnet /path/to/your/<MAGNET_FILE>
```

To check the current version of MinTorrent installed, use the `-v` flag likt this.
```bash
mintorrent -v

OR

mintorrent --version
```

To view the help screen, use the `-h` flag like this
```bash
mintorrent -h

OR

mintorrent --help
```

## Demo Screenshot
![240810_20h39m43s_screenshot](https://github.com/user-attachments/assets/025cddd1-376c-4e33-ac5c-216af43ed41a)
![240810_20h45m03s_screenshot](https://github.com/user-attachments/assets/7089b3c6-773a-421e-a9bf-b327b1638f06)
![240810_20h51m43s_screenshot](https://github.com/user-attachments/assets/0bcbbf2d-83ef-4049-bd6f-5d04b4e8ad81)

## Update

>[!NOTE]
>Update feature is not yet implemented. Add this project to your watchlist if you want to use this tool.
To update MinTorrent to the latest version, use the following command
```bash
mintorrent -u

OR

mintorrent --update
```

## Uninstallation

To uninstall MinTorrent from the system you can use following script
```bash
Script:
cd ~/.mintorrent
./uninstall.sh
```

> #### TODO
> - [x] Make is compatible with magnets
> - [x] Make is compatible with torrent files
> - [ ] Add session handling and resume download feature

<p align="center">Copyright &copy; 2024 <a href="https://github.com/mintRaven-05" target="_blank">Debjeet Banerjee</a>
<p align="center"><a href="https://github.com/mintRaven-05/MinTorrent/blob/main/LICENSE"><img src="https://img.shields.io/static/v1.svg?style=for-the-badge&label=License&message=MIT&logoColor=d9e0ee&colorA=363a4f&colorB=b7bdf8"/></a></p>
