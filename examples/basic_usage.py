from xdataforge import XDataForge


def main():
    client = XDataForge(api_token="sk_iA9IRy2rRMLFpJJSgEld5DDv5bqx97fP")
    # setup client, fetch or create run
    client.setup("test", "plan test")
    print(client.run_id)

    # fetch tasks
    tasks = client.fetch_tasks()
    # print(tasks)
    # for each task, fetch datapoints and process
    for task in tasks:
        print('-------------', task)
        for i, datapoint in enumerate(task.fetch_next_datapoint()):
            print(datapoint.input)
            # process
            result = {f"index{j}": j for j in range(i + 1)}
            print(result)
            task.commit_result(result)


if __name__ == "__main__":
    main()
