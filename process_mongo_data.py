# Import library
from pymongo import MongoClient
import numpy as np

# Process data in MongoDB for plotting
def process():
    # Initialization
    test_date = list()
    pass_fail = list()
    test_duration = list()
    antenna1_tx_power = list()
    antenna2_tx_power = list()

    # Create connection
    Client = MongoClient("mongodb://localhost:27017/")

    # Database
    db = Client.Veoneer_Data_Project

    # Collection
    col = db.RDR6_TxCal_Prod

    # Point the cursor
    x = col.find()

    for item in x:
        index_list = list(item.keys())
    index_list.remove('_id')

    # Point the cursor
    x = col.find()

    # Collect all the needed data info
    for item in list(x):
        for index in index_list:
            test_date.append(item[index]['TestDate'])
            pass_fail.append(item[index]['Pass/Fail'])
            test_duration.append(item[index]['Test Time'])
            antenna1_tx_power.append(item[index]['Antenna1 GetTxPower'])
            antenna2_tx_power.append(item[index]['Antenna2 GetTxPower'])

    # calculate the average test time
    avg_test_time = np.average(test_duration)

    # calculate the passing rate
    pass_rate = pass_fail.count('PASS') / (pass_fail.count('FAIL') + pass_fail.count('PASS'))

    # Keep unique date values 
    uni_date = list()
    for date in test_date:
        if date not in uni_date:
            uni_date.append(date)

    # return results
    return avg_test_time, pass_rate, uni_date, antenna1_tx_power, antenna2_tx_power
