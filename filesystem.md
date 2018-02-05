Resizing Linux Filesystems can be tricky. Here are some useful commands (almost all of which require sudo priviledges):

Information
$ df -h # show free space in human readable format
$ pvs # show basic info about physical volumes
$ lvs # show basic info about logical volumes
$ mount # show where volumes are mounted
$ fdisk -l # show more detailed information about filesystem

Resizing
$ growpart # see man page
$ pvresize # see man page
$ lvextend # resizing logical volumes
$ resize2fs / xfs_growfs # if you do not use the -r option with lvextend, you need to run one of these commands (ubuntu/centos flavors) as an extra step.
