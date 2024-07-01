from xdataforge import XDataForge


def main():
    client = XDataForge(base_url="http://localhost:8081", token="sk_wkOQkZSniwQdtMVAAxTFp9JxOxviEFsP", )
    # setup client, fetch or create run
    client.setup("Eleanor Test Project", "23434", run_id="RUN-1719836666-0z8f2J")
    print(client.run_id)
    # fetch tasks
    tasks = client.fetch_tasks()
    print(tasks)
    # for each task, fetch datapoints and process
    task = tasks[0]
    for datapoint in task.fetch_next_datapoint():
        print(datapoint)
        # process
        task.commit_result("test")

if __name__ == "__main__":
    main()
