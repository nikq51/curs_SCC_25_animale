FROM python:3.8-slim

WORKDIR /app

# Copiere cod sursa
COPY . .

# Instalare dependinte
RUN pip install --no-cache-dir -r quickrequirements.txt

# Expune portul 5000
EXPOSE 5000

# Ruleaza aplicatia
CMD ["python", "Vultur.py"]
