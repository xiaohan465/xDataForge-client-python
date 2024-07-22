from xdataforge import XDataForge


def main():
    client = XDataForge(base_url="http://39.105.188.185:8081", api_token="sk_LuCzQrjA0KRbakKYySc6QTiEp5gTUhN2" )
    # setup client, fetch or create run
    client.setup("Advanced Generation for Arithmetic Expressions", "Regression Test",run_id="RUN-1720945462-Ryr5rT")
    print(client.run_id)
    # fetch tasks
    tasks = client.fetch_tasks()
    print(tasks)
    # for each task, fetch datapoints and process
    task = tasks[0]
    for datapoint in task.fetch_next_datapoint():
        print(datapoint)
        # process
        task.commit_result({"output":"test"})

if __name__ == "__main__":
    main()
