def main():
    import pir_ingestion
    print(dir(pir_ingestion))
    pir_ingestion.extract_pir_sheets(["D:/repos/acf-pir-data/PIR_Pipeline/test_data/base_test_2008.xlsx", "D:/repos/acf-pir-data/PIR_Pipeline/test_data/base_test_2009.xlsx"])

main()