from neuralprophet import NeuralProphet
import pandas as pd

def forecast(df):
    """
    forecasts one year (365 daily periods) of data using NeuralProphet,
    accounting for seasonality, US holidays, and Covid-19 shift

    df : pandas dataframe with columns: 'ds' and 'y', containing the date and value to forecast

    returns a pandas dataframe with the forecasted values, including historical values
    """
    print(df)
    m = NeuralProphet(changepoints=["2020-03-31"])
    m.add_country_holidays("US")
    m.fit(df)
    future = m.make_future_dataframe(df,periods=365,n_historic_predictions=True)
    forecast =  m.predict(future)
    return forecast
