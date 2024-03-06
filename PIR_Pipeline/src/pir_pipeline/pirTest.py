def main():
    import os, shutil

    current_dir = os.path.dirname(os.path.abspath(__file__))
    config = conf.config

    test_data = os.path.join(current_dir, "..", "..", "test_data")
    files = os.listdir(test_data)
    dest = config['Raw']

    [shutil.copy(os.path.join(test_data, file), dest) for file in files]
    ingestData.main()

if __name__ == "__main__":
    import config as conf
    import ingestData
    main()
else:
    from . import config as conf
    from . import ingestData