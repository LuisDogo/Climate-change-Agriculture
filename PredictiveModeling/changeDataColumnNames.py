import pandas as pd
import os

def main():
    # Create the path
    directory = ('..\data')
    file = ('climate_change_agriculture_en.csv')
    path = os.path.join(directory, file)
    # Read the data
    data = pd.read_csv(path)

    # Rename the columns
    data.rename(columns={
        'Country': 'Pais',
        'Region': 'Region',
        'Year': 'Año',
        'Crop_Type': 'Tipo_Cosecha',
        'Average_Temperature_C': 'Temp_Promedio_C',
        'Total_Precipitation_mm': 'Precip_Total_mm',
        'CO2_Emissions_MT': 'Emisiones_Co2_MT',
        'Crop_Yield_MT_per_HA': 'Rendimiento_Ton_HA',
        'Extreme_Weather_Events': 'Eventos_Clima_Extremo',
        'Irrigation_Access_%': 'Acceso_Riego_%',
        'Pesticide_Use_KG_per_HA': 'Pest_kg_HA',
        'Fertilizer_Use_KG_per_HA': 'Fert_kg_HA',
        'Soil_Health_Index': 'Indice_Salud_Suelo',
        'Adaptation_Strategies': 'Estrategia_Adapt',
        'Economic_Impact_Million_USD': 'Impacto_Economico_MDD'
    }, inplace=True)

    # Save at as csv
    file = ('climate_change_agriculture_sp.csv')
    path = os.path.join(directory, file)
    data.to_csv(path, index=False)
    
if __name__ == '__main__':
    main()