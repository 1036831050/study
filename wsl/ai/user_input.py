import requests

api_key = "Bearer sk-2dZObLpOgdlb5AE9GJXwnEUd5ocLGY90nDnhp2TQmErRDW8m"


# Get the user's prompt
def get_prompt_from_user():
    # other thing
    # ...
    return "具体是哪个模型呢"


def main():
    # Before starting a session, you need to create a thread first
    url = "https://api.deepbricks.ai/api/v1/threads"
    resp = requests.post(url, headers={"Authorization": "Bearer sk-2dZObLpOgdlb5AE9GJXwnEUd5ocLGY90nDnhp2TQmErRDW8m"})
    thread = resp.json()
    if resp.status_code != 200:
        print(resp.json())
        return

    # multi turn chat
    while True:
        # 1. create message
        url = f"https://api.deepbricks.ai/api/v1/threads/{thread['id']}/messages"
        body = {
            "role": "user",
            "content": get_prompt_from_user()
        }
        resp = requests.post(url, headers={"Authorization": api_key}, json=body)
        if resp.status_code != 200:
            print(resp.json())
            return

        # 2. create run
        url = f"https://api.deepbricks.ai/api/v1/threads/{thread['id']}/runs"
        body = {
            "model": "gpt-4o"
        }
        resp = requests.post(url, headers={"Authorization": api_key}, json=body)
        run = resp.json()
        if resp.status_code != 200:
            print(resp.json())
            return

        # 3. get assistant answer
        url = f"https://api.deepbricks.ai/api/v1/threads/{thread['id']}/messages?run_id={run['id']}"
        resp = requests.get(url, headers={"Authorization": api_key})
        print(resp.json())


if __name__ == '__main__':
    main()
