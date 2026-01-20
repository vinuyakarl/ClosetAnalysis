# ClosetAnalysis API
A FastAPI application for tracking wardrobe usage and cost-per-wear analytics.

## Project Structure
This project uses a `src` layout to keep import clean.
- **Code**: `src/app/`
- **Database Config**: `src/app/database/`
- **Models**: `src/app/models/`
- **Migrations**: `alembic/` 

### **1. Local Development**
#### **Prequisites**:
- Python 3.13+
- Docker (Used only to host the Postgres database)

#### **Setup**:
1. **Create and Activate Virtual Environment**
```
python3 -m venv venv 
source venv/bin/activate
```
2. **Install dependencies**

```
pip install -r requirements.txt
pip install python-dotenv
```
3. **Configure Environment** Create a `.env` file in the project root:
```
POSTGRES_USER=
POSTRES_PASSWORD=
POSTGRES_DB=
POSTGRES_PORT=
POSTGRES_SERVER=
```
4. **Start the Database Only** Instead of running the whole app in Docker, we just spin up the database so our local Python can talk to it.
```
docker-compose-up -d db
```
5. **Run Migrations** Apply the database schema (tables) to the running Postgres instance.
```
alembic upgrade head
```
6. **Start the Server** Run the API locally. Note the `--app-dir` flag, which is required because of the `src` folder structure.
```
uvicorn app.main:app --reload --app-dir src
```
- **API URL:** http://localhost:8000
- **Docs:** http://localhost:8000/docs

### **2. Docker Development**
Use this method to verify the app works in a production-like environment.

#### **Setup**:
1. **Build and Start Everything** This spins up both the API container and the DB container.
```
docker-compose up --build
```
2. **Run Migrations (Inside Docker)** Since the app is running inside a container, we must execute the migration command inside that container.
```
docker-compose exec api python -m alembic upgrade head
```
3. **Access the API**
- **API URL:** http://localhost:8080 (Note: Port 8080 is defined in docker-composer)
- **Docs:** http://localhost:8080/docs

### **3. Database Management CheatSheet**
**Creating a New Migration:**
When you modify a model in `src/app/models/`, run this locally to generate the script:
```
alembic revision --autogenerate -m "Describe your change here"
```
**Inspecting the Database (CLI)**
```
docker exec -it <container name> psql -U <user> -d <db name>
```
**Resetting the Database**
If things break, and you want to start fresh:
```
docker-compose down -v
docker-compose up -d db
alembic upgrade head
```
