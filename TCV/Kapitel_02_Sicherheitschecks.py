

import random

from IPython.display import clear_output


def convert_list_to_string(lst, magic_byte, num_elements):

    selected_elements = lst[:num_elements]

    result_string = ''.join(chr(element ^ magic_byte) for element in selected_elements)

    return result_string


def write_text(lst, magic_byte):

    for i in range(len(lst)):

        print("\r", convert_list_to_string(lst, magic_byte, i), end="")


    print("")

    return


def spin_cursor(num_spins):

    for i in range(num_spins):

        for cursor in "\|/-":

            print("\r", cursor, end="")


    print("")

    return


def secure_communication(magic_byte,enc_message):

    write_text(enc_message,magic_byte)

    spin_cursor(10)

    clear_output(wait=True)

    return


def get_random_flag(num_elements):

    enc_flag = []

    for i in range(num_elements):

        enc_flag.append(random.randint(65, 90))

    return enc_flag


def modify_flag(ni,mb1,em1,mb2,em2,mb3,em3,mb4,em4):

    for i in range(50):

        enc_flag = get_random_flag(32)

        if(i >= ni-32): enc_flag[0] = em1[46]^mb1

        if(i >= ni-31): enc_flag[1] = em2[44]^mb2

        if(i >= ni-30): enc_flag[2] = em4[1]^mb4

        if(i >= ni-29): enc_flag[3] = em1[69]^mb1

        if(i >= ni-28): enc_flag[4] = em1[71]^mb1

        if(i >= ni-27): enc_flag[5] = em4[4]^mb4

        if(i >= ni-26): enc_flag[6] = em1[75]^mb1

        if(i >= ni-25): enc_flag[7] = em4[22]^mb4

        if(i >= ni-24): enc_flag[8] = em4[0]^mb4

        if(i >= ni-23): enc_flag[9] = em2[0]^mb2

        if(i >= ni-22): enc_flag[10] = em1[8]^mb1

        if(i >= ni-21): enc_flag[11] = em3[15]^mb3

        if(i >= ni-20): enc_flag[12] = em4[19]^mb4

        if(i >= ni-19): enc_flag[13] = em3[33]^mb3

        if(i >= ni-18): enc_flag[14] = em1[39]^mb1

        if(i >= ni-17): enc_flag[15] = em1[38]^mb1

        if(i >= ni-16): enc_flag[16] = em4[7]^mb4

        if(i >= ni-15): enc_flag[17] = em2[42]^mb2

        if(i >= ni-14): enc_flag[18] = em4[32]^mb4

        if(i >= ni-13): enc_flag[19] = em1[1]^mb1

        if(i >= ni-12): enc_flag[20] = em1[4]^mb1

        if(i >= ni-11): enc_flag[21] = em4[35]^mb4

        if(i >= ni-10): enc_flag[22] = em4[7]^mb4

        if(i >= ni-9): enc_flag[23] = em1[30]^mb1

        if(i >= ni-8): enc_flag[24] = em3[11]^mb3

        if(i >= ni-7): enc_flag[25] = em2[7]^mb2

        if(i >= ni-6): enc_flag[26] = em4[7]^mb4

        if(i >= ni-5): enc_flag[27] = em4[25]^mb4

        if(i >= ni-4): enc_flag[28] = em4[47]^mb4

        if(i >= ni-3): enc_flag[29] = em4[50]^mb4

        if(i >= ni-2): enc_flag[30] = em3[10]^mb3

        if(i >= ni-1): enc_flag[31] = em4[5]^mb4

        print("\r", convert_list_to_string(enc_flag, magic_byte_5, len(enc_flag)+1), end="")


    return


magic_byte_1 = 0xDE;

enc_message_1 = [141,170,191,172,170,187,254,141,183,189,

                 182,187,172,182,187,183,170,173,34,188,

                 187,172,174,172,34,184,171,176,185,254,

                 186,187,173,254,138,187,189,182,176,177,

                 178,177,185,183,187,254,157,191,179,174,

                 171,173,254,136,183,178,173,182,177,184,

                 187,176,254,243,254,156,151,138,138,155,

                 254,137,159,140,138,155,144,240,240,240];

secure_communication(magic_byte_1,enc_message_1)


magic_byte_2 = 0xAD;

enc_message_2 = [224,204,213,196,192,204,193,200,141,254,

                 196,206,197,200,223,197,200,196,217,222,

                 222,217,216,203,200,141,128,141,236,198,

                 217,196,219,196,200,223,200,141,238,131,

                 229,131,255,131,226,131,227,131,226,131,

                 254,131,141,236,207,222,206,197,196,223,

                 192,216,195,202,131,131,131];

secure_communication(magic_byte_2,enc_message_2)


magic_byte_3 = 0xBE;

enc_message_3 = [248,66,214,204,219,158,247,218,219,208,

                 202,215,202,90,202,205,66,220,219,204,

                 206,204,66,216,203,208,217,158,203,208,

                 218,158,246,215,208,202,219,204,217,204,

                 203,208,218,66,220,219,204,206,204,66,

                 216,203,208,217,158,218,203,204,221,214,

                 144,144,144];

secure_communication(magic_byte_3,enc_message_3)


magic_byte_4 = 0xEF;

enc_message_4 = [148,171,160,161,170,146,207,176,207,174,

                 131,131,138,207,172,135,138,140,132,156,

                 207,160,164,206,207,181,154,136,142,129,

                 136,207,138,157,155,138,134,131,155,193,

                 207,173,138,157,138,134,155,138,207,156,

                 134,140,135,138,157,138,129,207,187,157,

                 142,129,156,137,138,157,207,139,138,157,

                 207,169,131,142,136,136,138,207,153,128,

                 157,193,193,193];

secure_communication(magic_byte_4,enc_message_4)


magic_byte_5 = 0x00;

modify_flag(50,magic_byte_1,enc_message_1,magic_byte_2,

            enc_message_2,magic_byte_3,enc_message_3,

            magic_byte_4,enc_message_4)