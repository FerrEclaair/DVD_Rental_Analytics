"""
Simple Time Series Forecasting for DVD Rental Dashboard.
Pakai Linear Regression + Seasonal Pattern Detection.
"""

import pandas as pd
import numpy as np
from sqlalchemy import text
from sklearn.linear_model import LinearRegression
from dateutil.relativedelta import relativedelta


def get_monthly_revenue(engine, store_id=None):
    """Ambil data revenue bulanan dari database."""
    if store_id:
        where_clause = f"""
            WHERE staff_id IN (
                SELECT staff_id FROM staff WHERE store_id = {int(store_id)}
            )
        """
    else:
        where_clause = ""
    
    query = f"""
        SELECT
            TO_CHAR(payment_date, 'YYYY-MM') AS month,
            SUM(amount) AS total
        FROM payment
        {where_clause}
        GROUP BY TO_CHAR(payment_date, 'YYYY-MM')
        ORDER BY month
    """

    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df


def get_monthly_rentals(engine, store_id=None):
    """Ambil data jumlah rental bulanan dari database."""
    if store_id:
        where_clause = f"""
            WHERE staff_id IN (
                SELECT staff_id FROM staff WHERE store_id = {int(store_id)}
            )
        """
    else:
        where_clause = ""
    
    query = f"""
        SELECT
            TO_CHAR(rental_date, 'YYYY-MM') AS month,
            COUNT(*) AS total
        FROM rental
        {where_clause}
        GROUP BY TO_CHAR(rental_date, 'YYYY-MM')
        ORDER BY month
    """

    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df


def forecast_time_series(df, horizon=4):
    """Prediksi masa depan dengan Linear Regression + monthly seasonality."""
    if df.empty or len(df) < 3:
        return {
            "error": "Data terlalu sedikit untuk forecast (minimal 3 bulan).",
            "history": [],
            "forecast": [],
        }

    df = df.copy()
    df["date"] = pd.to_datetime(df["month"], format="%Y-%m")
    df = df.sort_values("date").reset_index(drop=True)
    df["total"] = pd.to_numeric(df["total"], errors="coerce").fillna(0.0)

    df["t"] = np.arange(len(df))
    df["month_num"] = df["date"].dt.month

    # Model trend dengan Linear Regression
    X_trend = df[["t"]].values
    y = df["total"].values
    trend_model = LinearRegression()
    trend_model.fit(X_trend, y)
    trend_pred = trend_model.predict(X_trend)

    # Pola musiman per bulan
    residuals = y - trend_pred
    seasonal_map = (
        pd.DataFrame({"month_num": df["month_num"], "resid": residuals})
        .groupby("month_num")["resid"]
        .mean()
        .to_dict()
    )

    # Generate forecast
    last_date = df["date"].iloc[-1]
    last_t = df["t"].iloc[-1]

    forecast_rows = []
    for i in range(1, horizon + 1):
        future_date = last_date + relativedelta(months=i)
        future_t = last_t + i
        future_month_num = future_date.month

        trend_value = trend_model.predict([[future_t]])[0]
        seasonal_value = seasonal_map.get(future_month_num, 0.0)
        prediction = max(0, trend_value + seasonal_value)

        forecast_rows.append({
            "month": future_date.strftime("%Y-%m"),
            "predicted": round(float(prediction), 2),
        })

    r2_score = trend_model.score(X_trend, y)

    history_rows = [
        {"month": row["month"], "actual": round(float(row["total"]), 2)}
        for _, row in df.iterrows()
    ]

    if len(forecast_rows) >= 1 and len(history_rows) >= 1:
        last_actual = history_rows[-1]["actual"]
        avg_forecast = np.mean([f["predicted"] for f in forecast_rows])
        change_pct = (
            ((avg_forecast - last_actual) / last_actual * 100) if last_actual else 0
        )
    else:
        change_pct = 0

    if change_pct > 5:
        insight = f"📈 Tren naik — prediksi rata-rata {change_pct:+.1f}% dibanding bulan terakhir."
    elif change_pct < -5:
        insight = f"📉 Tren turun — prediksi rata-rata {change_pct:+.1f}% dibanding bulan terakhir."
    else:
        insight = f"➡️ Tren stabil — prediksi rata-rata {change_pct:+.1f}% dibanding bulan terakhir."

    return {
        "history": history_rows,
        "forecast": forecast_rows,
        "metrics": {
            "r2_score": round(float(r2_score), 3),
            "data_points": len(df),
            "horizon": horizon,
            "change_pct": round(float(change_pct), 2),
        },
        "insight": insight,
        "model": "Linear Regression + Seasonal Pattern",
    }


def run_forecast(engine, dataset: str, horizon: int = 4):
    """Entry point untuk forecast endpoint."""
    horizon = max(1, min(int(horizon), 12))

    dataset_map = {
        "monthly_revenue_total": lambda: get_monthly_revenue(engine, None),
        "monthly_revenue_store_1": lambda: get_monthly_revenue(engine, 1),
        "monthly_revenue_store_2": lambda: get_monthly_revenue(engine, 2),
        "monthly_rental_total": lambda: get_monthly_rentals(engine, None),
        "monthly_rental_store_1": lambda: get_monthly_rentals(engine, 1),
        "monthly_rental_store_2": lambda: get_monthly_rentals(engine, 2),
    }

    if dataset not in dataset_map:
        return {
            "error": f"Dataset '{dataset}' tidak dikenal.",
            "available": list(dataset_map.keys()),
        }

    try:
        df = dataset_map[dataset]()
    except Exception as e:
        return {"error": f"Gagal mengambil data dari database: {str(e)}"}

    result = forecast_time_series(df, horizon=horizon)
    result["dataset"] = dataset
    return result