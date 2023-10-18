from services.ObjectCleaner import ObjectCleaner
from services.ObjectJoiner import ObjectJoiner
from services.ToolsObject import ToolsObject

#objectCleaner = ObjectCleaner(['C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_1-3.csv'])
#ToolsObject.convertDFToCsv('C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_2-3.csv', objectCleaner.mergeRowsOfOneDataFrame(0,'DNI', 'ID3'))

objectCleaner2 = ObjectCleaner(['C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_2-1.csv', 'C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_2-2.csv', 'C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_2-3.csv'])
ToolsObject.convertDFToCsv('C:/Users/jeroa/Documents/ProofOfConcepts/test/new_users_test_2.csv', objectCleaner2.mergeRowsOfDataFrames('DNI', 'EXTID', 'A23'))
#ToolsObject.convertDFToCsv('C:/Users/jeroa/Documents/ProofOfConcepts/test/new_users_test_nl_id_2.csv', ToolsObject.dropColums(ToolsObject.convertCsvToDF(['C:/Users/jeroa/Documents/ProofOfConcepts/test/new_users_test_2.csv'])[0], ['ID1', 'ID2', 'ID3']))

"""
objectJoiner = ObjectJoiner(
    'C:/Users/jeroa/Documents/ProofOfConcepts/test/cases_test_1-1.csv',
    'C:/Users/jeroa/Documents/ProofOfConcepts/test/new_users_test_2.csv',
    ['ID1', 'ID2', 'ID3'],
    'EXTID'
)
ToolsObject.convertDFToCsv('C:/Users/jeroa/Documents/ProofOfConcepts/test/new_cases_test_1.csv', objectJoiner.joinTwoDF('ID_ACCOUNT'))
"""