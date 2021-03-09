# Install Errors

Debugging some errors, especialy with Windows 10 Home + Docker + GitHub.

Windows 10 Enterprise can use the Hyper-V, but Windows 10 Home must use the WSL2. But, Docker should work with Windows 10 Home with some other settings adjusted.

## Ubuntu doesn't work!
```
The WSL optional component is not enabled. Please enable it and try again.
See https://aka.ms/wslinstall for details.
Error: 0x8007007e
```
Try this: 
* [Open Powershell, run as administrator](https://askubuntu.com/questions/966184/new-installation-of-windows-10-and-ubuntu-from-windows-store-error)
* Type `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`


## Docker can't enable Hyper-V
* [](https://forums.docker.com/t/cannot-enable-hyper-v-service/94086)

In Powershell, run as administrator: `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All`


## Error when cloning GitHub repo 
`Git init: fatal: could not set 'core.filemode' to 'false'`

Try this in Ubuntu: `sudo git clone https://github.com/YOUR-USERNAME/simple-coronavirus-report.git`
* [Stackoverflow: use sudo](https://stackoverflow.com/questions/50108363/git-init-fatal-could-not-set-core-filemode-to-false)
* [Set WSL to version 2](https://www.tenforums.com/tutorials/164318-how-set-linux-distribution-version-wsl-1-wsl-2-windows-10-a.html) 
    *  [Check what WSL you're running](https://askubuntu.com/questions/1177729/wsl-am-i-running-version-1-or-version-2) 
