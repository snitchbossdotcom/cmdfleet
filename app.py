import argparse  # this big boy handles the arguments so dont argue with it :)

from multiprocessing import Pool  # The real work handling big boi :3

import subprocess


def run(args):
    ip, cmd = args

    ip = ip.strip()

    if not ip:
        return

    running = subprocess.run(["ssh", "-o", "ConnectTimeout=10", "-o", "BatchMode=yes", ip, cmd],
                             capture_output=True,
                             text=True)

    return ip, running.stdout, running.stderr


# print(ip)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='CmdFleet',
        description='CmdFleet helps sysadmins to easily run a command across multiple servers',
        epilog='Made by Snitch'  # touch this = epstein will come and touch you
    )

    parser.add_argument('-c', '--command', required=True)

    args = parser.parse_args()
    cmd = args.command

    # grab the ips :)))
    with open("ips.txt", "r") as file:
        ip_list = file.read().splitlines()


    # Testing
    # def run(cmd):
    #   running = subprocess.run([ssh, froot@{}])
    # End of Testing


    # testing bs
    # print(ips.read().splitlines())
    #
    # ips.close()
    #
    # end of testing bs


    jobs = [(ip, cmd) for ip in ip_list]

    with Pool() as p:
        results = p.map(run, jobs)

for result in results:
    if result is None:
        continue

    ip, stdout, stderr = result

    print(f"\n{ip}:")
    print(stdout, end="\n")


    if stderr:
        print(stderr, end="\n")


print("worked successfully :)")