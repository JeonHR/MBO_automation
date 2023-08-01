import os, sys
import re
import time

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def parse_log_file(file_name):
    log_data = ""
    find_fail = False
    cal_error_msg_flag = False
    cal_error_msg_item = "None"
    fail_item = ""
    uid = ""
    temp_ant_info = 0
    fail_ant_info = 0
    temp_channel = 0
    fail_channel = 0

    fail_dut_cnt = 0
    pass_dut_cnt = 0

    TX_RX_flag = False
    temp_TX_RX_item = ""
    TX_RX_item = ""

    with open(file_name + '.txt', 'r') as f:

        lines = f.readlines()

        for line in lines:
            log_data += line

            if line.find('The 2DID of DUT') >= 0:
                log_data = line
                temp = line.split("The 2DID of DUT")[1]
                temp = temp.split(" ")[2]
                uid = temp.replace("\n", "")
                continue

            if line.find('CHANNEL                                            ') >= 0:
                splited_line = re.split(' |: |, |\(|\)|\n|\t|=', line)
                while '' in splited_line:
                    splited_line.remove('')

                temp_channel = splited_line[1]

            if line.find('____________________________________________________________') >= 0 and (line.find('UWB_TX_VERIFY')>=0 or line.find('UWB_RX_VERIFY')>=0):
                TX_RX_flag = True

                if line.find("TX") >= 0:
                    temp_TX_RX_item = 'UWB_TX_VERIFY'
                elif line.find("RX") >= 0:
                    temp_TX_RX_item = 'UWB_RX_VERIFY'
                else:
                    temp_TX_RX_item = ""

            if line.find("A                        ") >= 0 and line.find("RF") >= 0 and TX_RX_flag == True:    # Find RF1A ~ RF4A
                splited_line = re.split(' |: |, |\(|\)|\n|\t|=', line)
                while '' in splited_line:
                    splited_line.remove('')

                if splited_line[1] == '1':
                    if line.find("RF1A") >= 0:
                        temp_ant_info = 3
                    elif line.find("RF2A") >= 0:
                        temp_ant_info = 2
                    elif line.find("RF3A") >= 0:
                        temp_ant_info = 1
                    elif line.find("RF4A") >= 0:
                        temp_ant_info = 0
                        TX_RX_flag = False
                        TX_RX_item = temp_TX_RX_item
                        temp_TX_RX_item = ""

            if line.find('[FAILED]') >= 0:
                if find_fail == False:
                    find_fail = True
                    fail_ant_info = temp_ant_info
                    fail_channel = temp_channel

                    splited_line = re.split(' |: |, |\(|\)|\n|\t|=', line)
                    while '' in splited_line:
                        splited_line.remove('')

                    fail_item = splited_line[0]

                    if fail_item.find('BAD') >= 0:
                        fail_item = 'BAD_PKT'

                    if fail_item.find('CAL') >= 0:
                        cal_error_msg_flag = True

                else:
                    if line.find('ERROR_MESSAGE') >= 0:
                        if cal_error_msg_flag:
                            try:
                                error_msg_item = line.split("-")[1].split(";")[0]
                                cal_error_msg_flag = False

                                if cal_error_msg_item == "":
                                    cal_error_msg_item = "None"

                            except:
                                error_msg_item = "None"
                continue

            if line.find('Loop Elapsed Total Time') >= 0:
                if find_fail == True:
                    fail_log_path = "log/fail/"
                    if fail_item.find('CAL') >= 0:
                        fail_folder_name = "{}_{}({})".format(fail_item, error_msg_item.replace(" ", ""), TX_RX_item)
                        createFolder(fail_log_path + fail_folder_name)
                        split_name = fail_log_path + fail_folder_name + '/' + uid + '.txt'
                    else:
                        if fail_ant_info == 99:
                            fail_folder_name = "{}_CH{}".format(fail_item, fail_channel)
                        else:
                            fail_folder_name = "{}_ANT{}({})_CH{}".format(fail_item, fail_ant_info,TX_RX_item, fail_channel)

                        createFolder(fail_log_path + fail_folder_name)
                        split_name = fail_log_path + fail_folder_name + '/' + uid + '.txt'
                    fail_dut_cnt += 1

                    with open(split_name, 'a') as f:
                        f.write(log_data)
                        f.write('\n______________________________________________________________________________\n______________________________________________________________________________\n\n')
                else:
                    split_name = "log/pass/"+ uid + '.txt'
                    pass_dut_cnt += 1

                    with open(split_name, 'a') as f:
                        f.write(log_data)
                        f.write('\n______________________________________________________________________________\n______________________________________________________________________________\n\n')

                find_fail = False
                log_data = ""
                cal_error_msg_flag = False
                cal_error_msg_item = "None"
                uid = ""
                fail_channel = 0
                temp_ant_info = 99
                fail_ant_info = 99
                temp_TX_RX_item = ""
                TX_RX_item = ""

    return pass_dut_cnt, fail_dut_cnt

if __name__ == '__main__':
    start_time = time.time()
    file_name = sys.argv[1]
    print("Please wail until log split done!")

    createFolder('log')
    createFolder('log/pass')
    createFolder('log/fail')

    pass_cnt, fail_cnt = parse_log_file(file_name)

    print("Pass DUT count = {}".format(pass_cnt))
    print("Fail DUT count = {}".format(fail_cnt))
    print("Split Done! Total time = {} s".format(time.time() - start_time))



