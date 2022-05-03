from datetime import datetime
import sys


def timestamp(t1):

    # https: // www.geeksforgeeks.org / python - datetime - strptime - function /
    t1 = datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
    # Getting the current time
    t2 = datetime.now()

    # print(t2)

    # get the difference in the two timestamps
    t3 = t2 - t1
    s = str(t3)



    if len(s) <= 15:

        # ['19', '19', '22.717437']
        sys.exit()

        # 19
        hour = int(s.split(':')[0])

        # 19
        minutes = int(s.split(':')[1])

    else:

        s = s.split(',')[1].lstrip()
        hour = int(s.split(':')[0])
        minutes = int(s.split(':')[1])

    print(hour, minutes)

timestamp('2022-04-17 20:12:44')