from city_function import format_location

def test_city_country():
    assert "Hue, Vietnam" == format_location('hue', 'vietnam') 

def test_city_country_population():
    assert "Santiago, Chile - 5000000" == format_location('santiago', 'chile', 5000000)