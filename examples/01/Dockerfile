FROM ansible-base
COPY example-01.yml /app/
CMD ansible-playbook example-01.yml -i hosts -e 'variable_one=set-from-commandline'
