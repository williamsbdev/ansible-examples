FROM ansible-base
COPY example-08.yml /app/
COPY examples/08/*.yml /app/
CMD ansible-playbook example-08.yml -i hosts -e 'variable_eight=set-from-commandline'
