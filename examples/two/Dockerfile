FROM ansible-base
COPY example-two.yml /app/
CMD ansible-playbook example-two.yml -i hosts -e 'variable_two=set-from-commandline'
