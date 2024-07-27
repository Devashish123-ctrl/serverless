import json
import smtplib

def send_email(event, context):
    try:
        # Extract data from the request body
        body = json.loads(event['body'])
        receiver_email = body.get('receiver_email')
        subject = body.get('subject')
        body_text = body.get('body_text')

        # Validate input data
        if not all([receiver_email, subject, body_text]):
            return {
                'statusCode': 400,  # Bad Request
                'body': json.dumps({'error': 'Missing required fields'})
            }
        server = smtplib.SMTP('smtp.gmail.com','587')
        server.starttls()
        server.login('dummyu487@gmail.com','djangopython')
        server.sendmail('dummyu487@gmail.com',receiver_email,body_text)
        

    except Exception as e:  # Catch generic exceptions
        return {
            'statusCode': 500,  # Internal Server Error
            'body': json.dumps({'error': f'An error occurred: {str(e)}'})
        }

    # Success response (replace with specific success message if needed)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Email sent successfully!'})
    }
