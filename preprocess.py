import requests
from datetime import date
from excel_writer import write_preprocess_testcases 
import os
import json

def get_data(i):
    json_data = {
    'userId': 'string',
    'stationId': 'string',
    'applicationDetails': {
        'application_id': 'string',
        'application_type_id': 'string',
        'application_date_time_in': '2024-12-04T09:13:44.8183971Z',
        'is_branch_manager_comment': False,
        'channel_id': 'string',
        'create_date_time': '2024-12-04T09:13:44.8183994Z',
        'appl_authorizationinfo': {
            'ncb_grade': 'string',
        },
        'systemverifies': [
            {
                'id': 'string',
                'occode': 'string',
                'appl_systemverify_watchlists': [
                    {
                        'id': 'string',
                        'watchlist_lists': [
                            {
                                'id': 'string',
                                'bkl_type': 'string',
                                'bkl_subtype': 'string',
                                'bkl_degree': 'string',
                            },
                        ],
                    },
                ],
                'appl_systemverify_relateds': [
                    {
                        'id': 'string',
                        'found_status': 'string',
                    },
                ],
                'appl_systemverify_cdds': [
                    {
                        'id': 'string',
                        'appl_systemverify_cdd_alerts': [
                            {
                                'id': 'string',
                                'cdd_seq': 0,
                                'message': 'string',
                            },
                        ],
                    },
                ],
                'appl_systemverify_frauds': [
                    {
                        'id': 'string',
                        'found_status': 'string',
                        'is_validate_person': False,
                    },
                ],
                'appl_systemverify_peps': [
                    {
                        'id': 'string',
                        'appl_systemverify_pep_lists': [
                            {
                                'id': 'string',
                            },
                        ],
                    },
                ],
                'rm_kyc': 'string',
                'rm_kyc_reason': 'string',
            },
        ],
        'appl_parties': [
            {
                'id': 'string',
                'kyc_level_id': 0,
                'relationship': 'string',
                'customer_type_code': 'string',
                'collateral_owners': [
                    {
                        'id': 'string',
                        'appl_party_id': 'string',
                    },
                ],
                'cbosdata': [
                    {
                        'id': 'string',
                        'ncb_grade': 'string',
                        'cbosdata_juristic_credit_reports': [
                            {
                                'id': 'string',
                                'ncb_grade': 'string',
                            },
                        ],
                        'party_cbosdata_listpnsegments': [
                            {
                                'party_cbosdata_listidsegments': [
                                    {
                                        'party_cbosdata_listtlsegments': [
                                            {
                                                'pay_hist1': 'string',
                                                'create_date_time': '2024-12-04T09:13:44.8184226Z',
                                            },
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                ],
                'personal_infos': [
                    {
                        'id': 'string',
                        'appl_party_id': 'string',
                        'staff_id': 'string',
                        'dob': '2024-12-04',
                        'current_job_start_date': '2024-12-04',
                        'current_job_start_year': 0,
                        'current_job_start_month': 0,
                        'monthly_income_declare': 0.0,
                        'nationality_id': 'string',
                        'job_position_id': 'string',
                        'occupation_id': 'string',
                        'occupation_group_id': 'string',
                        'monthly_income': 0.0,
                        'company_title_name_id': 'string',
                    },
                ],
                'financialinfos': {
                    'total_income': 0.0,
                    'monthly_income': 0.0,
                    'total_other_income': 0.0,
                    'residual_income': 0.0,
                    'income_freq': 'string',
                    'estimated_ifs': 0.0,
                    'ifs': 0.0,
                    'total_debt_burden': 0.0,
                    'total_guarantor_income': 0.0,
                    'appl_party_financialinfo_hrms': [
                        {
                            'dsr_desc': 'string',
                        },
                    ],
                },
                'borrowers': [
                    {
                        'id': 'string',
                        'party': {
                            'id': 'string',
                            'financialinfos': {
                                'id': 'string',
                                'total_borrower_income': 0.0,
                            },
                            'personal_infos': [
                                {
                                    'id': 'string',
                                    'monthly_income_declare': 0.0,
                                },
                            ],
                        },
                    },
                ],
                'appl_guarantees': [
                    {
                        'party_type_id': 'string',
                        'party': {
                            'personal_infos': [
                                {
                                    'company_title_name_id': 'string',
                                },
                            ],
                        },
                    },
                ],
                'appl_systemverifies': [
                    {
                        'id': 'string',
                        'system_verify_type': 'string',
                        'rm_occode': 'string',
                        'occode': 'string',
                        'kyc': 'string',
                        'kyc_reason': 'string',
                        'rm_kyc': 'string',
                        'rm_kyc_reason': 'string',
                        'appl_systemverify_watchlists': [
                            {
                                'id': 'string',
                                'watchlist_lists': [
                                    {
                                        'id': 'string',
                                        'bkl_type': 'string',
                                        'bkl_subtype': 'string',
                                        'bkl_degree': 'string',
                                    },
                                ],
                            },
                        ],
                        'appl_systemverify_cdds': [
                            {
                                'id': 'string',
                                'appl_systemverify_cdd_alerts': [
                                    {
                                        'id': 'string',
                                        'cdd_seq': 0,
                                    },
                                ],
                            },
                        ],
                        'appl_systemverify_relateds': [
                            {
                                'id': 'string',
                                'found_status': 'string',
                            },
                        ],
                        'appl_systemverify_frauds': [
                            {
                                'id': 'string',
                                'found_status': 'string',
                                'is_validate_person': False,
                            },
                        ],
                        'appl_systemverify_peps': [
                            {
                                'id': 'string',
                                'appl_systemverify_pep_lists': [
                                    {
                                        'id': 'string',
                                    },
                                ],
                            },
                        ],
                        'appl_systemverify_rmservices': [
                            {
                                'id': 'string',
                                'appl_systemverify_rmservice_products': [
                                    {
                                        'id': 'string',
                                        'appl_systemverify_rmservice_cardproducts': [
                                            {
                                                'id': 'string',
                                                'card_status': 'string',
                                            },
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                ],
            },
        ],
        'accounts': [
            {
                'account_sublimits': [
                    {
                        'installment_type': 'string',
                    },
                ],
                'account_additionalservices': [
                    {
                        'addition_service_type': 'string',
                        'addition_service_group': 'string',
                        'is_credit_line_included': False,
                        'premium_amount': 0.0,
                        'insurance_cover_amount': False,
                        'insurance_period': False,
                    },
                ],
                'account_autos': {
                    'tracking_test_code': 'string',
                    'normal_installment': 0.0,
                    'percentage_insurance_ltv': 0.0,
                    'vehicle_price': 0.0,
                    'tracking_authority_code': 'string',
                    'actual_percentage_ltv': 0.0,
                    'insurance_percentage_down': 0.0,
                    'tracking_car_code': 'string',
                    'principal_amount': 0.0,
                    'standard_subsidy_interest': 0.0,
                    'require_rate_of_return': 0.0,
                    'interest_rate': 0.0,
                    'standard_rate': 0.0,
                    'balloon_installment_amount': 0.0,
                    'no_of_installment': 0,
                    'percentage_ltv': 0.0,
                    'als_remaining_term': 0,
                },
                'appl_account_existing_loans': [
                    {
                        'installment_amount_include_vat': 0.0,
                        'good_retail': 'string',
                        'original_contract_dt': 'string',
                        'no_of_installments_unpaid': 0,
                        'product_type_desc': 'string',
                        'no_of_installments': 0,
                    },
                ],
                'account_fees': [
                    {
                        'id': 'string',
                        'collected_fee': 0.0,
                        'fee_type_id': 'string',
                    },
                ],
                'account_collaterals': [
                    {
                        'is_new_collateral': False,
                        'collateral_auto': {
                            'id': 'string',
                            'vehicle_type': 'string',
                            'registered_date': '2024-12-04',
                            'insurance_lifeinsurances': [
                                {
                                    'premium_amount': 0.0,
                                },
                            ],
                            'insurances': [
                                {
                                    'vehicle_premium_incl_vat': 0.0,
                                    'insurance_type': 'string',
                                    'insurer': 'string',
                                    'vehicle_source_of_insurance': 'string',
                                },
                            ],
                            'rb_price': 0.0,
                            'vehicle_brand': 'string',
                            'vehicle_model': 'string',
                            'vehicle_age': 0,
                            'sum_container': 0.0,
                            'sum_modification_kit': 0.0,
                            'auto_accessories': [
                                {
                                    'amount': 0.0,
                                },
                            ],
                            'engine_type': 'string',
                        },
                        'collateral_real_estate': {
                            'id': 'string',
                            'province': 'string',
                            'land_appraisal_value': 0.0,
                            'fire_insurance_amount': 0.0,
                            'is_subordinated': False,
                            'subordinated_detail': 'string',
                            'is_located_in_city': False,
                            'existing_fire_insurance_amount': 0.0,
                            'project_code': 'string',
                            'zip_code': 'string',
                            'is_free_debtburden': False,
                            'collateral_type': 'string',
                            'number_of_unit': 0,
                        },
                        'collateral_security': {
                            'id': 'string',
                            'collateral_type': 'string',
                            'appraisal_value': 0,
                        },
                        'id': 'string',
                        'npanpl_code': 'string',
                        'legal_transaction_type_code': 'string',
                        'number_total_housing_debt': 0,
                        'appl_collateral_guarantee_id': 'string',
                        'appl_collateral_cash_id': 'string',
                        'legal_transaction_amount': 0.0,
                    },
                ],
                'id': 'string',
                'developer_code': 'string',
                'npanpl_code': 'string',
                'product_group_id': 'string',
                'product_program': 'string',
                'inquiry_no_period_unpaid': 0,
                'pis_credit_limit': 0.0,
                'investment_percent': 0.0,
                'letter_amount': 0.0,
                'approved_amount': 0.0,
                'partner_code': 'string',
                'pot_credit_limit': 0.0,
                'master_account_flag': 'string',
                'product_type_id': 'string',
                'project_code': 'string',
                'sub_product_type_id': 'string',
                'tenor_month': 0,
                'tenor_year': 0,
                'campaign_id': 'string',
                'package_loan_code': 'string',
                'broker_code': 'string',
                'balance_credit_line_amount': 0.0,
                'old_credit_line_amount': 0.0,
                'inquiry_amt_unpaid': 0.0,
                'account_installment_monthly_amount': 0.0,
                'loan_purpose_code': 'string',
                'mf_project_colour': 'string',
                'sub_loan_type': 'string',
                'credit_line_type': 'string',
                'inquiry_outstanding_amount': 0.0,
                'payment_method': 'string',
                'account_objectives': [
                    {
                        'id': 'string',
                        'objective_id': 'string',
                    },
                ],
                'payment_items': [
                    {
                        'id': 'string',
                        'payment_method': 'string',
                    },
                ],
                'existing_loan_fees': [
                    {
                        'id': 'string',
                        'fee_amount': 0.0,
                    },
                ],
                'appl_dealer': {
                    'dealer_group': 'string',
                },
                'account_partialinstallment_details': [
                    {
                        'premium_requested_amt': 0.0,
                    },
                ],
                'appl_account_vat_infos': [
                    {
                        'description': 'string',
                        'amount_include_vat': 0.0,
                    },
                ],
                'requested_amount': 0.0,
            },
        ],
        'primary_borrower': {
            'borrower': {
                'id': 'string',
                'party_type_id': 'string',
                'party': {
                    'id': 'string',
                    'minor2_id': 'string',
                    'income_type': 'string',
                    'kyc_level_id': 0,
                    'kyc_reason_id': 0,
                    'rm_kyc_level_id': 0,
                    'rm_kyc_reason_id': 0,
                    'customer_type_code': 'string',
                    'personal_infos': [
                        {
                            'customer_type_group_id': 'string',
                            'dob': '2024-12-04',
                            'current_job_start_date': '2024-12-04',
                            'current_job_start_year': 0,
                            'id': 'string',
                            'source_of_income': 'string',
                            'occupation_id': 'string',
                            'nationality_id': 'string',
                            'occupation_group_id': 'string',
                            'monthly_income_declare': 0.0,
                            'monthly_income': 0.0,
                            'company_isic': 'string',
                            'income_type': 'string',
                        },
                    ],
                    'cbosdata': [
                        {
                            'id': 'string',
                            'cnt_all_tl_delq_mr00336m': False,
                            'cnt_all_tl_delq_ody36m': False,
                            'ncb_grade': 'string',
                            'cbosdata_juristic_credit_reports': [
                                {
                                    'id': 'string',
                                    'ncb_grade': 'string',
                                },
                            ],
                            'is_good_payment_in_curr_month': False,
                        },
                    ],
                    'financialinfos': {
                        'id': 'string',
                        'total_income': 0.0,
                        'total_borrower_income': 0.0,
                        'total_fixed_income': 0.0,
                        'monthly_income': 0.0,
                        'residual_income': 0.0,
                        'pq_campaign_credit_limit': 0.0,
                        'inquiry_income_source': 'string',
                        'appl_party_financialinfo_hrms': [
                            {
                                'level': 'string',
                                'dsr_desc': 'string',
                            },
                        ],
                    },
                    'oc_code': 'string',
                    'appl_systemverifies': [
                        {
                            'kyc': 'string',
                            'kyc_reason': 'string',
                            'occode': 'string',
                            'appl_systemverify_peps': [
                                {
                                    'id': 'string',
                                    'appl_systemverify_pep_lists': [
                                        {
                                            'id': 'string',
                                        },
                                    ],
                                },
                            ],
                        },
                    ],
                    'accountlistncbs': [
                        {
                            'id': 'string',
                            'ncb_account_type': 'string',
                            'create_date_time': '2024-12-04T09:13:44.8185267Z',
                            'ncb_member_short_name': 'string',
                            'ncb_date_of_last_debt_restructure': 'string',
                            'ncb_amount_owned': 0.0,
                            'ncb_account_status': 'string',
                        },
                    ],
                    'appl_guarantees': [
                        {
                            'party': {
                                'id': 'string',
                                'oc_code': 'string',
                                'personal_infos': [
                                    {
                                        'current_job_start_date': 'string',
                                    },
                                ],
                            },
                        },
                    ],
                    'business_infos': [
                        {
                            'business_main_type_id': 'string',
                        },
                    ],
                },
            },
        },
        'borrowers': [
            {
                'id': 'string',
                'party_type_id': 'string',
                'party': {
                    'id': 'string',
                    'income_type': 'string',
                    'kyc_level_id': 0,
                    'kyc_reason_id': 0,
                    'customer_type_code': 'string',
                    'addresses': [
                        {
                            'address_owner': 'string',
                        },
                    ],
                    'personal_infos': [
                        {
                            'customer_type_group_id': 'string',
                            'dob': '2024-12-04',
                            'id': 'string',
                            'source_of_income': 'string',
                            'occupation_id': 'string',
                            'nationality_id': 'string',
                            'occupation_group_id': 'string',
                            'monthly_income_declare': 0.0,
                            'current_job_start_date': '2024-12-04',
                            'current_job_start_year': 0,
                            'monthly_income': 0.0,
                        },
                    ],
                    'business_infos': [
                        {
                            'income_per_year': 0.0,
                        },
                    ],
                    'cbosdata': [
                        {
                            'id': 'string',
                            'cnt_all_tl_delq_mr00336m': False,
                            'cnt_all_tl_delq_ody36m': False,
                            'customer_has_negative_status_from_ncb': False,
                            'customer_has_negative_status_mcp_from_ncb': False,
                            'is_debt_payment_completed': False,
                            'customer_has_tdr_from_ncb': False,
                            'create_date_time': '2024-12-04T09:13:44.8185437Z',
                            'ncb_grade': 'string',
                            'cbosdata_juristic_credit_reports': [
                                {
                                    'id': 'string',
                                    'ncb_grade': 'string',
                                },
                            ],
                        },
                    ],
                    'financialinfos': {
                        'id': 'string',
                        'total_income': 0.0,
                        'appl_party_financialinfo_hrms': [
                            {
                                'dsr_desc': 'string',
                            },
                        ],
                        'appl_party_financial_statements': [
                            {
                                'financial_stmt_details': [
                                    {
                                        'cheque_back_time': 0,
                                        'statement_month': 'string',
                                    },
                                ],
                            },
                        ],
                        'total_borrower_income': 0.0,
                        'total_fixed_income': 0.0,
                        'monthly_income': 0.0,
                        'residual_income': 0.0,
                    },
                    'oc_code': 'string',
                    'appl_systemverifies': [
                        {
                            'kyc': 'string',
                            'kyc_reason': 'string',
                            'occode': 'string',
                            'appl_systemverify_peps': [
                                {
                                    'id': 'string',
                                    'appl_systemverify_pep_lists': [
                                        {
                                            'id': 'string',
                                        },
                                    ],
                                },
                            ],
                        },
                    ],
                    'accountlistncbs': [
                        {
                            'id': 'string',
                            'ncb_account_type': 'string',
                            'ncb_account_status': 'string',
                        },
                    ],
                },
            },
        ],
        'breInput': [
            {
                'id': 'string',
                'age_in_months': 0,
            },
        ],
        'authorizationInfo': [
            {
                'id': 'string',
                'dscr': 0.0,
                'auth_dscr': 0.0,
                'create_date_time': '2024-12-04T09:13:44.8185585Z',
                'ncb_grade': 'string',
                'mlscoreinfo_mlgroups': [
                    {
                        'id': 'string',
                        'ml_grade': 'string',
                        'ml_score': 0.0,
                        'create_date_time': '2024-12-04T09:13:44.8185609Z',
                    },
                ],
            },
        ],
        'breResults': [
            {
                'id': 'string',
                'total_collateral_amount_gurantor': 0,
            },
        ],
        'financialinfo_etlincome': [
            {
                'id': 'string',
                'party_id': 'string',
                'income': 0.0,
            },
        ],
        'project_gcompsim': [
            {
                'id': 'string',
                'comp_sim': 'string',
                'grade': 'string',
                'group_id': 'string',
            },
        ],
        'mfappl_generalinfo': [
            {
                'application_id': 'string',
                'prefinance_from_scb': 'string',
            },
        ],
        'appl_cpgguideline': [
            {
                'id': 'string',
                'in_cpg_condition_flag': 'string',
                'risk_level': 'string',
            },
        ],
        'mfappl_appraisalworkdetails_collateralitems_basecollatdetls': [
            {
                'located_in_city': False,
            },
        ],
        'appl_qc_vehicle_info': [
            {
                'confirmed_selling_price': 0.0,
                'rb_price': 0.0,
                'up_price_percent': 0.0,
            },
        ],
        'appl_financialinfo': [
            {
                'total_borrower_guarantor_income': 0.0,
                'total_insurance_premium_amount': 0.0,
                'total_dsr': 0.0,
                'dsr_ex_insurance': 0.0,
                'insurance_dsr': 0.0,
            },
        ],
        'appl_collateral_realestate': [
            {
                'appraisal_value': 0.0,
            },
        ],
        'skip_ncb_special_request': 'string',
    },
}
    return json_data

def generate_output(index, input_json, response_json):
    request_id, workflow_output = response_json["RequestId"], response_json["WorkflowOutput"]
    url = f'https://console.nleadsdev.se.scb.co.th/#/report/modern/process/{request_id}?workspace=default'
    output_obj = {
        "return": workflow_output["return"],
        "outcomeMessage": workflow_output["outcomeMessage"],
        "matchRowNumber": workflow_output["matchRowNumber"]
    }

    return [index, input_json, json.dumps(output_obj), url]

# Execution 
# ==========================================================================================



if __name__ == "__main__": 
    # CONSTANTS
    PROCESS_WF_NAME = 'UW_GuarantorKYC3AUTO_Preprocess'
    WF_VERSION=0
    WF_REVISION=15
    EMAIL='sadeeptha.bandara@zorallabs.com'
    EXTERNAL_ID=f"{EMAIL}-{date.today()}"
    HTTP_HEADERS = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': AUTH_TOKEN,
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'expires': '0',
        'origin': 'https://console.nleadsdev.se.scb.co.th',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://console.nleadsdev.se.scb.co.th/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'zworkspace': 'default',
    }
    WORKSHEET_HEADER_COLS = [
        'Test Case No', 
        'Input', 
        'Output', 
        f'Report Link for {PROCESS_WF_NAME} [DEV ENV]'
    ]
    FOLDERNAME = 'data'
    
    # EPHYMERAL CONSTANTS
    AUTH_TOKEN='Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ5NTEwRjQxRjkwNTJFRTNBRjhFQUQyRjk0RkZERDM1Q0UyRjYzRkUiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiJTVkVQUWZrRkx1T3ZqcTB2bFBfZE5jNHZZXzQifQ.eyJuYmYiOjE3MzMzMTA4MDEsImV4cCI6MTczMzMxMjAwMSwiaXNzIjoiaHR0cHM6Ly9hdXRoLm5sZWFkc2Rldi5zZS5zY2IuY28udGgiLCJhdWQiOlsiY29uZmlndXJhdGlvbkFwaSIsIm1vZGVscyIsImF1ZGl0IiwiZGF0YXByb3ZpZGVycyJdLCJjbGllbnRfaWQiOiJjb25zb2xlIiwic3ViIjoiMzg1IiwiYXV0aF90aW1lIjoxNzMzMzA3MjY1LCJpZHAiOiJvaWRjIiwicm9sZSI6WyJEZWNpc2lvbkVuZ2luZVdvcmtmbG93U2lnbmVyIiwiRGVjaXNpb25FbmdpbmVXb3JrZmxvd0VkaXRvciIsIkRlY2lzaW9uRW5naW5lV29ya2Zsb3dWaWV3ZXIiLCJEZWNpc2lvbkVuZ2luZUF1ZGl0Vmlld2VyIiwiRGVjaXNpb25FbmdpbmVSZXBvcnRWaWV3ZXIiLCJEZWNpc2lvbkVuZ2luZVByb3RlY3RlZERhdGFWaWV3ZXIiLCJCRFdBZG1pbmlzdHJhdG9yIiwiQkRXQ29uZmlndXJhdGlvblZpZXdlciIsIkJEV0RhdGFWaWV3ZXIiLCJEZWNpc2lvbkVuZ2luZVJlY292ZXJ5TWFuYWdlciIsIkRlY2lzaW9uRW5naW5lV29ya2Zsb3dFeGVjdXRvciIsIkFEV0FkbWluaXN0cmF0b3IiLCJCT1VzZXIiLCJTQ0JfQVVUTyIsIlNDQl9DUk9TU1BST0RVQ1QiLCJTQ0JfTU9SVEdBR0UiLCJTQ0JfVU5TRUNVUkVEIiwiQWRtaW5pc3RyYXRvciJdLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9lbWFpbGFkZHJlc3MiOiJzYWRlZXB0aGEuYmFuZGFyYUB6b3JhbGxhYnMuY29tIiwiQXNwTmV0LklkZW50aXR5LlNlY3VyaXR5U3RhbXAiOiJFUElSRlJSNUM3NVFPSUlURUlUN05VTDIyM0RLN1lTTyIsImdyYWZhbmFfcm9sZSI6ImFkbWluIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2FkZWVwdGhhLmJhbmRhcmFAem9yYWxsYWJzLmNvbSIsIm5hbWUiOiJzYWRlZXB0aGEuYmFuZGFyYUB6b3JhbGxhYnMuY29tIiwiZW1haWwiOiJzYWRlZXB0aGEuYmFuZGFyYUB6b3JhbGxhYnMuY29tIiwiZW1haWxfdmVyaWZpZWQiOiJmYWxzZSIsImh0dHBzOi8vYWR3LnpvcmFsbGFicy5jb20vand0L2NsYWltcyI6IntcIngtYWR3LWFsbG93ZWQtZmVhdHVyZXNcIjpcIntcXFwiQXV0b1xcXCIsXFxcIkNyb3NzUHJvZHVjdFxcXCIsXFxcIk1vcnRnYWdlXFxcIixcXFwiVW5zZWN1cmVkXFxcIn1cIixcIngtYWR3LWFsbG93ZWQtcm9sZXNcIjpbXCJhZG1pblwiXSxcIngtYWR3LWRlZmF1bHQtcm9sZVwiOlwiYWRtaW5cIixcIngtYWR3LXVzZXItaWRcIjpcInNhZGVlcHRoYS5iYW5kYXJhQHpvcmFsbGFicy5jb21cIn0iLCJzY29wZSI6WyJvcGVuaWQiLCJwcm9maWxlIiwiZW1haWwiLCJ1c2VyZGF0YSIsImNvbmZpZ3VyYXRpb25BcGkiLCJtb2RlbHMiLCJhdWRpdCIsImRhdGFwcm92aWRlcnMiXSwiYW1yIjpbImV4dGVybmFsIl19.ibjY4YBAP6ynf8ZlVD5xBYTHqujOduFi-KBUvtxe9OBVDoQP-AtS_afX4JKfLmj66U1g7i6n0Iy7oFLRjvyT_A9hg8d6X5ar42SfSXPhZASrROyVzJOmFX4ykFiOUOjrvBmTUfMsojOREoC67z_rA6avRCG-NGgruQ4bs3uSvYZyugNt9S7Nr_FkHtmXzo-TsMEQhO-LE1JAzPnlmehgTQpmJco4II1V10WSLyw68vmC-gb-GRRVJbJd7x7X4pJrKB2XSbTv81I8vpCpnrGd01BvBm3BDJDyCW4zJXFvILc9PAZoWQy8if49_hSnGFezgAUfJfJn-3jxvaHDK43C-A'
    DATA_INPUTS = [
        {
            "kycLevel":"",
            "kycReason":"",
            "occupation":"",
            "kycLevelRM":"",
            "kycReasonRM":""
        }
    ]

    output_agg = []
    for row_no, data_input in enumerate(DATA_INPUTS, 1):
        input_json = get_data(data_input)

        response = requests.post(
            f'https://ms.nleadsdev.se.scb.co.th/runtime/api/process?workflowType=Process&workflowName={PROCESS_WF_NAME}&workflowVersion={WF_VERSION}&workflowRevision={WF_REVISION}&externalId={EXTERNAL_ID}&externalSystemCode=ms-invoke&settingsProfile=Default&uiRequest=true&scriptingRuntime=',
            headers=HTTP_HEADERS,
            json=input_json
        )
        
        out = generate_output(input_json, response.json())
        output_agg.append(out)

    filepath = os.path.join(os.getcwd(), FOLDERNAME, f'TestCase-{PROCESS_WF_NAME}.xlsx')
    write_preprocess_testcases(filepath, WORKSHEET_HEADER_COLS, output_agg)





