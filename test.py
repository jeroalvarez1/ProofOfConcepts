
from services.ToolsObject import *
from services.ObjectCleaner import ObjectCleaner


print('Corre el sistema')
objectCleaner = ObjectCleaner(['./users_test_1-1.csv'])
ToolsObject.convertDFToCsv('./users_test_2-1.csv', objectCleaner.mergeRowsOfOneDataFrame(0,['PersonEmail','DNI__c'], 'ExtID'))

#objectCleaner2 = ObjectCleaner(['./users_test_1-1.csv', './users_test_1-2.csv', './users_test_1-3.csv'])
#ToolsObject.convertDFToCsv('./new_users_test_2.csv', objectCleaner2.mergeRowsOfDataFrames('DNI', 'EXTID', 'A23'))
#ToolsObject.convertDFToCsv('./new_users_test_nl_id_2.csv', ToolsObject.dropColums(ToolsObject.convertCsvToDF(['./new_users_test_2.csv'])[0], ['ID1', 'ID2', 'ID3']))

"""
objectJoiner = ObjectJoiner(
    './cases_test_1-1.csv',
    './new_users_test_2.csv',
    ['ID1', 'ID2', 'ID3'],
    'EXTID'
)
ToolsObject.convertDFToCsv('./new_cases_test_1.csv', objectJoiner.joinTwoDF('ID_ACCOUNT'))
"""
print('Cierra el sistema')