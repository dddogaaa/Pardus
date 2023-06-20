from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess
from datetime import datetime
from django.conf import settings as Settings

def get_date_now():
    """Return time with speacial format for logging"""
    return datetime.today().strftime('%Y-%m-%d-%H-%M-%S')


def run_command(command):
    creationTime = get_date_now()
    
    log_dir = 'logs'

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f'{creationTime}_{command.replace(" ", "_")}.log')

    process = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    with open(log_file, 'w') as file:
        file.write(process.stdout)
        file.write(process.stderr)

    status = process.returncode

    return status, log_file

def execute_command(request):
    if request.method == 'POST':
        command = request.POST.get('command')
        # name eklenicek
        status, log_file = run_command(command)
        log_content = ""

        if os.path.isfile(log_file):
            with open(log_file, 'r') as file:
                log_content = file.read()

        return render(request, 'result.html', {'command': command, 'log_file': log_file, 'log_content': log_content, 'status': status})

    return render(request, 'index.html')

def serve_log_file(request, log_file_name):
    try:
        with open(log_file_name, 'r') as file:
            file_content = file.read()
            
            # If you want the file downloadable:
            # response = HttpResponse(file_content, content_type='text/plain')
            # response['Content-Disposition'] = f'attachment; filename={log_file_name}'
            # return response
            
            return HttpResponse(file_content, content_type='text/plain')

    except FileNotFoundError:
        return HttpResponse(f'Log file {log_file_name} not found.', status=404)