# Ansible examples for https://williamsbdev.com/

You can run all the examples by having Docker installed (I created all examples
with Docker for Mac version 17.12.0-ce). Otherwise, you can deconstruct what
commands are needed from the following code examples and Dockerfiles.

### Build base image for all examples using Ansible 2.2.0.0

    docker build -t ansible-base -f ansible-base/Dockerfile .

### Example 1

Make sure to build [base image] (used for all examples).

#### Build Docker image

    docker build -t example-01 -f examples/01/Dockerfile .

#### Run

    docker run example-01

### Example 2

Make sure to build [base image] (used for all examples).

#### Build Docker image

    docker build -t example-02 -f examples/02/Dockerfile .

#### Run

    docker run example-02

### Example 3

Make sure to build [base image] (used for all examples).

#### Build Docker image

    docker build -t example-03 -f examples/03/Dockerfile .

#### Run

    docker run example-03

### Example 4

Make sure to build [base image] (used for all examples).

#### Build Docker image

    docker build -t example-04 -f examples/04/Dockerfile .

#### Run

    docker run example-04

### Example 5

Make sure to build [base image] (used for all examples).

#### Build Docker image

    docker build -t example-05 -f examples/05/Dockerfile .

#### Run

    docker run example-05

### Example 6

Make sure to build [base image] (used for all examples).

#### Build Docker image

    docker build -t example-06 -f examples/06/Dockerfile .

#### Run

    docker run example-06

[base image]: https://github.com/williamsbdev/ansible-examples#build-base-image-for-all-examples-using-ansible-2200
