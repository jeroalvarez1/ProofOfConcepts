from services.ObjectCleaner import ObjectCleaner

dataFrameService = ObjectCleaner()
dataFrameService.convertCsvToDF(['C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_1-1.csv', 'C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_1-2.csv'])
dataFrameService.convertDFToCsv('C:/Users/jeroa/Documents/ProofOfConcepts/test/new_users_test_1.csv', dataFrameService.mergeRowsOfOneDataFrame(0,'DNI', 'ID1', 'EXTID', 'A23'))

dataFrameService.convertCsvToDF(['C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_2-1.csv', 'C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_2-2.csv', 'C:/Users/jeroa/Documents/ProofOfConcepts/test/users_test_2-3.csv'])
dataFrameService.convertDFToCsv('C:/Users/jeroa/Documents/ProofOfConcepts/test/new_users_test_2.csv', dataFrameService.mergeRowsOfDataFrames('DNI'))
