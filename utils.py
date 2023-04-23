product_names_mapping = {
    'ind_ahor_fin_ult1': 'Saving Account',
    'ind_aval_fin_ult1': 'Guarantees',
    'ind_cco_fin_ult1': 'Current Accounts',
    'ind_cder_fin_ult1': 'Derivada Account',
    'ind_cno_fin_ult1': 'Payroll Account',
    'ind_ctju_fin_ult1': 'Junior Account',
    'ind_ctma_fin_ult1': 'Más particular Account',
    'ind_ctop_fin_ult1': 'particular Account',
    'ind_ctpp_fin_ult1': 'particular Plus Account',
    'ind_deco_fin_ult1': 'Short-term deposits',
    'ind_deme_fin_ult1': 'Medium-term deposits',
    'ind_dela_fin_ult1': 'Long-term deposits',
    'ind_ecue_fin_ult1': 'e-account',
    'ind_fond_fin_ult1': 'Funds',
    'ind_hip_fin_ult1': 'Mortgage',
    'ind_plan_fin_ult1': 'Pensions',
    'ind_pres_fin_ult1': 'Loans',
    'ind_reca_fin_ult1': 'Taxes',
    'ind_tjcr_fin_ult1': 'Credit Card',
    'ind_valo_fin_ult1': 'Securities',
    'ind_viv_fin_ult1': 'Home Account',
    'ind_nomina_ult1': 'Payroll',
    'ind_nom_pens_ult1': 'Pensions',
    'ind_recibo_ult1': 'Direct Debit'
}

properties_mapping = {
    'country_of_residence': 'pais_residencia',
    'gender': 'sexo',
    'age': 'age',
    'seniority_level': 'antiguedad',    
    'relation_type': 'tiprel_1mes',
    'province_name': 'nomprov',
    'activity_level': 'ind_actividad_cliente',
    'annual_income': 'renta',
    'segment': 'segmento' 
}

allowed_values_countries = ['LV', 'BE', 'BG', 'BA', 'BM', 'BO', 'JP', 'JM', 'BR', 'BY', 'BZ', 'RU', 'RS', 'RO', 'GW', 'GT', 'GR', 'GQ', 'GE', 'GB', 'GA', 'GN', 'GM', 'GI', 'GH', 'OM', 'HR', 'HU', 'HK', 'HN', 'AD', 'PR', 'PT', 'PY', 'PA', 'PE', 'PK', 'PH', 'PL', 'EE', 'EG', 'ZA', 'EC', 'AL', 'VN', 'ET', 'ZW', 'ES', 'MD', 'UY', 'MM', 'ML', 'US', 'MT', 'MR', 'UA', 'MX', 'IL', 'FR', 'MA', 'FI', 'NI', 'NL', 'NO', 'NG', 'NZ', 'CI', 'CH', 'CO', 'CN', 'CM', 'CL', 'CA', 'CG', 'CF', 'CD', 'CZ', 'CR', 'CU', 'KE', 'KH', 'SV', 'SK', 'KR', 'KW', 'SN', 'SL', 'KZ', 'SA', 'SG', 'SE', 'DO', 'DJ', 'DK', 'DE', 'DZ', 'MK', -99, 'LB', 'TW', 'TR', 'TN', 'LT', 'LU', 'TH', 'TG', 'LY', 'AE', 'VE', 'IS', 'IT', 'AO', 'AR', 'AU', 'AT', 'IN', 'IE', 'QA', 'MZ']
allowed_values_gender = ['V', 'H']
allowed_values_relation_type = ['I', 'A', 'P', 'R', 'N']
allowed_values_activity_level = ['0', '1']
allowed_values_segment = ['01 - TOP', '02 - PARTICULARES', '03 - UNIVERSITARIO']