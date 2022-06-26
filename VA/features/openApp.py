import subprocess

def launch(app):
    #launch specific app
    try:
        subprocess.call(app)
        return True
    except Exception as e:
        print(e)
        raise
        return False
