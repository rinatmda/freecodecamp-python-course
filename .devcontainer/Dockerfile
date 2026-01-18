FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Устанавливаем Python, pip и venv
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y python3 python3-pip python3.12-venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
