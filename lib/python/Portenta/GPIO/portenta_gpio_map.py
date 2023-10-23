INDEX_TAG = 0
INDEX_CAPABILITIES = 1
INDEX_GPIOCHIP_INFO = 2
INDEX_HD_CONN_POSITION = 3
INDEX_GPIO_OBJ = 4
INDEX_EVENT_TRIGGD = 5
INDEX_EVENT_CB = 6

INDEX_GPIOCHIP_NUM = 0
INDEX_GPIO = 1

BOARD_main_header_map = {
# INDEX    TAG       CAPABILITIES                CHIP#+GPIO#    HD CONNECTOR    GPIO OBJECT PLACEHOLDER
    1  : ["3v3"     ,None                        ,None          ,None,          None],
    2  : ["5v"      ,None                        ,None          ,None,          None],
    3  : ["GPIO02"  ,["GPIO","I2C2_SDA"]         ,(4,21)        ,"J2-45",       None],
    4  : ["5v"      ,None                        ,None          ,None,          None],
    5  : ["GPIO03"  ,["GPIO","I2C2_SCL"]         ,(4,20)        ,"J2-47",       None],
    6  : ["GND"     ,None                        ,None          ,None,          None],
    7  : ["GPIO04"  ,["GPIO","1WIRE","PWM0"]     ,(5,23)        ,"J2-59",       None],
    8  : ["GPIO14"  ,["GPIO","UART3_TX"]         ,(4,29)        ,"J2-25",       None],
    9  : ["GND"     ,None                        ,None          ,None,          None],
    10 : ["GPIO15"  ,["GPIO","UART3_RX"]         ,(4,28)        ,"J2-27",       None],
    11 : ["GPIO17"  ,None                        ,(5,2)         ,"J2-50",       None],
    12 : ["GPIO18"  ,["GPIO","PCM_CLK","I2S_CK"] ,(2,23)        ,"J1-56",       None],
    13 : ["GPIO27"  ,None                        ,(5,6)         ,"J2-58",       None],
    14 : ["GND"     ,None                        ,None          ,None,          None],
    15 : ["GPIO22"  ,["GPIO","SAI_DO"]           ,(3,12)        ,"J2-53",       None],
    16 : ["GPIO23"  ,["GPIO","SAI_CK"]           ,(3,11)        ,"J2-49",       None],
    17 : ["3v3"     ,None                        ,None          ,None,          None],
    18 : ["GPIO24"  ,["GPIO","SAI_FS"]           ,(3,10)        ,"J2-51",       None],
    19 : ["GPIO10"  ,["GPIO","SPI1_MOSI"]        ,(4,7)         ,"J2-42",       None],
    20 : ["GND"     ,None                        ,None          ,None,          None],
    21 : ["GPIO09"  ,["GPIO","SPIO0_MISO"]       ,(4,8)         ,"J2-40",       None],
    22 : ["GPIO25"  ,["GPIO","PWM1"]             ,(5,24)        ,"J2-61",       None],
    23 : ["GPIO11"  ,["GPIO","SPI1_SCLK"]        ,(4,6)         ,"J2-38",       None],
    24 : ["GPIO08"  ,["GPIO","SPI1_CE0_N"]       ,(4,9)         ,"J2-36",       None],
    25 : ["GND"     ,None                        ,None          ,None,          None],
    26 : ["GPIO07"  ,["GPIO","SPI1_CE1_N","PWM2"],(5,25)        ,"J2-63",       None],
    27 : ["RESERVED",["GPIO","I2C0_SDA"]         ,(4,19)        ,"J1-44",       None],
    28 : ["RESERVED",["GPIO","I2C0_SCL"]         ,(4,18)        ,"J1-46",       None],
    29 : ["GPIO05"  ,["GPIO","UART1_RX"]         ,(3,31)        ,"J1-35",       None],
    30 : ["GND"     ,None                        ,None          ,None,          None],
    31 : ["GPIO06"  ,["GPIO","PWM3"]             ,(5,26)        ,"J2-65",       None],
    32 : ["GPIO12"  ,["GPIO","UART1_TX"]         ,(4,0)         ,"J1-33",       None],
    33 : ["GPIO13"  ,["GPIO","PWM4"]             ,(5,27)        ,"J2-67",       None],
    34 : ["GND"     ,None                        ,None          ,None,          None],
    35 : ["GPIO19"  ,["GPIO","I2S_WS"]           ,(2,22)        ,"J1-58",       None],
    36 : ["GPIO16"  ,["GPIO","PWM5"]             ,(5,28)        ,"J2-60",       None],
    37 : ["GPIO26"  ,["GPIO","PWM6"]             ,(5,29)        ,"J2-62",       None],
    38 : ["GPIO20"  ,["GPIO","I2S_SDI"]          ,(2,21)        ,"J1-60",       None],
    39 : ["GND"     ,None                        ,None          ,None,          None],
    40 : ["GPIO21"  ,["GPIO","I2S_SDO"]          ,(2,24)        ,"J1-62",       None],
}

X8_main_header_map = {
    "I2C2_SDA"  : 3 ,
    "I2C2_SCL"  : 5 ,
    "PWM0"      : 7 ,
    "TX3"       : 8 ,
    "RX3"       : 10,
    "GPIO2"     : 11,
    "I2S_CK"    : 12,   
    "GPIO6"     : 13,
    "SAI_DO"    : 15,   
    "SAI_CK"    : 16,   
    "SAI_FS"    : 18,   
    "SPI1_COPI" : 19,   
    "SPIO1_CIPO": 21,   
    "PWM1"      : 22,
    "SPI1_SCK"  : 23,   
    "SPI1_CE"   : 24,   
    "PWM2"      : 26,
    "I2C0_SDA"  : 27,   
    "I2C0_SCL"  : 28,   
    "RX1"       : 29,
    "PWM3"      : 31,
    "TX1"       : 32,
    "PWM4"      : 33,
    "I2S_WS"    : 35,   
    "PWM5"      : 36,
    "PWM6"      : 37,
    "I2S_SDI"   : 38,   
    "I2S_SDO"   : 40,   
}

IMX_main_header_map = {
   149 :  3, 
   148 :  5, 
   183 :  7,       
   157 :  8, 
   156 : 10, 
   87  : 12,       
   108 : 15, 
   107 : 16, 
   106 : 18, 
   135 : 19, 
   136 : 21, 
   184 : 22, 
   134 : 23, 
   137 : 24, 
   185 : 26, 
   147 : 27, 
   146 : 28, 
   127 : 29, 
   186 : 31, 
   128 : 32, 
   187 : 33, 
   86  : 35, 
   188 : 36, 
   189 : 37, 
   85  : 38, 
   88  : 40, 

}

BCM_main_header_map = {
    2  : 3, 
    3  : 5,
    4  : 7,
    5  : 29,
    6  : 31,
    7  : 26,
    8  : 24,
    9  : 21,
    10 : 19,
    11 : 23,
    12 : 32,
    13 : 33,
    14 : 8,
    15 : 10,
    16 : 36,
    17 : 11,
    18 : 12,
    19 : 35,
    20 : 38,
    21 : 40,
    22 : 15,
    23 : 16,
    24 : 18,
    25 : 22,
    26 : 37,
    27 : 13,
}

def test_func():
    return "test"

'''
BCM_analog_header_map = {
    1  : ("A0", ["GPIO"],),
    2  : ("A1", ["GPIO"],),
    3  : ("A2", ["GPIO"],),
    4  : ("A3", ["GPIO"],),
    5  : ("A4", ["GPIO"],),
    6  : ("A5", ["GPIO"],),
    7  : ("A6", ["GPIO"],),
    8  : ("A7", ["GPIO"],),
    9  : ("PWM7", ["GPIO"],),
    10 : ("PWM8", ["GPIO"],),
    11 : ("LICELL", ,),
    12 : ("GPIO0", None,),
    13 : ("3v3", None, None),
    14 : ("UART2_TX", ["GPIO"],),
    15 : ("GND", None, None),
    16 : ("UART2_RX", ["GPIO"],),
}

BCM_fan_connector_map = {
    1  : ("PWM9", ["GPIO"],),
    2  : ("NC", None, None),
    3  : ("5V", None, None),
    4  : ("GND", None, None),
}
'''