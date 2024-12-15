from nicegui import ui
import requests

backend_host = 'http://localhost:1234'

base = False


def main():
    def update_users_table():
        response = requests.get(f"{backend_host}/get_users")
        users_dict = response.json()
        grid_test.rows = [{'id': str(k), 'name': str(v)} for k, v in users_dict.items()]
        grid_test.update()

    # def add_user(a1, a2):
    #     json_gen = {a1: a2}
    #     response = requests.post(f"{backend_host}/add_user/", json=json_gen)
    #     print()

    rows = []
    columns = [{'name': 'id', 'label': 'id', 'field': 'id'}, {'name': 'name', 'label': 'name', 'field': 'name'}]
    grid_test = ui.table(rows=rows, columns=columns)
    ui.button('Get list of users', on_click=update_users_table())

    a1 = ui.input(label='Name', placeholder='...some name...',
                  validation={'Wrong input': lambda value: 1 < len(value) < 20})

    a2 = ui.input(label='Name', placeholder='...some surname...',
                  validation={'Wrong input': lambda value: 1 < len(value) < 20})



    ui.button('Add user', on_click=lambda: requests.post(f'{backend_host}/add_user/', timeout=1, json={a1.value:a2.value}))

    ui.run()


if __name__ in {"__main__", "__mp_main__"}:
    main()
