FROM ansible-base
COPY example-one.yml /app/
CMD ansible-playbook example-one.yml -i hosts -e 'variable_one=set-from-commandline'
