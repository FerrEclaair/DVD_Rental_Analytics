# 🎬 DVD Rental Analytics Dashboard with AI

An interactive **DVD Rental Analytics Dashboard** built with **FastAPI, PostgreSQL, Pandas, Plotly-style interactive visualizations, and DeepSeek AI.

The application turns the classic DVD Rental database into an interactive business intelligence dashboard where users can explore revenue, rentals, customers, films, actors, inventory, and other operational metrics — while an AI assistant can answer dashboard-related questions and dynamically control the dashboard.

---

## 📌 Project Overview

This project was developed as an end-to-end **Business Intelligence + AI Analytics** application.

Instead of only displaying static charts, the dashboard allows users to interact with the data through an integrated AI assistant.

The AI assistant can understand requests such as:

> "Show me the top 10 most rented films."

or:

> "Change the dashboard theme to ocean."

and then perform the appropriate dashboard action.

### Core concept

```text
PostgreSQL DVD Rental Database
            │
            ▼
        FastAPI Backend
            │
      ┌─────┴─────┐
      ▼           ▼
 Analytics      AI Layer
      │           │
      │      ┌────┴────┐
      │      ▼         ▼
      │   DeepSeek   Local ML
      │      │         │
      └──────┴─────────┘
             │
             ▼
      Interactive Dashboard
```

---

# ✨ Key Features

## 📊 1. Interactive Analytics Dashboard

The dashboard provides visual analytics for important DVD Rental business metrics, including:

- Revenue
- Rentals
- Customers
- Films
- Actors
- Inventory
- Store performance
- Genre performance
- Payment activity

Users can explore the data through interactive charts and dashboard sections.

---

## 🤖 2. AI Floating Chat

The project includes an integrated AI assistant accessible through a floating chat interface.

The assistant is powered by **DeepSeek** and is specifically designed to work with the DVD Rental Dashboard.

It can:

- Answer questions about dashboard data
- Explain revenue trends
- Find top-performing films
- Find high-spending customers
- Analyze rental activity
- Filter dashboard sections
- Change dashboard themes
- Render charts based on natural-language requests
- Highlight specific KPIs
- Scroll to relevant dashboard sections

Example prompts:

```text
Show the top 10 most rented films.

Who are the top 5 customers by spending?

Show revenue by genre.

Which month has the highest revenue?

Change the dashboard theme to ocean.

Filter the dashboard to Action genre.
```

The assistant is intentionally scoped to the DVD Rental domain and can politely reject unrelated questions.

---

# 🧠 3. AI Function / Action System

The AI assistant does more than return text.

A user request can be translated into a dashboard action.

For example:

```text
User
 │
 │ "Show top 10 films"
 ▼
DeepSeek AI
 │
 │ action
 ▼
FastAPI
 │
 │ query database
 ▼
Dashboard Data
 │
 ▼
JavaScript Dashboard
 │
 ▼
Interactive Chart
```

Supported dashboard actions include:

```text
set_theme
scroll_to
render_chart
filter_genre
highlight_kpi
```

This creates a more natural interaction between the user and the analytics interface.

---

# 📈 4. Time-Series Forecasting

The project also includes a forecasting module in:

```text
ml_forecast.py
```

The forecasting engine uses:

**Linear Regression + Monthly Seasonal Pattern Detection**

to predict future:

- Monthly revenue
- Monthly rentals

The system can generate forecasts for up to **12 months**.

### Forecasting process

```text
Historical Data
      │
      ▼
Monthly Aggregation
      │
      ▼
Linear Regression
      │
      ▼
Trend Calculation
      │
      ▼
Seasonal Residual Analysis
      │
      ▼
Future Prediction
```

The model also calculates:

- R² score
- Number of historical data points
- Forecast horizon
- Expected percentage change
- Automatic trend insight

Example insights:

```text
📈 Upward trend
📉 Downward trend
➡️ Stable trend
```

---

# 🧪 5. Local Transformer ML

In addition to the DeepSeek AI assistant, the application supports an optional local Transformer model.

This model can perform:

- Zero-shot classification
- Text classification
- Feature extraction

Supported inference endpoint:

```text
GET  /api/ml/local-transformer/status
POST /api/ml/local-transformer/predict
```

Example request:

```json
{
  "text": "Revenue is dropping while rental demand stays strong.",
  "labels": [
    "revenue risk",
    "rental growth",
    "customer churn"
  ],
  "top_k": 3
}
```

This provides an additional local ML capability alongside the cloud-based conversational AI.

---

# 🗄️ 6. PostgreSQL Integration

The application connects directly to a PostgreSQL DVD Rental database.

SQLAlchemy is used as the database abstraction layer, while Pandas is used for analytical data processing.

Example data sources include:

```text
payment
rental
inventory
customer
film
staff
```

The backend can query operational data and convert it into JSON-safe records for the frontend.

---

# 🔎 7. Natural-Language Database Interaction

The AI system includes structured support for understanding database-related requests.

Users can ask for information using natural language instead of manually writing SQL.

For example:

```text
"Show me the highest payment."

"Find customers from a specific district."

"Show rental records."

"Which films have the highest rental rate?"
```

The backend maps natural-language terms to supported database entities and fields.

This makes the dashboard more accessible to users without requiring SQL knowledge.

---

# ✏️ 8. Database Record Management

The backend includes controlled operations for selected database tables.

Supported mutation operations include:

```text
INSERT
UPDATE
DELETE
```

The current implementation specifically defines controlled operations for:

- `payment`
- `rental`

The system validates:

- Allowed fields
- Data types
- Required fields
- Foreign-key references
- Record existence

This provides a structured way to interact with selected operational data.

---

# 🎨 9. Dashboard Themes

The dashboard supports multiple visual themes:

| Theme | Description |
|---|---|
| 🌑 Dark | Default cinema-style dark theme |
| ☀️ Light | Clean light interface |
| 🟡 Gold | Premium gold/black theme |
| 🌊 Ocean | Deep blue theme |
| 🌅 Sunset | Warm orange/pink theme |

Themes can be changed:

- Through dashboard controls
- Through the AI assistant

Example:

```text
"Change the theme to ocean."
```

The dashboard automatically re-renders charts to maintain readable axis and text colors.

---

# 💾 10. Persistent Dashboard State

The project stores selected dashboard states through:

```text
localStorage
```

and server-side JSON state files:

```text
dashboard_visual_state.json
dashboard_ai_outputs.json
```

This allows certain dashboard preferences and AI-generated outputs to persist between sessions.

---

# 🏗️ Project Architecture

```text
                     ┌──────────────────────┐
                     │ PostgreSQL Database  │
                     │    DVD Rental DB     │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │     FastAPI API      │
                     │       main.py        │
                     └───────┬───────┬──────┘
                             │       │
                ┌────────────┘       └────────────┐
                ▼                                 ▼
       ┌─────────────────┐              ┌─────────────────┐
       │ Analytics / SQL │              │    AI Layer     │
       │     Queries     │              │    DeepSeek     │
       └────────┬────────┘              └────────┬────────┘
                │                                │
                │                       ┌────────┴────────┐
                │                       ▼                 ▼
                │                Action Generation   Chat Response
                │
                ▼
       ┌─────────────────┐
       │ Forecast Module │
       │ ml_forecast.py  │
       └────────┬────────┘
                │
                └──────────────┐
                               ▼
                    ┌──────────────────────┐
                    │ Interactive Frontend │
                    │ HTML/CSS/JavaScript  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Dashboard UI      │
                    │ Charts + KPI + Chat  │
                    └──────────────────────┘
```

---

# 📂 Project Structure

```text
FINAL_PROJECT-main/
│
├── main.py
│   └── FastAPI backend
│       Database queries
│       AI chat endpoint
│       Dashboard APIs
│       Database operations
│       ML endpoints
│
├── ml_forecast.py
│   └── Revenue and rental forecasting
│
├── download_model.py
│   └── Local Transformer model utility
│
├── requirements.txt
│   └── Python dependencies
│
├── .env.example
│   └── Environment variable template
│
├── dashboard_ai_outputs.json
│   └── Persisted AI dashboard outputs
│
├── dashboard_visual_state.json
│   └── Persisted dashboard visual state
│
├── templates/
│   └── index.html
│       Main dashboard interface
│
├── static/
│   ├── css/
│   │   └── styles.css
│   │
│   └── js/
│       ├── dashboard.js
│       │   └── Charts, dashboard state,
│       │       themes and actions
│       │
│       └── chat.js
│           └── Floating AI chat interface
│
└── models/
    └── local-transformer/
        ├── config.json
        ├── model.safetensors
        ├── tokenizer.json
        └── tokenizer_config.json
```

---

# 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend REST API |
| PostgreSQL | Database |
| SQLAlchemy | Database connectivity |
| Pandas | Data analysis and transformation |
| NumPy | Numerical processing |
| Scikit-learn | Forecasting / machine learning |
| DeepSeek | Conversational AI |
| Hugging Face Transformers | Local Transformer inference |
| PyTorch | Local ML model execution |
| Jinja2 | HTML templating |
| JavaScript | Interactive dashboard logic |
| HTML5 | Frontend structure |
| CSS3 | Frontend styling |
| Plotly / interactive chart layer | Data visualization |

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd FINAL_PROJECT-main
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The main dependencies include:

```text
FastAPI
Uvicorn
SQLAlchemy
psycopg2-binary
Pandas
Jinja2
OpenAI
Pydantic
python-dotenv
Transformers
PyTorch
```

---

# 🗄️ Database Configuration

The application expects a PostgreSQL DVD Rental database.

Create a `.env` file based on:

```text
.env.example
```

Example:

```env
DATABASE_URL=postgresql+psycopg2://postgres:YOUR_PASSWORD@localhost:5432/dvd_project_database

DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_API_KEY=YOUR_DEEPSEEK_API_KEY
DEEPSEEK_MODEL=deepseek-chat
```

---

# 🔐 Environment Variables

| Variable | Purpose |
|---|---|
| `DATABASE_URL` | PostgreSQL connection URL |
| `DEEPSEEK_BASE_URL` | DeepSeek API endpoint |
| `DEEPSEEK_API_KEY` | DeepSeek API authentication |
| `DEEPSEEK_MODEL` | DeepSeek model name |
| `LOCAL_TRANSFORMER_MODEL_PATH` | Local Transformer model path |
| `LOCAL_TRANSFORMER_TASK` | Transformer task |
| `LOCAL_TRANSFORMER_DEVICE` | CPU/GPU device configuration |
| `LOCAL_TRANSFORMER_DEFAULT_LABELS` | Default classification labels |
| `LOCAL_TRANSFORMER_MAX_TEXT_CHARS` | Maximum input length |

---

# 🤖 Local Transformer Configuration

If the included local model is used, configure:

```env
LOCAL_TRANSFORMER_MODEL_PATH=./models/local-transformer
LOCAL_TRANSFORMER_TASK=zero-shot-classification
LOCAL_TRANSFORMER_DEVICE=-1
LOCAL_TRANSFORMER_DEFAULT_LABELS=revenue,rental,customer,inventory,film,actor,payment,promotion,risk
LOCAL_TRANSFORMER_MAX_TEXT_CHARS=2000
```

`-1` means CPU execution.

---

# ▶️ Running the Application

Start the FastAPI application:

```bash
python main.py
```

Or use Uvicorn directly:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open the dashboard:

```text
http://localhost:8000
```

---

# 🔌 Important API Endpoints

The application exposes several API endpoints.

### Dashboard

```text
GET /
```

Returns the main dashboard interface.

### AI Chat

```text
POST /api/chat
```

Processes natural-language dashboard requests.

### Visual State

```text
GET  /api/visual-state
POST /api/visual-state
```

Stores and retrieves dashboard visual preferences.

### AI Outputs

```text
GET  /api/ai-outputs
POST /api/ai-outputs
```

Stores and retrieves generated AI dashboard outputs.

### Forecast

The forecasting functionality is exposed through the FastAPI backend and uses `ml_forecast.py`.

### Local Transformer

```text
GET  /api/ml/local-transformer/status
POST /api/ml/local-transformer/predict
```

---

# 📊 Forecasting Methodology

The forecasting module follows these steps:

### Step 1 — Aggregate Historical Data

Revenue or rental activity is grouped by month.

```text
2025-01
2025-02
2025-03
...
```

### Step 2 — Create Time Index

Each month receives a sequential time index:

```text
t = 0, 1, 2, 3, ...
```

### Step 3 — Train Linear Regression

The trend is modeled using:

```text
X = time index
Y = monthly metric
```

### Step 4 — Calculate Seasonal Residuals

The difference between actual values and trend predictions is used to estimate monthly seasonal effects.

### Step 5 — Generate Forecast

The final prediction combines:

```text
Trend
+
Seasonal Pattern
=
Forecast
```

The prediction is constrained to non-negative values.

---

# 💬 AI Assistant Examples

### Analytics

```text
Show the top 10 films by rental count.
```

### Customer Analysis

```text
Who are the top 5 customers by spending?
```

### Revenue Analysis

```text
Which month generated the highest revenue?
```

### Genre Analysis

```text
Show me revenue by genre.
```

### Dashboard Control

```text
Change the theme to ocean.
```

### Filtering

```text
Show only Action movies.
```

### Navigation

```text
Take me to the revenue section.
```

---

# 🎯 Project Objectives

The project was designed to demonstrate the integration of:

```text
Business Intelligence
        +
Data Analytics
        +
Data Visualization
        +
Time-Series Forecasting
        +
Generative AI
        +
Local Machine Learning
        +
Web Application Development
```

The main objectives are to:

1. Transform relational DVD Rental data into useful business insights.
2. Build an interactive analytics dashboard.
3. Allow users to query data using natural language.
4. Integrate AI-driven dashboard interactions.
5. Forecast future revenue and rental activity.
6. Demonstrate local Transformer inference.
7. Provide a user-friendly interface for non-technical users.

---

# 💼 Business Use Cases

The dashboard can support business questions such as:

### Revenue Management

- Which months generate the most revenue?
- Which stores perform best?
- Is revenue increasing or decreasing?

### Customer Analytics

- Who are the highest-spending customers?
- Which customers are most active?

### Film Analytics

- Which films are rented most frequently?
- Which genres generate the highest revenue?
- Which films have strong rental performance?

### Inventory Management

- Which films have high rental demand?
- Which inventory items may require additional copies?

### Management Decision Support

The dashboard provides a single interface for exploring operational data and receiving AI-assisted insights.

---

# ⚠️ Security Notes

**Never commit real credentials to GitHub.**

Before publishing this project:

- Remove any real `DEEPSEEK_API_KEY`.
- Remove real database passwords.
- Use `.env` for local secrets.
- Keep `.env` in `.gitignore`.
- Rotate any API key that has previously been exposed.

Example:

```env
DEEPSEEK_API_KEY=your-key-here
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/database
```

The included `.env.example` should contain placeholders rather than real credentials.

---

# 🔮 Future Improvements

Potential improvements include:

- [ ] Add authentication and role-based access.
- [ ] Add automated data-refresh scheduling.
- [ ] Add more advanced forecasting models.
- [ ] Add model evaluation dashboards.
- [ ] Add anomaly detection.
- [ ] Add customer churn prediction.
- [ ] Add recommendation systems.
- [ ] Add downloadable PDF/Excel reports.
- [ ] Add Docker deployment.
- [ ] Add automated testing and CI/CD.
- [ ] Add database migration management.
- [ ] Add production logging and monitoring.
- [ ] Replace JSON state storage with a persistent database.

---

# 👨‍💻 Project Role

**Role:** Data Analytics, Machine Learning & AI Integration

Main contributions:

- Developed the interactive analytics dashboard.
- Integrated PostgreSQL database analytics.
- Developed revenue and rental forecasting.
- Integrated the DeepSeek AI assistant.
- Implemented AI-driven dashboard actions.
- Implemented local Transformer inference.
- Developed interactive chart rendering.
- Implemented dashboard theme management.
- Designed natural-language interaction for dashboard analytics.
- Integrated database querying and controlled data operations.
