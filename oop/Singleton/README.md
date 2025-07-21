# Python Singleton Examples: Logger and DB Connection with Permissions

This repository demonstrates two practical implementations of the **Singleton pattern** in Python:

1. **Logger** — a global logging class accessible from anywhere in the application.
2. **Connect** — a singleton-style database connection class with role-based access control (RBAC).

---

## Table of Contents
- [Logger (Singleton_1)](#logger-singleton_1)
  - [Example](#logger-example)
- [Connect (db_connection)](#connect-db_connection)
  - [Example](#connect-example)
- [Summary](#summary)
- [License](#license)

---

## Logger (Singleton_1)

A simple singleton logger class that stores logs in a shared list accessible globally.

| Feature          | Description                                                  |
|------------------|--------------------------------------------------------------|
| Singleton Pattern| Implemented via overriding the `__new__` method              |
| Shared Logs      | Logs stored in class-level list                              |
| Timestamp        | Automatic timestamping with `datetime.now()`                 |


# Connect (db_connection) — Singleton with Role-Based Access Control

This example implements a singleton-style connection class in Python that restricts access based on user roles and permissions. Only users with the `admin` role are allowed to initialize and use the connection.

---

## Features

| Feature            | Description                                                   |
|--------------------|---------------------------------------------------------------|
| Singleton Pattern  | Implemented via custom `@singleton` decorator                 |
| Role Management    | Supports roles: `guest`, `editor`, `moderator`, `admin`       |
| Permissions Enum   | `READ`, `WRITE`, `DELETE`, `EDIT`, `ADMIN`                    |
| Access Control     | Enforced in `__init__` and in methods via `@require_permission` |
| Error Handling     | Raises `PermissionError` if access is denied                  |
| Decorator-Based    | Uses `@require_permission` to guard sensitive operations      |

---
