import investpy
import date


def get_xfl():
    return investpy.get_etf_historical_data(etf='Financial Select Sector SPDR', country='United States',
                                            from_date=date.ten_years_ago_str(),
                                            to_date=date.today_str())


def get_spx():
    return investpy.get_index_historical_data(index='S&P 500', country='United States',
                                          from_date=date.ten_years_ago_str(),
                                          to_date=date.today_str())

                                    
def get_copper():
    return investpy.get_commodity_historical_data(commodity='Copper',
                                                  from_date=date.ten_years_ago_str(), 
                                                  to_date=date.today_str())


def get_gold():
    return investpy.get_commodity_historical_data(commodity='Gold',
                                                  from_date=date.ten_years_ago_str(), 
                                                  to_date=date.today_str())


def get_us10yt():
    return investpy.get_bond_historical_data(bond='U.S. 10Y',
                                             from_date=date.ten_years_ago_str(),
                                             to_date=date.today_str())
