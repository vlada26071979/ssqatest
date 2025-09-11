# Python Selenium Test Automation Framework

This is a personal project where I am building a custom test automation framework using **Python**, **Selenium**, and **pytest**.  
The goal of this framework is to practice test automation concepts and to have a base structure for UI test automation projects 
as well as for backend testing.

---

## Features
- Built with **Python 3** and **Selenium WebDriver**
- Uses **pytest** as the test runner
- Page Object Model (POM) design pattern
- API test support using **Python requests** module
- Automatic screenshot capture on test failure
- Easy to integrate with **GitHub Actions** for CI/CD
- Can run tests **locally in a Docker container** or **on GitHub Actions**

---

## Installation

Clone the repository:
```bash
git clone https://github.com/vlada26071979/ssqatest.git
cd ssqatest

pip install -r requirements.txt

---

## Running all tests in a container on GitHub Actions

A GitHub Actions workflow named Selenium Tests in Container has been added to automatically run the tests inside a Docker containeron a daily basis.
The workflow file is located at:

.github/workflows/selenium_tests_ran_in_container.yml
This allows tests to run directly on GitHub Actions, ensuring that the environment is consistent and that results are visible in the GitHub Actions interface

---


## Running Tests in Docker (Locally)

This framework supports running tests locally inside a Docker container, which ensures a consistent environment across different machines.

Build the Docker image:
docker build -t selenium-tests .

Run tests inside the container:
docker run -e RUN_IN_DOCKER=true selenium-tests

This allows you to execute all Selenium and API tests in an isolated environment without installing browsers or drivers on your local machine.



