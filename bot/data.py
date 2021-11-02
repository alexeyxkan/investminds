import investpy


def get_xfl():
    return investpy.get_etf_historical_data(etf='Financial Select Sector SPDR', country='United States',
                                            from_date='16/10/2011',
                                            to_date='16/10/2021')


def get_spx():
    return investpy.get_index_historical_data(index='S&P 500', country='United States',
                                          from_date='16/10/2011',
                                          to_date='16/10/2021')


def get_us10yt():
    return investpy.get_bond_historical_data(bond='U.S. 10Y',
                                             from_date='16/10/2011',
                                             to_date='16/10/2021')