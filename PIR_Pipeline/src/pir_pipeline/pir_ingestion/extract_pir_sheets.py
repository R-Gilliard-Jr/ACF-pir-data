def extract_pir_sheets(workbooks):
    import pandas as pd
    import sqlite3, os, time
    from pir_pipeline import config as conf

    config = conf.config

    # Establish db connection
    pir_logs_db = os.path.join(config["dbpath"], "pir_logs.db")
    try:
        log_conn = sqlite3.connect(pir_logs_db)
        log_cursor = log_conn.cursor()
    except:
        raise(f"Could not open database: {pir_logs_db}")

    run = time.strftime("%Y-%m-%d %H:%M:%S")
    wb_list = []
    for workbook in workbooks:
        try:
            wb_list.append(pd.ExcelFile(workbook))
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            message = f"Successfully opened workbook: {workbook}"
            log_query = f"""
                INSERT INTO pir_ingestion_logs (run, timestamp, message) VALUES ('{run}','{timestamp}','{message}')
            """
            log_cursor.execute(log_query)
        except Exception as e:
            raise(e)
        
    log_conn.commit()
    log_conn.close()
    return(wb_list)