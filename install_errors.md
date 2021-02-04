# Install Errors

Debugging some errors, especialy with Windows 10 Home + Docker + GitHub.

Windows 10 Enterprise can use the Hyper-V, but Windows 10 Home must use the WSL2. But, Docker should work with Windows 10 Home with some other settings adjusted.

Error when cloning: 
`Git init: fatal: could not set 'core.filemode' to 'false'`

Try this in Ubuntu: `sudo git clone https://github.com/YOUR-USERNAME/simple-coronavirus-report.git`
* [Stackoverflow: use sudo](https://stackoverflow.com/questions/50108363/git-init-fatal-could-not-set-core-filemode-to-false)
* [Set WSL to version 2](https://www.tenforums.com/tutorials/164318-how-set-linux-distribution-version-wsl-1-wsl-2-windows-10-a.html) 
    *  [Check what WSL you're running](https://askubuntu.com/questions/1177729/wsl-am-i-running-version-1-or-version-2) 
