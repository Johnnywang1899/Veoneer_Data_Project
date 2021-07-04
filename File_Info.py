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
# Honda 1.0
RDR7_TxCal_prod_Honda_1_0_FID = "0000"
RDR7_TxCal_prod_Honda_1_0_drop_index = [2, 15, 47]
column_names_Honda_1_0_prod = "Date,Time,Bat_Ctrl State,InitCanInterface,Sensor_Comm_Init,Init_Tx_Cal,PingDut,MIS,Point 1571,Point 1572,Point 1573,Point 1574,Point 1575,Point 1576,Temperature,Make_Path,AnalogVoltMeas,GetSWVersion,SetTemperatureCompensation,SetSAtoDefault Status,SaveConfigPoints,Force_Radar_Mode,RCTA Occupied BW,Force_Radar_Mode,Select_TX_Antenna,SetCWMode,SetTemperatureCompensation,InitDAC_amp,InitDAC_sw,Power,Point 1481,Point 1666,Point 1667,Point 1668,Point 1669,SetTemperatureCompensation,Antenna1 GetTxPower,Antenna2 GetTxPower,Antenna1 GetCenterFrequency,Antenna2 GetCenterFrequency,Antenna1 GetCwLeakage,Antenna2 GetCwLeakage,SetCWMode,Temperature,Delta,Bat_Ctrl State"
total_test_item_prod_RDR7_Honda_1_0 = 46

# Honda 1.75
RDR7_TxCal_prod_Honda_175_FID = "0000"
RDR7_TxCal_prod_Honda_175_drop_index = [2, 19, 68]
column_names_Honda_175_prod = "Date,Time,Bat_Ctrl State,AnalogVoltMeas,InitCanInterface,Sensor_Comm_Init,Init_Tx_Cal,GetNbTestVersion,GetNbLibVersion,PingDut,SetSAtoDefault,MIS,Point 1571,Point 1572,Point 1573,Point 1574,Point 1575,Point 1576,Temperature,Make_Path,GetSWVersion,SetTemperatureCompensation,SaveConfigPoints,Force_Radar_Mode,SetCWMode,Select_TX_Antenna,Tx1 BSD,Tx1 RCTA,Tx2 BSD,Tx2 RCTA,Point 1481,Point 1482,Point 1666,Point 1667,Point 1668,Point 1669,Point 1792,Point 1883,Point 1884,Point 1885,Point 1886,Point 1887,Point 1888,FreqComp Offset0,FreqComp Offset1,FreqComp Average0,FreqComp Average1,FreqComp NumbZeroCrossing0,FreqComp NumbZeroCrossing1,FreqComp Result,ResetDSP,SetSAtoDefault,Force_Radar_Mode,RCTA Occupied BW,SetSAtoDefault,SetTemperatureCompensation,Force_Radar_Mode,SetCWMode,Antenna1 GetTxPower,Antenna2 GetTxPower,Antenna1 GetCenterFrequency,Antenna2 GetCenterFrequency,Antenna1 GetCwLeakage,Antenna2 GetCwLeakage,Temperature2,Temperature1,PrepareForPowerdown,Bat_Ctrl State"
total_test_item_prod_RDR7_Honda_175 = 68











