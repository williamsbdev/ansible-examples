FROM ansible-base
COPY example-02.yml /app/
CMD ansible-playbook example-02.yml -i hosts -e 'variable_two=set-from-commandline'
