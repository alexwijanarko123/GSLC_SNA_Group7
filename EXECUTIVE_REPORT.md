# Executive Report

## Project Overview
This workspace is a Docker-based static dashboard project for Server and Network Administration. The app builds a React/Vite frontend into an Nginx container, then uses GoAccess and a lightweight Python middleware to turn web access logs into operational insights.

## Pipeline Summary
- `app` container serves the frontend through Nginx.
- Nginx writes access logs to the shared `nginx_logs/` volume.
- `goaccess` reads `nginx_logs/access.log` and continuously regenerates `nginx_logs/report.json`.
- `src/scenario_filter.py` watches `report.json` and writes `ai_catch.json` when anomaly thresholds are met.

## Current State
- The stack is containerized with Docker Compose.
- Log analysis is wired to the same shared volume as the web server logs.
- Generated output and runtime artifacts are kept out of version control through `.gitignore`.

## Key Files
- `compose.yaml`: container orchestration for app, GoAccess, and middleware.
- `Dockerfile`: multi-stage build for the frontend and Nginx runtime image.
- `nginx/nginx.conf` and `nginx/default.conf`: Nginx logging and serving configuration.
- `goaccess.conf`: GoAccess log parsing rules.
- `src/scenario_filter.py`: anomaly detection middleware.

## Notes for the Team
- The `goaccess` service must stay aligned with the actual Nginx log format.
- `ai_catch.json`, `nginx_logs/`, `dist/`, `.vite/`, and `node_modules/` are generated or runtime-only artifacts.
- The middleware is intentionally separated so it can evolve independently from the frontend container.