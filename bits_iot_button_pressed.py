import requests 

def lambda_handler(event, context):
    request = requests.post(url = 'https://hooks.slack.com/services/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', json = {'text':'andon IOT Button Pressed'})
    return request.text