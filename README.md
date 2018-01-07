# Ansible examples for https://williamsbdev.com/posts/ansible-variable-precedence/

You can run all the examples by having Docker installed (I created all examples
with Docker for Mac version 17.12.0-ce). Otherwise, you can deconstruct what
commands are needed from the following code examples and Dockerfiles.

### Build base image for all examples using Ansible 2.2.0.0

    docker build -t ansible-base -f ansible-base/Dockerfile .

### Example 1

#### Build Docker image

    docker build -t example-one -f examples/one/Dockerfile .

#### Run

    docker run example-one
