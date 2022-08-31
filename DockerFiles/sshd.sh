if [[ $EUID -ne 0 ]]; then
   exit 2
fi
read -r -p "Do you want to change the SSH port? [Y/N]" response
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then
   read -p "Choose between 1024 and 65535: " sshportconfig
   if (( ("$sshportconfig" > 1024) && ("$sshportconfig" < 65535) )); then
    echo "Port $sshportconfig" >> /etc/ssh/sshd_config
    echo "SSH port has been changed to: $sshportconfig"
   else
    echo "This port is unacceptable"
    exit 1
   fi
else 
   sshPort=$(grep "Port" /etc/ssh/sshd_config) | head -n 1
   exit 1
fi
exit 0


# below is the list of main commands i carried out on the terminal to disable the root login and to make sure there is at least one user with sudo priviliges

# adduser newuser
# passwd newuser

# visudo
# ## Allow root to run any commands anywhere
# root    ALL=(ALL)       ALL
# newuser ALL=(ALL)       ALL

# sudo usermod -s /usr/sbin/nologin root