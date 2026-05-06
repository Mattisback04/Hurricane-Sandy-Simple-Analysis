# For more information on sounderpy, cehck out their documentation here --> https://kylejgillett.github.io/sounderpy/

import sounderpy as spy

okx_oct29_12z_sounding = spy.get_obs_data('OKX', '2012', '10', '29', '12')
spy.build_sounding(okx_oct29_12z_sounding)

okx_oct30_0z_sounding = spy.get_obs_data('OKX', '2012', '10', '30', '0')
spy.build_sounding(okx_oct30_0z_sounding, special_parcels=False)

okx_oct30_12z_sounding = spy.get_obs_data('OKX', '2012', '10', '30', '12')
spy.build_sounding(okx_oct30_12z_sounding)
