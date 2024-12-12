def make_car(manufacture, model, **kargs):
    kargs['manufacture'] = manufacture
    kargs['model'] = model
    return kargs

print(make_car('subaru', 'outback', color='blue', tow_package='True'))