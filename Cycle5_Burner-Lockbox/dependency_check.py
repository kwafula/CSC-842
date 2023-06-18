#!/usr/bin/env python3
import subprocess

#cmd = 'dpkg-query -W libwixgtk3.0-gtk3-0v5 | grep libwxgtk3.0-gtk3-0v5 | wc -l'
#cmd = 'dpkg-query -W wget | grep wget | wc -l'

def run_shell_command(shell_cmd):
    try:
        pro = subprocess.run(shell_cmd, capture_output=True, text=True, shell=True)#, shell=True,env=myenv,executable='/bin/bash')#
        if pro.stdout:
            print('Subprocess Exitcode: ', pro.stdout)
            print(type(pro.stdout))
            print('-----------------------------------')
            exit_code = pro.stdout
            return exit_code

        elif pro.stderr:
            return f"---------------Error----------------------------------\n {pro.stderr}"

        else:
            return f"[executed]"

    except Exception as ex:
        print("exception occurred", ex)
        return f"   [subprocess broke]"

if __name__ == '__main__':

    cmd = 'dpkg-query -W wget | grep wget | wc -l'
    status_code = run_shell_command (cmd)
    print('status_code outside run_shell_command: ', status_code)
    print(type(status_code))
    print('------------------------------------------')
    if status_code == '1':
        print('Status inside if: ', status_code)
        print(type(status_code))
        x = 1
        print('Exit code: ', x, ' Pakage installed')
    else:
        print('Status inside else: ', status_code)
        print(type(status_code))
        x = 0
        print('Exit code: ', x, ' Package not installed')
