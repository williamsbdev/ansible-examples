FROM ansible-base
COPY example-09.yml /app/
CMD ansible-playbook example-09.yml -i hosts -e 'variable_nine=set-from-commandline'
