# RDR6 Info

# TxCal 

# Golden
# GM175
RDR6_TxCal_golden_GM175_FID = "8888"
column_names_GM175_golden = "TestDate,Time,Bat_Ctrl,Current,InitCanInterface,Sensor_Comm_Init,Get_Test_Instrument,Init_Tx_Cal,PingDut,Read Gold DAC Val,1666,1667,1668,1669,1685,1686,1687,1688,Org1666,Org1667,Org1668,Org1669,Org1685,Org1686,Org1687,Org1688,MIS, FID,Make_Path,SetTemperatureCompensation,SetCWMode,Select_TX_Antenna,Gold Temp,Temperature,Antenna1 GetTxPower,Point2309, Point2310, Point5046, Point5048,SetCWMode,Bat_Ctrl"
total_test_item_golden_RDR6_GM175 = 41

# Chrysler
RDR6_TxCal_golden_Chrysler_FID = "0000"
column_names_Chrysler_golden = "TestDate,Time,Temperature,Antenna1 GetTxPower"
total_test_item_golden_RDR6_Chrysler = 4

# Production
RDR6_test_result_col_names = "Date,Time,Test Time,Nest,MIS,Pass/Fail"
RDR6_total_test_result_item_num = 6
# GM175
RDR6_TxCal_prod_GM175_FID = "0000"
column_names_GM175_prod = "TestDate,Time,Bat_Ctrl,Current,InitCanInterface,Sensor_Comm_Init,Get_Test_Instrument,Init_Tx_Cal,PingDut,MIS, FID,Point 1571,Point 1572,Point 1573,Point 1574,Point 1575,Point 1576,WritePointCsvValue,WriteNBMailboxPoints,Temperature,Make_Path,SetTemperatureCompensation,SaveConfigPoints,Force_Radar_Mode,RCTA Occupied BW,Select_TX_Antenna,SetCWMode,SetTemperatureCompensation,Tx1 BSD,Tx1 RCTA,Tx2 BSD,Tx2 RCTA,Point 1481,Point 1482,Point 1666,Point 1667,Point 1668,Point 1669,Point 1792,Point 1883,Point 1884,Point 1885,Point 1886,Point 1887,Point 1888,offset1,offset2,Average1,Average2,NumbZeroCrossing1,NumbZeroCrossing2,FreqComp,SetTemperatureCompensation,Antenna1 GetTxPower,Point2309, Point2310, Point5046, Point5048,Antenna2 GetTxPower,Point2309, Point2310, Point5046, Point5048,Antenna1 GetCenterFrequency,Antenna2 GetCenterFrequency,Antenna1 GetCwLeakage,Antenna2 GetCwLeakage,SetCWMode,Temperature,Delta,SaveConfigPoints,SerialpointsCheck,ReadPointCSV,VerifyNBMailboxPoints,Bat_Ctrl"
total_test_item_prod_RDR6_GM175 = 75

# Chrysler
RDR6_TxCal_prod_Chrysler_FID = "0000"
column_names_Chrysler_prod = "TestDate,Time,MIS,Point 1571,Point 1572,Point 1573,Point 1574,Point 1575,Point 1576,Temperature,Current,RCTA Occupied BW,BSD Occupied BW,Power,Point 1481,Point 1666,Point 1667,Point 1668,Point 1669,Antenna1 GetTxPower,Antenna2 GetTxPower,Antenna1 GetCenterFrequency,Antenna2 GetCenterFrequency,Antenna1 GetCwLeakage,Antenna2 GetCwLeakage,Temperature,Delta"
total_test_item_prod_RDR6_Chrysler = 27


# RDR7 Info

# TxCal 

# Golden
# Honda 1.0
RDR7_TxCal_golden_Honda_1_0_FID = "9999"
RDR7_TxCal_golden_Honda_1_0_drop_index = [2, 13, 18]
column_names_Honda_1_0_golden = "Date,Time,Bat_Ctrl State,InitCanInterface,Sensor_Comm_Init,Init_Tx_Cal,PingDut,ReadGoldDACValError,1666,1667,1668,1669,exp1666,exp1667,exp1668,exp1669,MIS,FID,Make_Path,SetTemperatureCompensation,Temperature,SetCWMode,Select_TX_Antenna,WaitForTemp,Antenna1 GetTxPower,SetCWMode,Bat_Ctrl State"
total_test_item_golden_RDR7_Honda_1_0 = 27


# Honda 1.75
RDR7_TxCal_golden_Honda_175_FID = "8888"
RDR7_TxCal_golden_Honda_175_drop_index = [2]
column_names_Honda_175_golden = "Date,Time,Bat_Ctrl State,AnalogVoltMeas,InitCanInterface,Sensor_Comm_Init,Init_Tx_Cal,PingDut,SetSAtoDefault,ReadGoldDACValError,1666,1667,1668,1669,1885,1886,1887,1888,exp1666,exp1667,exp1668,exp1669,exp1885,exp1886,exp1887,exp1888,MIS,FID,Make_Path,SetTemperatureCompensation,Force_Radar_Mode,SetCWMode,WaitForTemp,Temperature,Antenna1 GetTxPower,Antenna2 GetTxPower,Antenna1 GetCenterFrequency,Antenna2 GetCenterFrequency,SetCWMode,PrepareForPowerdown,Bat_Ctrl State"
total_test_item_golden_RDR7_Honda_175 = 41


# Production
RDR7_test_result_col_names = "Date,Time,Test Time,Nest,MIS,Pass/Fail,FailedTests"
RDR7_total_test_result_item_num = 7
# Honda 1.0
RDR7_TxCal_prod_Honda_1_0_FID = "0000"
RDR7_TxCal_prod_Honda_1_0_drop_index = [15, 48]
column_names_Honda_1_0_prod = "Date,Time,MIS,Bat_Ctrl State,InitCanInterface,Sensor_Comm_Init,Init_Tx_Cal,PingDut,MIS,Point 1571,Point 1572,Point 1573,Point 1574,Point 1575,Point 1576,Temperature,Make_Path,AnalogVoltMeas,GetSWVersion,SetTemperatureCompensation,SetSAtoDefault Status,SaveConfigPoints,Force_Radar_Mode,RCTA Occupied BW,Force_Radar_Mode,Select_TX_Antenna,SetCWMode,SetTemperatureCompensation_1,InitDAC_amp,InitDAC_sw,Power,Point 1481,Point 1666,Point 1667,Point 1668,Point 1669,SetTemperatureCompensation_2,Antenna1 GetTxPower,Antenna2 GetTxPower,Antenna1 GetCenterFrequency,Antenna2 GetCenterFrequency,Antenna1 GetCwLeakage,Antenna2 GetCwLeakage,SetCWMode_1,Temperature_1,Delta,Bat_Ctrl State"
total_test_item_prod_RDR7_Honda_1_0 = 47

# Honda 1.75
RDR7_TxCal_prod_Honda_175_FID = "0000"
RDR7_TxCal_prod_Honda_175_drop_index = [19, 68]
column_names_Honda_175_prod = "Date,Time,MIS,Bat_Ctrl State,AnalogVoltMeas,InitCanInterface,Sensor_Comm_Init,Init_Tx_Cal,GetNbTestVersion,GetNbLibVersion,PingDut,SetSAtoDefault,MIS,Point 1571,Point 1572,Point 1573,Point 1574,Point 1575,Point 1576,Temperature,Make_Path,GetSWVersion,SetTemperatureCompensation,SaveConfigPoints,Force_Radar_Mode,SetCWMode,Select_TX_Antenna,Tx1 BSD,Tx1 RCTA,Tx2 BSD,Tx2 RCTA,Point 1481,Point 1482,Point 1666,Point 1667,Point 1668,Point 1669,Point 1792,Point 1883,Point 1884,Point 1885,Point 1886,Point 1887,Point 1888,FreqComp Offset0,FreqComp Offset1,FreqComp Average0,FreqComp Average1,FreqComp NumbZeroCrossing0,FreqComp NumbZeroCrossing1,FreqComp Result,ResetDSP,SetSAtoDefault,Force_Radar_Mode,RCTA Occupied BW,SetSAtoDefault,SetTemperatureCompensation,Force_Radar_Mode,SetCWMode,Antenna1 GetTxPower,Antenna2 GetTxPower,Antenna1 GetCenterFrequency,Antenna2 GetCenterFrequency,Antenna1 GetCwLeakage,Antenna2 GetCwLeakage,Temperature2,Temperature1,PrepareForPowerdown,Bat_Ctrl State"
total_test_item_prod_RDR7_Honda_175 = 69


# Sensor Test 

# Golden
# GM175
ST_column_names_GM175_golden = "Date,Time,SN,Nest,Pass/Fail,Failed Step,Log PLM limit file version,Check if DUT is GM 1.75,Ping,Check Golden Sample Serial,Measure Current,LCA Main SNR @ -30_GM1.75,LCA Main SNR @ 30,GM1.75 Angle @ -30,GM1.75 Angle @ 0,GM1.75 Angle @ 30"
ST_total_test_item_golden_RDR6_GM175 = 16

# Chrysler
ST_column_names_Chrysler_golden = "Date,Time,SN,Nest,Pass/Fail,Failed Step,Station Name,Sequence Version,Log PLM limit file version,init SensorInterface,Ping,Measure Current,HP faults - left word,HP faults - right word,DSP faults - left word,DSP faults - right word,create file path for data results,MeasData_BSD_Main_10_Honda,create file for Meas. Data,Report Tx1 Power @ -40,Report Tx2 Power @ -40,Report Tx1 Power @ -38,Report Tx2 Power @ -38,Report Tx1 Power @ -36,Report Tx2 Power @ -36,Report Tx1 Power @ -34,Report Tx2 Power @ -34,Report Tx1 Power @ -32,Report Tx2 Power @ -32,Report Tx1 Power @ -30,Report Tx2 Power @ -30,Report Tx1 Power @ -28,Report Tx2 Power @ -28,Report Tx1 Power @ -26,Report Tx2 Power @ -26,Report Tx1 Power @ -24,Report Tx2 Power @ -24,Report Tx1 Power @ -22,Report Tx2 Power @ -22,Report Tx1 Power @ -20,Report Tx2 Power @ -20,Report Tx1 Power @ -18,Report Tx2 Power @ -18,Report Tx1 Power @ -16,Report Tx2 Power @ -16,Report Tx1 Power @ -14,Report Tx2 Power @ -14,Report Tx1 Power @ -12,Report Tx2 Power @ -12,Report Tx1 Power @ -10,Report Tx2 Power @ -10,Report Tx1 Power @ -8,Report Tx2 Power @ -8,Report Tx1 Power @ -6,Report Tx2 Power @ -6,Report Tx1 Power @ -4,Report Tx2 Power @ -4,Report Tx1 Power @ -2,Report Tx2 Power @ -2,Report Tx1 Power @ 0,Report Tx2 Power @ 0,Report Tx1 Power @ 2,Report Tx2 Power @ 2,Report Tx1 Power @ 4,Report Tx2 Power @ 4,Report Tx1 Power @ 6,Report Tx2 Power @ 6,Report Tx1 Power @ 8,Report Tx2 Power @ 8,Report Tx1 Power @ 10,Report Tx2 Power @ 10,Report Tx1 Power @ 12,Report Tx2 Power @ 12,Report Tx1 Power @ 14,Report Tx2 Power @ 14,Report Tx1 Power @ 16,Report Tx2 Power @ 16,Report Tx1 Power @ 18,Report Tx2 Power @ 18,Report Tx1 Power @ 20,Report Tx2 Power @ 20,Report Tx1 Power @ 22,Report Tx2 Power @ 22,Report Tx1 Power @ 24,Report Tx2 Power @ 24,Report Tx1 Power @ 26,Report Tx2 Power @ 26,Report Tx1 Power @ 28,Report Tx2 Power @ 28,Report Tx1 Power @ 30,Report Tx2 Power @ 30,Report Tx1 Power @ 32,Report Tx2 Power @ 32,Report Tx1 Power @ 34,Report Tx2 Power @ 34,Report Tx1 Power @ 36,Report Tx2 Power @ 36,Report Tx1 Power @ 38,Report Tx2 Power @ 38,Report Tx1 Power @ 40,Report Tx2 Power @ 40,Normalized Tx2 Power @ -40,Normalized Tx2 Power @ -38,Normalized Tx2 Power @ -36,Normalized Tx2 Power @ -34,Normalized Tx2 Power @ -32,Normalized Tx2 Power @ -30,Normalized Tx2 Power @ -28,Normalized Tx2 Power @ -26,Normalized Tx2 Power @ -24,Normalized Tx2 Power @ -22,Normalized Tx2 Power @ -20,Normalized Tx2 Power @ -18,Normalized Tx2 Power @ -16,Normalized Tx2 Power @ -14,Normalized Tx2 Power @ -12,Normalized Tx2 Power @ -10,Normalized Tx2 Power @ -8,Normalized Tx2 Power @ -6,Normalized Tx2 Power @ -4,Normalized Tx2 Power @ -2,Normalized Tx2 Power @ 0,Normalized Tx2 Power @ 2,Normalized Tx2 Power @ 4,Normalized Tx2 Power @ 6,Normalized Tx2 Power @ 8,Normalized Tx2 Power @ 10,Normalized Tx2 Power @ 12,Normalized Tx2 Power @ 14,Normalized Tx2 Power @ 16,Normalized Tx2 Power @ 18,Normalized Tx2 Power @ 20,Normalized Tx2 Power @ 22,Normalized Tx2 Power @ 24,Normalized Tx2 Power @ 26,Normalized Tx2 Power @ 28,Normalized Tx2 Power @ 30,Normalized Tx2 Power @ 32,Normalized Tx2 Power @ 34,Normalized Tx2 Power @ 36,Normalized Tx2 Power @ 38,Normalized Tx2 Power @ 40,EIRP delta,Tx1 EIRP,RCTA Squint SNR @ -40_Honda,MeasData_RCTA_Squint_0_Honda,RCTA Squint Range @ 0 Honda,RCTA Squint SNR @ 0 _Honda,RCTA Squint SNR @ 10 Honda,RCTA Squint Range @ 30,RCTA Squint SNR @ 30,RCTA Squint Range @ 40,RCTA Squint SNR @ 40,RCTA Squint Range @ 50,RCTA Squint SNR @ 50,RCTA Main SNR @ -20,MeasData_RCTA_Main_0,RCTA Main SNR @ 0,RCTA Main Angle @ 20,RCTA Main Range @ 20,RCTA Main SNR @ 20,RCTA Main SNR @ 40,RCTA Main Angle @ -40_Honda,RCTA Main Angle @ -20,RCTA Squint Angle @ 10_Honda,RCTA Squint Range @ 10 Honda,RCTA Main Angle @ 10_Honda,RCTA Squint Angle @ 30,RCTA Main Angle @ 30,RCTA Main Angle @ 40,RCTA Squint Angle @ 40,RCTA Squint Angle @ 50,RCTA Main Angle @ 50,Test Time"
ST_total_test_item_golden_RDR6_Chrysler = 174

# Production
# GM175
ST_column_names_GM175_prod = "Date,Time,SN,Nest,Pass/Fail,Failed Step,init SensorInterface,Check if DUT is GM 1.75,Ping,Measure Current,Log raw HP faults - left word,Log raw HP faults - right word,Log raw DSP faults - left word,Log raw DSP faults - right word,HP faults - left word,HP faults - right word,DSP faults - left word,DSP faults - right word,Antenna AC Q Cal Factor,Antenna AD Q Cal Factor,Antenna BC Q Cal Factor,Antenna BD Q Cal Factor,Antenna AC Phase Cal Factor,Antenna AD Phase Cal Factor,Antenna BC Phase Cal Factor,Antenna BD Phase Cal Factor,Report sensor temperature before validation,LCA Main SNR @ -50_GM1.75,LCA Main SNR @ -30_GM1.75,LCA Main SNR @ -10_GM1.75,LCA Main SNR @ 30,LCA Main SNR @ 50,GM1.75 Angle @ -50,GM1.75 Angle @ -45,GM1.75 Angle @ -40,GM1.75 Angle @ -35,GM1.75 Angle @ -30,GM1.75 Angle @ -25,GM1.75 Angle @ -20,GM1.75 Angle @ -18,GM1.75 Angle @ -16,GM1.75 Angle @ -14,GM1.75 Angle @ -12,GM1.75 Angle @ -10,GM1.75 Angle @ -8,GM1.75 Angle @ -6,GM1.75 Angle @ -4,GM1.75 Angle @ -2,GM1.75 Angle @ 0,GM1.75 Angle @ 2,GM1.75 Angle @ 4,GM1.75 Angle @ 6,GM1.75 Angle @ 8,GM1.75 Angle @ 10,GM1.75 Angle @ 12,GM1.75 Angle @ 14,GM1.75 Angle @ 16,GM1.75 Angle @ 18,GM1.75 Angle @ 20,GM1.75 Angle @ 25,GM1.75 Angle @ 30,GM1.75 Angle @ 35,GM1.75 Angle @ 40,GM1.75 Angle @ 45,GM1.75 Angle @ 50"
ST_total_test_item_prod_RDR6_GM175 = 103

# Chrysler
ST_column_names_Chrysler_prod = "Date,Time,SN,Nest,Pass/Fail,Failed Step,init SensorInterface,Ping,Measure Current,H-BSD Antenna 1 Q Cal Factor,H-BSD Antenna 2 Q Cal Factor,H-BSD Antenna 1 Phase Cal Factor,H-BSD Antenna 2 Phase Cal Factor,H-BSD Angle Cal Factor,H-BSD Antenna Cal Factor,Report Tx1 Power @ -40,Report Tx2 Power @ -40,Report Tx1 Power @ -34,Report Tx2 Power @ -34,Report Tx1 Power @ -28,Report Tx2 Power @ -28,Report Tx1 Power @ -26,Report Tx2 Power @ -26,Report Tx1 Power @ -24,Report Tx2 Power @ -24,Report Tx1 Power @ -22,Report Tx2 Power @ -22,Report Tx1 Power @ -20,Report Tx2 Power @ -20,Report Tx1 Power @ -18,Report Tx2 Power @ -18,Report Tx1 Power @ -16,Report Tx2 Power @ -16,Report Tx1 Power @ -14,Report Tx2 Power @ -14,Report Tx1 Power @ -12,Report Tx2 Power @ -12,Report Tx1 Power @ -10,Report Tx2 Power @ -10,Report Tx1 Power @ -8,Report Tx2 Power @ -8,Report Tx1 Power @ -6,Report Tx2 Power @ -6,Report Tx1 Power @ -4,Report Tx2 Power @ -4,Report Tx1 Power @ 0,Report Tx2 Power @ 0,Report Tx1 Power @ 6,Report Tx2 Power @ 6,Report Tx1 Power @ 12,Report Tx2 Power @ 12,Report Tx1 Power @ 20,Report Tx2 Power @ 20,Report Tx1 Power @ 22,Report Tx2 Power @ 22,Report Tx1 Power @ 24,Report Tx2 Power @ 24,Report Tx1 Power @ 26,Report Tx2 Power @ 26,Report Tx1 Power @ 28,Report Tx2 Power @ 28,Report Tx1 Power @ 30,Report Tx2 Power @ 30,Report Tx1 Power @ 40,Report Tx2 Power @ 40,Normalized Tx2 Power @ -40,Normalized Tx2 Power @ -34,Normalized Tx2 Power @ -28,Normalized Tx2 Power @ -26,Normalized Tx2 Power @ -24,Normalized Tx2 Power @ -22,Normalized Tx2 Power @ -20,Normalized Tx2 Power @ -18,Normalized Tx2 Power @ -16,Normalized Tx2 Power @ -14,Normalized Tx2 Power @ -12,Normalized Tx2 Power @ -10,Normalized Tx2 Power @ -8,Normalized Tx2 Power @ -6,Normalized Tx2 Power @ -4,Normalized Tx2 Power @ 0,Normalized Tx2 Power @ 6,Normalized Tx2 Power @ 12,Normalized Tx2 Power @ 20,Normalized Tx2 Power @ 22,Normalized Tx2 Power @ 24,Normalized Tx2 Power @ 26,Normalized Tx2 Power @ 28,Normalized Tx2 Power @ 30,Normalized Tx2 Power @ 40,EIRP delta,Tx1 EIRP,Report Null Angle,RCTA Squint SNR @ -40_Honda,MeasData_RCTA_Squint_0_Honda,RCTA Squint Range @ 0 Honda,RCTA Squint SNR @ 0 _Honda,RCTA Squint SNR @ 10 Honda,RCTA Squint Range @ 30,RCTA Squint SNR @ 30,RCTA Squint Range @ 40,RCTA Squint SNR @ 40,RCTA Squint Range @ 50,RCTA Squint SNR @ 50,RCTA Main SNR @ -20,MeasData_RCTA_Main_0,RCTA Main SNR @ 0,RCTA Main Angle @ 20,RCTA Main Range @ 20,RCTA Main SNR @ 20,RCTA Main SNR @ 40,RCTA Main Angle @ -40_Honda,RCTA Main Angle @ -20,RCTA Squint Angle @ 10_Honda,RCTA Squint Range @ 10 Honda,RCTA Main Angle @ 10_Honda,RCTA Squint Angle @ 30,RCTA Main Angle @ 30,RCTA Main Angle @ 40,RCTA Squint Angle @ 40,RCTA Squint Angle @ 50,RCTA Main Angle @ 50,Test Time"
ST_total_test_item_prod_RDR6_Chrysler = 105






