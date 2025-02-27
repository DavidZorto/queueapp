# Django Celery Redis OpenAI API Project

🚀 **Asynchronous Task Processing with Celery, Redis, and OpenAI API**

---

## 📌 Project Overview

This project is a comprehensive demonstration of how to integrate asynchronous task processing into your Django application. It leverages Celery for task queuing, Redis as the message broker, and the OpenAI API for generating responses based on submitted prompts. In addition, the project utilises Flower to monitor task execution, ensuring that you have full visibility into both pending and completed tasks. Furthermore, a simulated long-running task is provided to illustrate the handling of extended processes.

---

## 🛠 Tech Stack

- **Django**: The robust backend framework.
- **Django REST Framework**: A powerful toolkit to build RESTful APIs.
- **Celery**: A distributed task queue for executing tasks asynchronously.
- **Redis**: An in-memory data structure store used as a message broker.
- **OpenAI API**: Utilised for state-of-the-art text generation.
- **Flower**: A web-based tool for monitoring Celery workers.
- **Docker**: Optional, for containerising and managing the Redis service.

---

## 🚀 Features

This monolithic project is designed with a rich feature set to address various asynchronous processing scenarios:

- **Prompt Submission**: Submit a prompt via the Django API, which forwards the request to the OpenAI API.
- **Task Queuing**: Celery manages the task queue, ensuring that tasks are processed in the background.
- **Non-Blocking Operations**: Background processing keeps the main application responsive.
- **Redis Messaging**: Provides a fast, reliable, and scalable messaging system for task handling.
- **Real-Time Task Monitoring**: Flower UI enables tracking of task progress and system performance.
- **Simulated Long-Running Task**: Demonstrates the capability to handle extended processes without blocking other operations.

---


