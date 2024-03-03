def load_pir_data(wb_list):
    import pandas as pd, sqlite3, os, re, janitor
    from pir_pipeline import config as conf

    config = conf.config

    # Establish db connection
    pir_logs_db = os.path.join(config["dbpath"], "pir_logs.db")
    try:
        log_conn = sqlite3.connect(pir_logs_db)
        log_cursor = log_conn.cursor()
    except:
        raise(f"Could not open database: {pir_logs_db}")
    
    section_re = re.compile("^Section")
    for workbook in wb_list:
        for sheet in workbook.sheet_names:
            # Special logic for sections
            if re.match(section_re, sheet):
                continue
            # Reference and program can be loaded directly
            else:
                try:
                    df = pd.read_excel(workbook, sheet_name=sheet)
                    df = janitor.clean_names(df)
                    if sheet == 'Reference':
                        group_vars = ['question_number', 'question_name']
                        # Ensure that data is unique by question_number and question_name
                        try:
                            assert df.set_index(group_vars).index.is_unique
                        except:
                            df = df.drop_duplicates(group_vars)
                        finally:
                            assert df.set_index(group_vars).index.is_unique
                    print(df)
                except Exception as e:
                    raise(e)
            
import extract_pir_sheets
wb_list = extract_pir_sheets.extract_pir_sheets(["D:/repos/acf-pir-data/PIR_Pipeline/test_data/base_test_2008.xlsx", "D:/repos/acf-pir-data/PIR_Pipeline/test_data/base_test_2009.xlsx"])
load_pir_data(wb_list)
