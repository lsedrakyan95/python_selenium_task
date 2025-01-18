This project contains implementations of tasks from "Python for QA" module (https://learning.griddynamics.com/#/online-course-player/3bc8adf4-422b-4205-ab0d-2c592c08f647).

"tests" directory contains 2 files:
 1. test_books_api.py - API tests for the service https://github.com/orgs/griddynamics/teams/manual_python-qa-book-service
 2. test_blog_ui.py - UI tests for https://www.griddynamics.com/blog

Steps to run the tests:
1. pip install --no-cache-dir -r requirements.txt
2. pytest tests/test_blog_ui.py
3. pytest tests/test_books_api.py
4. allure serve allure-results