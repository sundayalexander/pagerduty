from pdpyras import APISession

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
api_token = 'u+d5nXN_3J3W9PW8LDZQ'
user_id = 'PGIYB7K'


def main():
    # Initialize Session conectin with pagerduty
    session = APISession(api_token)
    # Fetch Incidents list
    incidents = session.list_all('incidents')
    # Generate Column titles
    columns = ['incident_number', 'id', 'title', 'description', 'created_at', 'last_status_change_at', 'status',
               'incident_key', 'summary', 'is_mergeable', 'assigned_via', 'urgency', 'type', 'html_url']
    # Save to file
    with open('incidents.csv', 'w+') as file:
        file.write(F"{','.join(columns)}\n")

        for incident in incidents:
            file.write(F"{','.join([str(incident.get(column, '')) for column in columns])}\n")
    print('Task completed, data saved to incidents.csv')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
