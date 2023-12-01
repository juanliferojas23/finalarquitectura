import urequests

ifttt_key = 'nzyqt4tLjXsEOe4SBeRa0H70oz9SmV4TkpYWxDp0Nt7'

def send_ifttt_event(ds18b20):
    ifttt_url = 'https://maker.ifttt.com/trigger/ds18b20/with/key/nzyqt4tLjXsEOe4SBeRa0H70oz9SmV4TkpYWxDp0Nt7'.format(ds18b20, ifttt_key)
    try:
        response = urequests.post(ifttt_url,json=temp)
        print('IFTTT Event Sent:', response.text)
    except Exception as e:
        print('Failed to send IFTTT event:', str(e))

