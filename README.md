# Ansible examples for https://williamsbdev.com/

You can run all the examples by having Docker installed (I created all examples
with Docker for Mac version 17.12.0-ce). Otherwise, you can deconstruct what
commands are needed from the following code examples and Dockerfiles.

### Build base image for all examples using Ansible 2.2.0.0

    docker build -t ansible-base -f ansible-base/Dockerfile .

### Example 1

Make sure to build [base image] (used for all examples).

#### Build Docker image

    docker build -t example-one -f examples/one/Dockerfile .

#### Run

    docker run example-one

### Example 2

Make sure to build [base image] (used for all examples).

#### Build Docker image

    docker build -t example-two -f examples/two/Dockerfile .

#### Run

    docker run example-two

[base image]: https://github.com/williamsbdev/ansible-examples#build-base-image-for-all-examples-using-ansible-2200
