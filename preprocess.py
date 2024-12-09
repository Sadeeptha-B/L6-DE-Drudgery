import requests
from datetime import date
from utils.excel_writer import write_preprocess_testcases 
import os
import json

def get_data(i):
    json_data = {
    'userId': 'string',
    'stationId': 'string',
    'applicationDetails': {
        'application_id': 'APP191000101V',
        'application_type_id': 'New',
        'application_group_id': 'MortgageGroup',
        'application_date_time_in': '2024-07-19T10:00:24.3850000+07:00',
        'channel_id': 'PartnerTools',
        'is_branch_manager_comment': True,
        'skip_ncb_special_request': 'SPREQ',
        'create_date_time': '2024-07-18T20:00:25.6700000+07:00',
        'appl_authorizationinfo': {
            'ncb_grade': 'C',
        },
        'appl_parties': [
            {
                'id': '0c0b0c76-457b-11ef-9409-46564be27671',
                'rm_kyc_level_id': 1,
                'rm_kyc_reason_id': 1,
                'relationship': None,
                'kyc_level_id': 1,
                'customer_type_code': 'C',
                'collateral_owners': [],
                'cbosdata': [
                    {
                        'id': 'd28f6fec-311a-11ef-8d51-7277a50224fd',
                        'cnt_all_tl_delq_mr00336m': None,
                        'cnt_all_tl_delq_ody36m': None,
                        'ncb_grade': '00',
                        'cbosdata_juristic_credit_reports': [
                            {
                                'id': '5693c73c-5477-11ef-b5e8-46564be27671',
                                'ncb_grade': 'D',
                            },
                            {
                                'id': 'dd9ce890-548f-11ef-8adb-46564be27671',
                                'ncb_grade': 'D',
                            },
                        ],
                        'party_cbosdata_listpnsegments': [
                            {
                                'party_cbosdata_listidsegments': [
                                    {
                                        'party_cbosdata_listtlsegments': [
                                            {
                                                'pay_hist1': 'TEST',
                                                'create_date_time': '2024-09-19T10:20:46.1847250+07:00',
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
                        'appl_party_id': '0c0b0c76-457b-11ef-9409-46564be27671',
                        'staff_id': '111',
                        'dob': '1980-07-22',
                        'current_job_start_date': '2022-01-23',
                        'current_job_start_year': None,
                        'monthly_income_declare': None,
                        'current_job_start_month': None,
                        'nationality_id': None,
                        'job_position_id': None,
                        'occupation_id': 'TEST',
                        'occupation_group_id': None,
                        'monthly_income': None,
                        'company_title_name_id': None,
                    },
                ],
                'financialinfos': {
                    'total_income': 120000,
                    'monthly_income': 10000,
                    'total_other_income': None,
                    'residual_income': None,
                    'income_freq': None,
                    'estimated_ifs': 9001,
                    'ifs': 9001,
                    'total_debt_burden': None,
                    'total_guarantor_income': None,
                    'appl_party_financialinfo_hrms': [
                        {
                            'dsr_desc': 'ไม่อยู่ในเกณฑ์',
                        },
                    ],
                },
                'borrowers': [
                    {
                        'id': '0c0e11aa-457b-11ef-940f-46564be27671',
                        'party': {
                            'rm_kyc_level_id': 1,
                            'rm_kyc_reason_id': 1,
                            'id': '0c0b0c76-457b-11ef-9409-46564be27671',
                            'relationship': None,
                            'financialinfos': {
                                'id': '7afc9236-700e-11ef-b146-46564be27671',
                                'total_borrower_income': None,
                            },
                            'personal_infos': [
                                {
                                    'id': '0c0c465e-457b-11ef-940b-46564be27671',
                                    'monthly_income_declare': None,
                                    'current_job_start_month': None,
                                },
                            ],
                        },
                    },
                ],
                'appl_guarantees': [
                    {
                        'party_type_id': 'Guarantor',
                        'party': {
                            'id': '0c0b0c76-457b-11ef-9409-46564be27671',
                            'personal_infos': [
                                {
                                    'id': '0c0c465e-457b-11ef-940b-46564be27671',
                                    'company_title_name_id': None,
                                    'current_job_start_month': None,
                                },
                            ],
                        },
                    },
                ],
                'appl_systemverifies': [
                    {
                        'id': '1332dc52-a25c-11ef-9f17-43bd561d2667',
                        'system_verify_type': None,
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                ],
            },
            {
                'id': 'a1232d52-2cad-11ef-ae14-a736e7657da9',
                'rm_kyc_level_id': None,
                'rm_kyc_reason_id': None,
                'relationship': None,
                'kyc_level_id': 1,
                'customer_type_code': 'P',
                'collateral_owners': [],
                'cbosdata': [],
                'personal_infos': [
                    {
                        'appl_party_id': 'a1232d52-2cad-11ef-ae14-a736e7657da9',
                        'staff_id': None,
                        'dob': None,
                        'current_job_start_date': None,
                        'current_job_start_year': None,
                        'monthly_income_declare': None,
                        'current_job_start_month': None,
                        'nationality_id': None,
                        'job_position_id': None,
                        'occupation_id': '01',
                        'occupation_group_id': None,
                        'monthly_income': None,
                        'company_title_name_id': None,
                    },
                ],
                'financialinfos': None,
                'borrowers': [
                    {
                        'id': 'a125777e-2cad-11ef-ae19-cf4579dfa48f',
                        'party': {
                            'rm_kyc_level_id': None,
                            'rm_kyc_reason_id': None,
                            'id': 'a1232d52-2cad-11ef-ae14-a736e7657da9',
                            'relationship': None,
                            'financialinfos': None,
                            'personal_infos': [
                                {
                                    'id': 'a123d810-2cad-11ef-ae15-2b700796f678',
                                    'monthly_income_declare': None,
                                    'current_job_start_month': None,
                                },
                            ],
                        },
                    },
                    {
                        'id': 'bff0c8f8-6f96-11ef-a930-46564be27671',
                        'party': {
                            'rm_kyc_level_id': None,
                            'rm_kyc_reason_id': None,
                            'id': 'a1232d52-2cad-11ef-ae14-a736e7657da9',
                            'relationship': None,
                            'financialinfos': None,
                            'personal_infos': [
                                {
                                    'id': 'a123d810-2cad-11ef-ae15-2b700796f678',
                                    'monthly_income_declare': None,
                                    'current_job_start_month': None,
                                },
                            ],
                        },
                    },
                ],
                'appl_guarantees': [],
                'appl_systemverifies': [
                    {
                        'id': '585bdf3a-903d-11ef-8a18-e3991747d0c5',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': 'A4114',
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': '9e4bc5f4-903e-11ef-a18c-ef80e5fc0fae',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': '63c84b1e-9039-11ef-9379-d37014383e17',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': '85829d58-903f-11ef-b14a-7b8bf136467e',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': '993f2704-9039-11ef-b804-07478cd65d06',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': '6ea3c9b4-8229-11ef-8963-e3af22cee4a1',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': 'A2223',
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [
                            {
                                'id': '64bfac20-50d7-11ef-a2e4-46564be27671',
                                'watchlist_lists': [
                                    {
                                        'id': '64e972bc-50d7-11ef-8c6a-46564be27671',
                                        'bkl_type': '1',
                                        'bkl_subtype': '22',
                                        'bkl_degree': 'W99',
                                    },
                                    {
                                        'id': '64e976ea-50d7-11ef-8c6b-46564be27671',
                                        'bkl_type': '5',
                                        'bkl_subtype': '25',
                                        'bkl_degree': 'W10',
                                    },
                                ],
                            },
                        ],
                        'appl_systemverify_cdds': [
                            {
                                'id': '0c421ce6-65c6-11ef-91c1-46564be27671',
                                'appl_systemverify_cdd_alerts': [
                                    {
                                        'id': '0c421ce6-65c6-11ef-91c1-46564be27671',
                                        'cdd_seq': 1,
                                    },
                                ],
                            },
                        ],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [
                            {
                                'id': '79e11990-822d-11ef-b456-3f63c2fa71c5',
                                'found_status': 'Found',
                                'is_validate_person': None,
                            },
                            {
                                'id': '4a399fd6-822e-11ef-9a66-bba8a467a309',
                                'found_status': 'Found',
                                'is_validate_person': None,
                            },
                            {
                                'id': '3bee4e9a-822e-11ef-83c2-0f86bbe503bc',
                                'found_status': 'Found',
                                'is_validate_person': None,
                            },
                            {
                                'id': '4719ca3c-822f-11ef-9d89-bb24570c3f8c',
                                'found_status': 'Found',
                                'is_validate_person': None,
                            },
                        ],
                        'appl_systemverify_rmservices': [
                            {
                                'id': '45d2b724-822f-11ef-8e15-e7b8d135357c',
                                'appl_systemverify_rmservice_products': [
                                    {
                                        'id': '70c0de2a-8b71-11ef-9f72-274057323e31',
                                        'appl_systemverify_rmservice_cardproducts': [
                                            {
                                                'id': 'b9a102e2-7bc1-11ef-9ea9-26f16a5dcb9c',
                                                'card_status': 'C',
                                            },
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                    {
                        'id': '46b6ca5e-903a-11ef-92bf-ab681f86106f',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': '5038005e-904c-11ef-b579-bf27f6ebe51f',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': '5d8f5f2a-903a-11ef-9054-ff7e07af2874',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': '7e3152a2-8f80-11ef-9c97-078c35cd2f79',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': 'b81c5bb4-9c1a-11ef-be53-6b7fb900da95',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': None,
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                    {
                        'id': '38ff4464-9039-11ef-991e-cbfa3d0ab0f3',
                        'system_verify_type': 'Borrower1',
                        'rm_occode': 'A4114',
                        'occode': None,
                        'kyc': None,
                        'kyc_reason': None,
                        'appl_systemverify_watchlists': [],
                        'appl_systemverify_cdds': [],
                        'appl_systemverify_relateds': [],
                        'appl_systemverify_frauds': [],
                        'appl_systemverify_rmservices': [],
                    },
                ],
            },
            {
                'id': 'd9047b3e-9b3b-11ef-be57-238f305467b1',
                'rm_kyc_level_id': None,
                'rm_kyc_reason_id': None,
                'relationship': None,
                'kyc_level_id': 1,
                'customer_type_code': 'C',
                'collateral_owners': [
                    {
                        'id': 'd9061340-9b3b-11ef-be5c-f71729c90ce8',
                        'appl_party_id': 'd9047b3e-9b3b-11ef-be57-238f305467b1',
                    },
                ],
                'cbosdata': [],
                'personal_infos': [
                    {
                        'appl_party_id': 'd9047b3e-9b3b-11ef-be57-238f305467b1',
                        'staff_id': None,
                        'dob': None,
                        'current_job_start_date': None,
                        'current_job_start_year': None,
                        'monthly_income_declare': None,
                        'current_job_start_month': None,
                        'nationality_id': None,
                        'job_position_id': None,
                        'occupation_id': None,
                        'occupation_group_id': None,
                        'monthly_income': None,
                        'company_title_name_id': None,
                    },
                ],
                'financialinfos': None,
                'borrowers': [],
                'appl_guarantees': [],
                'appl_systemverifies': [],
            },
            {
                'id': 'f70c5212-9b42-11ef-a537-475a4d96cff9',
                'rm_kyc_level_id': None,
                'rm_kyc_reason_id': None,
                'relationship': None,
                'kyc_level_id': 1,
                'customer_type_code': 'P',
                'collateral_owners': [],
                'cbosdata': [],
                'personal_infos': [
                    {
                        'appl_party_id': 'f70c5212-9b42-11ef-a537-475a4d96cff9',
                        'staff_id': None,
                        'dob': '2002-01-01',
                        'current_job_start_date': None,
                        'current_job_start_year': None,
                        'monthly_income_declare': None,
                        'current_job_start_month': None,
                        'nationality_id': 'TH',
                        'job_position_id': None,
                        'occupation_id': None,
                        'occupation_group_id': None,
                        'monthly_income': None,
                        'company_title_name_id': '2',
                    },
                ],
                'financialinfos': None,
                'borrowers': [],
                'appl_guarantees': [],
                'appl_systemverifies': [],
            },
            {
                'id': '1ff1f8de-9cd4-11ef-be95-d729ab3bdeac',
                'rm_kyc_level_id': None,
                'rm_kyc_reason_id': None,
                'relationship': None,
                'kyc_level_id': 1,
                'customer_type_code': 'C',
                'collateral_owners': [
                    {
                        'id': '1ff55290-9cd4-11ef-be9a-dfd3f1724930',
                        'appl_party_id': '1ff1f8de-9cd4-11ef-be95-d729ab3bdeac',
                    },
                ],
                'cbosdata': [],
                'personal_infos': [
                    {
                        'appl_party_id': '1ff1f8de-9cd4-11ef-be95-d729ab3bdeac',
                        'staff_id': None,
                        'dob': None,
                        'current_job_start_date': None,
                        'current_job_start_year': None,
                        'monthly_income_declare': None,
                        'current_job_start_month': None,
                        'nationality_id': None,
                        'job_position_id': None,
                        'occupation_id': None,
                        'occupation_group_id': None,
                        'monthly_income': None,
                        'company_title_name_id': None,
                    },
                ],
                'financialinfos': None,
                'borrowers': [],
                'appl_guarantees': [],
                'appl_systemverifies': [],
            },
            {
                'id': 'a20a1edc-9cd4-11ef-9f78-5b7641b2f585',
                'rm_kyc_level_id': None,
                'rm_kyc_reason_id': None,
                'relationship': None,
                'kyc_level_id': 1,
                'customer_type_code': 'P',
                'collateral_owners': [],
                'cbosdata': [],
                'personal_infos': [
                    {
                        'appl_party_id': 'a20a1edc-9cd4-11ef-9f78-5b7641b2f585',
                        'staff_id': None,
                        'dob': '1971-06-12',
                        'current_job_start_date': None,
                        'current_job_start_year': None,
                        'monthly_income_declare': None,
                        'current_job_start_month': None,
                        'nationality_id': 'IM',
                        'job_position_id': None,
                        'occupation_id': None,
                        'occupation_group_id': None,
                        'monthly_income': None,
                        'company_title_name_id': '1',
                    },
                ],
                'financialinfos': None,
                'borrowers': [],
                'appl_guarantees': [],
                'appl_systemverifies': [],
            },
            {
                'id': '2fc1396e-9833-11ef-b5b4-23fbe3a95cbe',
                'rm_kyc_level_id': None,
                'rm_kyc_reason_id': None,
                'relationship': None,
                'kyc_level_id': 1,
                'customer_type_code': 'C',
                'collateral_owners': [
                    {
                        'id': '2fc2afb0-9833-11ef-b5b9-bfe6e8fe23f5',
                        'appl_party_id': '2fc1396e-9833-11ef-b5b4-23fbe3a95cbe',
                    },
                ],
                'cbosdata': [],
                'personal_infos': [
                    {
                        'appl_party_id': '2fc1396e-9833-11ef-b5b4-23fbe3a95cbe',
                        'staff_id': None,
                        'dob': None,
                        'current_job_start_date': None,
                        'current_job_start_year': None,
                        'monthly_income_declare': None,
                        'current_job_start_month': None,
                        'nationality_id': None,
                        'job_position_id': None,
                        'occupation_id': None,
                        'occupation_group_id': None,
                        'monthly_income': None,
                        'company_title_name_id': None,
                    },
                ],
                'financialinfos': None,
                'borrowers': [],
                'appl_guarantees': [],
                'appl_systemverifies': [],
            },
        ],
        'accounts': [
            {
                'account_autos': {
                    'als_remaining_term': 12,
                    'balloon_installment_amount': 1,
                    'no_of_installment': 60,
                    'standard_subsidy_interest': 1.1,
                    'require_rate_of_return': 1,
                    'interest_rate': 2.99,
                    'standard_rate': 1.1,
                    'principal_amount': 1.11,
                    'tracking_car_code': 'CC-5542',
                    'tracking_test_code': 'TEST',
                    'normal_installment': 25000,
                    'percentage_insurance_ltv': None,
                    'vehicle_price': 750000,
                    'tracking_authority_code': None,
                    'actual_percentage_ltv': None,
                    'percentage_ltv': 26.3,
                    'insurance_percentage_down': None,
                    'id': '73798d96-65f2-11ef-b80a-46564be27671',
                },
                'account_sublimits': [],
                'account_additionalservices': [
                    {
                        'addition_service_type': '17',
                        'addition_service_group': None,
                        'is_credit_line_included': None,
                        'premium_amount': None,
                        'create_date_time': '2024-06-24T00:15:27.4137180+07:00',
                        'insurance_cover_amount': None,
                        'insurance_period': None,
                    },
                    {
                        'addition_service_type': '98',
                        'addition_service_group': '0004',
                        'is_credit_line_included': False,
                        'premium_amount': 456698.9,
                        'create_date_time': '2024-10-21T13:29:10.7241450+07:00',
                        'insurance_cover_amount': None,
                        'insurance_period': 78,
                    },
                ],
                'account_partialinstallment_details': [
                    {
                        'premium_requested_amt': 300000,
                    },
                ],
                'appl_account_vat_infos': [
                    {
                        'description': 'downPayment',
                        'amount_include_vat': 10000,
                    },
                ],
                'appl_dealer': {
                    'dealer_group': 'G4',
                },
                'appl_account_existing_loans': [
                    {
                        'product_type_desc': 'SCB',
                        'no_of_installments_unpaid': 7,
                        'no_of_installments': 9,
                        'installment_amount_include_vat': 25100,
                        'good_retail': 'A2332',
                        'original_contract_dt': '2020-10-10',
                        'id': '4880619c-8621-11ef-bdfa-7f8725373460',
                    },
                ],
                'account_fees': [],
                'account_collaterals': [
                    {
                        'is_new_collateral': True,
                        'collateral_auto': {
                            'id': '09df04c6-5998-11ef-88a4-46564be27671',
                            'vehicle_type': '0004:0011:005',
                            'vehicle_brand': 'FOR',
                            'vehicle_model': 'EVE',
                            'vehicle_age': 12,
                            'engine_type': 'BENZINE',
                            'registered_date': None,
                            'sum_container': 0,
                            'rb_price': 0,
                            'sum_modification_kit': 0,
                            'sum_of_life_insurance_premium': None,
                            'insurances': [
                                {
                                    'insurance_type': 'VehicleInsur',
                                    'sum_insured': None,
                                    'vehicle_source_of_insurance': '2',
                                    'insurer': '01710006',
                                    'vehicle_premium_incl_vat': None,
                                    'id': 'ebdda804-adfe-11ef-abe8-8ff258c21bc2',
                                },
                            ],
                            'auto_accessories': [
                                {
                                    'amount': 352,
                                },
                            ],
                            'insurance_lifeinsurances': [],
                        },
                        'collateral_real_estate': {
                            'id': '09dfa0fc-5998-11ef-88a5-46564be27671',
                            'project_code': None,
                            'zip_code': None,
                            'is_free_debtburden': None,
                            'collateral_type': None,
                            'number_of_unit': None,
                            'province': None,
                            'land_appraisal_value': None,
                            'fire_insurance_amount': None,
                            'existing_fire_insurance_amount': None,
                            'is_subordinated': None,
                            'subordinated_detail': None,
                            'is_located_in_city': None,
                            'type_of_building': '1',
                            'collateral_realestate_buildingdetails': [
                                {
                                    'id': 'e93f0f2a-d4c8-40fa-a189-3b8cbbf49808',
                                },
                            ],
                            'collateral_realestate_condodetails': [
                                {
                                    'id': 'd5a86ba8-49d8-11ef-a29a-46564be27671',
                                },
                            ],
                        },
                        'collateral_security': {
                            'id': '89061efc-44e3-11ef-b173-46564be27671',
                            'collateral_type': '0121',
                            'appraisal_value': None,
                        },
                        'account_collateral_owners': [],
                        'id': '09e0b5c8-5998-11ef-88a6-46564be27671',
                        'legal_transaction_type_code': None,
                        'legal_transaction_amount': None,
                        'number_total_housing_debt': None,
                        'appl_collateral_guarantee_id': None,
                        'appl_collateral_cash_id': None,
                        'appl_collateral_realestate_id': '09dfa0fc-5998-11ef-88a5-46564be27671',
                        'appl_collateral_security_id': '89061efc-44e3-11ef-b173-46564be27671',
                        'appl_collateral_auto_id': '09df04c6-5998-11ef-88a4-46564be27671',
                        'create_date_time': '2024-08-14T00:18:20.7113060+07:00',
                    },
                ],
                'appl_account_bre_inputs': [
                    {
                        'id': '5e40769e-9831-11ef-b068-a3f67a81c987',
                        'total_ltav': 25310,
                        'create_date_time': '2024-08-27T03:43:05.4184580+07:00',
                    },
                ],
                'id': 'ebf76695-3987-08df-5d6d-c1959602a940',
                'investment_percent': None,
                'letter_amount': None,
                'master_account_flag': None,
                'old_credit_line_amount': 20000,
                'requested_amount': 50000,
                'npanpl_code': None,
                'developer_code': None,
                'product_group_id': 'Mortgage',
                'product_program': 'MORT_NLNORMAL',
                'balance_credit_line_amount': None,
                'pri_credit_limit': None,
                'inquiry_no_period_unpaid': 4,
                'pis_credit_limit': None,
                'approved_amount': None,
                'partner_code': None,
                'product_type_id': 'Mortgage',
                'project_code': 'Green',
                'sub_product_type_id': 'REFINANCE',
                'tenor_month': None,
                'tenor_year': None,
                'campaign_id': None,
                'package_loan_code': None,
                'broker_code': None,
                'inquiry_amt_unpaid': None,
                'account_installment_monthly_amount': None,
                'loan_purpose_code': None,
                'mf_project_colour': None,
                'pot_credit_limit': None,
                'sub_loan_type': '2419',
                'credit_line_type': 'LOAN',
                'inquiry_outstanding_amount': None,
                'payment_method': 'Cash',
                'account_objectives': [
                    {
                        'id': '6dde50ce-8f78-11ef-8a70-a3900c473c8d',
                        'objective_id': '53',
                    },
                ],
                'payment_items': [
                    {
                        'id': '2327e15e-b3ad-11ef-b911-fb27b2d56126',
                        'payment_method': None,
                    },
                ],
                'existing_loan_fees': [],
            },
        ],
        'primary_borrower': {
            'borrower': {
                'id': '0c0e11aa-457b-11ef-940f-46564be27671',
                'party_type_id': '01',
                'party': {
                    'id': '0c0b0c76-457b-11ef-9409-46564be27671',
                    'relationship': None,
                    'addresses': [
                        {
                            'id': '67f9fcba-18ba-11ef-9a53-63d6ef117404',
                            'address_owner': 'HeadofHousehold',
                        },
                    ],
                    'minor2_id': '1A',
                    'income_type': 'SA',
                    'kyc_level_id': 1,
                    'kyc_reason_id': None,
                    'rm_kyc_level_id': 1,
                    'rm_kyc_reason_id': 1,
                    'customer_type_code': 'C',
                    'appl_guarantees': [
                        {
                            'id': '03a336fc-2498-11ef-acdd-bb04205cf958',
                            'party_type_id': 'Guarantor',
                            'party': {
                                'id': '0c0b0c76-457b-11ef-9409-46564be27671',
                                'oc_code': '6849',
                                'personal_infos': [
                                    {
                                        'id': '0c0c465e-457b-11ef-940b-46564be27671',
                                        'company_title_name_id': None,
                                        'current_job_start_date': '2022-01-23',
                                        'current_job_start_month': None,
                                        'occupation_id': f'{i["Occupation"]}',
                                        'dob': '1980-07-22',
                                    },
                                ],
                                'appl_systemverifies': [
                                    {
                                        'id': '1332dc52-a25c-11ef-9f17-43bd561d2667',
                                        'create_date_time': '2024-07-12T13:06:52.0000000+07:00',
                                        'kyc': f'{i["KYCLevel"]}',
                                        'kyc_reason': f'{i["KYCReason"]}',
                                        'rm_kyc': f'{i["KYCLevelRM"]}',
                                        'rm_kyc_reason': f'{i["KYCReasonRM"]}',
                                    },
                                ],
                            },
                        },
                    ],
                    'cbosdata': [
                        {
                            'id': 'd28f6fec-311a-11ef-8d51-7277a50224fd',
                            'ncb_grade': '00',
                            'is_good_payment_in_curr_month': True,
                            'cnt_all_tl_delq_mr00336m': None,
                            'cnt_all_tl_delq_ody36m': None,
                            'count_enquiries_new_appl_90day': 10,
                            'create_date_time': '2024-06-22T21:41:14.3227320+07:00',
                            'cbosdata_juristic_credit_reports': [
                                {
                                    'id': '5693c73c-5477-11ef-b5e8-46564be27671',
                                    'ncb_grade': 'D',
                                    'create_date_time': '2024-08-07T11:41:40.2064720+07:00',
                                },
                                {
                                    'id': 'dd9ce890-548f-11ef-8adb-46564be27671',
                                    'ncb_grade': 'D',
                                    'create_date_time': '2024-08-07T14:37:14.6768550+07:00',
                                },
                            ],
                            'party_cbosdata_listpnsegments': [
                                {
                                    'id': '05975cec-311b-11ef-8d52-7277a50224fd',
                                    'party_cbosdata_listidsegments': [
                                        {
                                            'id': '16f6801c-311b-11ef-8d53-7277a50224fd',
                                            'party_cbosdata_listtlsegments': [
                                                {
                                                    'id': '291cfd06-7636-11ef-9720-46564be27671',
                                                    'pay_hist1': 'TEST',
                                                    'create_date_time': '2024-09-19T10:20:46.1847250+07:00',
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
                            'customer_type_group_id': '0001',
                            'dob': '1980-07-22',
                            'id': '0c0c465e-457b-11ef-940b-46564be27671',
                            'source_of_income': 'TH',
                            'income_type': 'Freelancing',
                            'occupation_id': 'TEST',
                            'occupation_group_id': None,
                            'monthly_income_declare': None,
                            'nationality_id': None,
                            'staff_id': '111',
                            'current_job_start_date': '2022-01-23',
                            'current_job_start_year': None,
                            'monthly_income': None,
                            'company_title_name_id': None,
                            'current_job_start_month': None,
                            'company_isic': 'G478940',
                            'create_date_time': '2024-07-18T20:00:25.6705400+07:00',
                        },
                    ],
                    'financialinfos': {
                        'id': '7afc9236-700e-11ef-b146-46564be27671',
                        'total_guarantor_income': None,
                        'total_income': 120000,
                        'monthly_income': 10000,
                        'estimated_ifs': 9001,
                        'ifs': 9001,
                        'total_other_income': None,
                        'total_borrower_income': None,
                        'total_fixed_income': None,
                        'residual_income': None,
                        'income_freq': None,
                        'total_debt_burden': None,
                        'inquiry_income_source': 'PQ',
                        'pq_campaign_credit_limit': 42452,
                        'appl_party_financialinfo_hrms': [
                            {
                                'id': '3814ebb0-5e04-11ef-a289-a3303ea332a6',
                                'dsr_desc': 'ไม่อยู่ในเกณฑ์',
                                'level': 'HIGH',
                                'create_date_time': '2024-08-19T15:22:48.6952100+07:00',
                            },
                        ],
                        'appl_party_financial_statements': [
                            {
                                'id': '4ba3165c-6c37-11ef-a129-46564be27671',
                                'financial_stmt_details': [
                                    {
                                        'id': '4ca84220-6c37-11ef-bf1a-46564be27671',
                                        'cheque_back_time': 1,
                                        'statement_month': None,
                                    },
                                    {
                                        'id': '4d8cace4-6c37-11ef-8ea4-46564be27671',
                                        'cheque_back_time': None,
                                        'statement_month': None,
                                    },
                                    {
                                        'id': '4e48e148-6c37-11ef-8ea5-46564be27671',
                                        'cheque_back_time': None,
                                        'statement_month': None,
                                    },
                                ],
                            },
                        ],
                    },
                    'business_infos': [
                        {
                            'id': '0c0cd3da-457b-11ef-940c-46564be27671',
                            'business_main_type_id': '3',
                        },
                    ],
                    'oc_code': '6849',
                    'appl_systemverifies': [
                        {
                            'id': '1332dc52-a25c-11ef-9f17-43bd561d2667',
                            'kyc': None,
                            'kyc_reason': None,
                            'occode': None,
                            'appl_systemverify_peps': [],
                        },
                    ],
                    'accountlistncbs': [
                        {
                            'id': '0c0bbb94-457b-11ef-940a-46564be27671',
                            'ncb_account_type': 'ncb_account_type',
                            'ncb_member_short_name': None,
                            'ncb_date_of_last_debt_restructure': None,
                            'ncb_account_status': 'Unknown',
                            'ncb_amount_owned': 8000,
                            'create_date_time': '2024-07-18T20:00:25.6705400+07:00',
                        },
                    ],
                    'segment_id': '78',
                },
            },
        },
        'borrowers': [
            {
                'id': '0c0e11aa-457b-11ef-940f-46564be27671',
                'party_type_id': '01',
                'party': {
                    'id': '0c0b0c76-457b-11ef-9409-46564be27671',
                    'relationship': None,
                    'income_type': 'SA',
                    'kyc_level_id': 1,
                    'kyc_reason_id': None,
                    'rm_kyc_level_id': 1,
                    'rm_kyc_reason_id': 1,
                    'customer_type_code': 'C',
                    'appl_guarantees': [
                        {
                            'party_type_id': 'Guarantor',
                            'party': {
                                'id': '0c0b0c76-457b-11ef-9409-46564be27671',
                                'personal_infos': [
                                    {
                                        'id': '0c0c465e-457b-11ef-940b-46564be27671',
                                        'company_title_name_id': None,
                                        'current_job_start_month': None,
                                    },
                                ],
                            },
                        },
                    ],
                    'addresses': [
                        {
                            'id': '67f9fcba-18ba-11ef-9a53-63d6ef117404',
                            'address_owner': 'HeadofHousehold',
                        },
                    ],
                    'business_infos': [
                        {
                            'id': '0c0cd3da-457b-11ef-940c-46564be27671',
                            'income_per_year': 12332,
                            'create_date_time': '2024-07-18T20:00:25.6705400+07:00',
                        },
                    ],
                    'cbosdata': [
                        {
                            'id': 'd28f6fec-311a-11ef-8d51-7277a50224fd',
                            'ncb_grade': '00',
                            'cnt_all_tl_delq_mr00336m': None,
                            'cnt_all_tl_delq_ody36m': None,
                            'create_date_time': '2024-06-22T21:41:14.3227320+07:00',
                            'customer_has_negative_status_from_ncb': None,
                            'customer_has_negative_status_mcp_from_ncb': None,
                            'is_debt_payment_completed': None,
                            'customer_has_tdr_from_ncb': None,
                            'cbosdata_juristic_credit_reports': [
                                {
                                    'id': '5693c73c-5477-11ef-b5e8-46564be27671',
                                    'ncb_grade': 'D',
                                },
                                {
                                    'id': 'dd9ce890-548f-11ef-8adb-46564be27671',
                                    'ncb_grade': 'D',
                                },
                            ],
                            'party_cbosdata_listpnsegments': [
                                {
                                    'id': '05975cec-311b-11ef-8d52-7277a50224fd',
                                    'party_cbosdata_listidsegments': [
                                        {
                                            'id': '16f6801c-311b-11ef-8d53-7277a50224fd',
                                            'party_cbosdata_listtlsegments': [
                                                {
                                                    'id': '291cfd06-7636-11ef-9720-46564be27671',
                                                    'pay_hist1': 'TEST',
                                                    'create_date_time': '2024-09-19T10:20:46.1847250+07:00',
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
                            'customer_type_group_id': '0001',
                            'dob': '1980-07-22',
                            'id': '0c0c465e-457b-11ef-940b-46564be27671',
                            'source_of_income': 'TH',
                            'occupation_id': 'TEST',
                            'occupation_group_id': None,
                            'monthly_income_declare': None,
                            'nationality_id': None,
                            'staff_id': '111',
                            'current_job_start_date': '2022-01-23',
                            'current_job_start_year': None,
                            'monthly_income': None,
                            'company_title_name_id': None,
                            'current_job_start_month': None,
                        },
                    ],
                    'financialinfos': {
                        'id': '7afc9236-700e-11ef-b146-46564be27671',
                        'total_income': 120000,
                        'monthly_income': 10000,
                        'estimated_ifs': 9001,
                        'ifs': 9001,
                        'total_other_income': None,
                        'total_borrower_income': None,
                        'total_guarantor_income': None,
                        'total_fixed_income': None,
                        'residual_income': None,
                        'income_freq': None,
                        'total_debt_burden': None,
                        'appl_party_financialinfo_hrms': [
                            {
                                'id': '3814ebb0-5e04-11ef-a289-a3303ea332a6',
                                'dsr_desc': 'ไม่อยู่ในเกณฑ์',
                            },
                        ],
                        'appl_party_financial_statements': [
                            {
                                'id': '4ba3165c-6c37-11ef-a129-46564be27671',
                                'financial_stmt_details': [
                                    {
                                        'id': '4ca84220-6c37-11ef-bf1a-46564be27671',
                                        'cheque_back_time': 1,
                                        'statement_month': None,
                                    },
                                    {
                                        'id': '4d8cace4-6c37-11ef-8ea4-46564be27671',
                                        'cheque_back_time': None,
                                        'statement_month': None,
                                    },
                                    {
                                        'id': '4e48e148-6c37-11ef-8ea5-46564be27671',
                                        'cheque_back_time': None,
                                        'statement_month': None,
                                    },
                                ],
                            },
                        ],
                    },
                    'oc_code': '6849',
                    'appl_systemverifies': [
                        {
                            'id': '1332dc52-a25c-11ef-9f17-43bd561d2667',
                            'kyc': None,
                            'kyc_reason': None,
                            'occode': None,
                            'appl_systemverify_peps': [],
                        },
                    ],
                    'accountlistncbs': [
                        {
                            'id': '0c0bbb94-457b-11ef-940a-46564be27671',
                            'ncb_account_type': 'ncb_account_type',
                            'ncb_account_status': 'Unknown',
                        },
                    ],
                    'segment_id': '78',
                },
            },
            {
                'id': '5529f152-2df6-11ef-a648-3f85ae98e2a2',
                'party_type_id': 'BorrowerIndividual',
                'party': {
                    'id': '55258284-2df6-11ef-a643-3741b1ba10f8',
                    'relationship': None,
                    'income_type': None,
                    'kyc_level_id': None,
                    'kyc_reason_id': None,
                    'rm_kyc_level_id': None,
                    'rm_kyc_reason_id': None,
                    'customer_type_code': None,
                    'appl_guarantees': [
                        {
                            'party_type_id': 'BorrowerIndividual',
                            'party': {
                                'id': '55258284-2df6-11ef-a643-3741b1ba10f8',
                                'personal_infos': [
                                    {
                                        'id': '90505da0-8177-11ef-b366-6bfe2a2d87f8',
                                        'company_title_name_id': None,
                                        'current_job_start_month': None,
                                    },
                                ],
                            },
                        },
                    ],
                    'addresses': [
                        {
                            'id': 'cfc6e84c-2df7-11ef-81fe-179596db4bef',
                            'address_owner': None,
                        },
                    ],
                    'business_infos': [],
                    'cbosdata': [],
                    'personal_infos': [
                        {
                            'customer_type_group_id': None,
                            'dob': '1994-10-03',
                            'id': '90505da0-8177-11ef-b366-6bfe2a2d87f8',
                            'source_of_income': None,
                            'occupation_id': None,
                            'occupation_group_id': None,
                            'monthly_income_declare': None,
                            'nationality_id': None,
                            'staff_id': None,
                            'current_job_start_date': None,
                            'current_job_start_year': None,
                            'monthly_income': None,
                            'company_title_name_id': None,
                            'current_job_start_month': None,
                        },
                    ],
                    'financialinfos': None,
                    'oc_code': None,
                    'appl_systemverifies': [],
                    'accountlistncbs': [
                        {
                            'id': '5526e7b4-2df6-11ef-a644-bf0761732134',
                            'ncb_account_type': None,
                            'ncb_account_status': 'Unknown',
                        },
                    ],
                    'segment_id': None,
                },
            },
            {
                'id': 'cbb4452c-63eb-11ef-904b-46564be27671',
                'party_type_id': 'BorrowerLegalEntity',
                'party': {
                    'id': 'cbac88be-63eb-11ef-9044-46564be27671',
                    'relationship': None,
                    'income_type': None,
                    'kyc_level_id': 1,
                    'kyc_reason_id': 1,
                    'rm_kyc_level_id': None,
                    'rm_kyc_reason_id': None,
                    'customer_type_code': 'P',
                    'appl_guarantees': [],
                    'addresses': [],
                    'business_infos': [
                        {
                            'id': 'cbb21180-63eb-11ef-9048-46564be27671',
                            'income_per_year': None,
                            'create_date_time': '2024-08-27T03:43:05.4184580+07:00',
                        },
                    ],
                    'cbosdata': [
                        {
                            'id': 'cbb0da7c-63eb-11ef-9047-46564be27671',
                            'ncb_grade': None,
                            'cnt_all_tl_delq_mr00336m': None,
                            'cnt_all_tl_delq_ody36m': None,
                            'create_date_time': '2024-08-27T03:43:05.4184580+07:00',
                            'customer_has_negative_status_from_ncb': True,
                            'customer_has_negative_status_mcp_from_ncb': True,
                            'is_debt_payment_completed': True,
                            'customer_has_tdr_from_ncb': True,
                            'cbosdata_juristic_credit_reports': [],
                            'party_cbosdata_listpnsegments': [],
                        },
                    ],
                    'personal_infos': [
                        {
                            'customer_type_group_id': None,
                            'dob': '1994-07-09',
                            'id': 'cbae46b8-63eb-11ef-9046-46564be27671',
                            'source_of_income': None,
                            'occupation_id': None,
                            'occupation_group_id': None,
                            'monthly_income_declare': None,
                            'nationality_id': None,
                            'staff_id': None,
                            'current_job_start_date': None,
                            'current_job_start_year': None,
                            'monthly_income': None,
                            'company_title_name_id': None,
                            'current_job_start_month': None,
                        },
                    ],
                    'financialinfos': {
                        'id': 'c26983b4-7012-11ef-b7d7-46564be27671',
                        'total_income': 120000,
                        'monthly_income': 10000,
                        'estimated_ifs': 9002,
                        'ifs': 9001,
                        'total_other_income': None,
                        'total_borrower_income': None,
                        'total_guarantor_income': None,
                        'total_fixed_income': None,
                        'residual_income': None,
                        'income_freq': None,
                        'total_debt_burden': None,
                        'appl_party_financialinfo_hrms': [],
                        'appl_party_financial_statements': [],
                    },
                    'oc_code': '6888',
                    'appl_systemverifies': [],
                    'accountlistncbs': [
                        {
                            'id': 'cbad5a0a-63eb-11ef-9045-46564be27671',
                            'ncb_account_type': None,
                            'ncb_account_status': 'Unknown',
                        },
                    ],
                    'segment_id': '78',
                },
            },
        ],
        'systemverifies': [
            {
                'id': '6ea3c9b4-8229-11ef-8963-e3af22cee4a1',
                'appl_systemverify_watchlists': [
                    {
                        'id': '64bfac20-50d7-11ef-a2e4-46564be27671',
                        'create_date_time': '2024-08-02T20:59:10.0000000+07:00',
                        'watchlist_lists': [
                            {
                                'id': '64e972bc-50d7-11ef-8c6a-46564be27671',
                                'bkl_type': '1',
                                'bkl_subtype': '22',
                                'bkl_degree': 'W99',
                                'create_date_time': '2024-08-02T20:59:11.0000000+07:00',
                            },
                            {
                                'id': '64e976ea-50d7-11ef-8c6b-46564be27671',
                                'bkl_type': '5',
                                'bkl_subtype': '25',
                                'bkl_degree': 'W10',
                                'create_date_time': '2024-08-02T20:59:11.0000000+07:00',
                            },
                        ],
                    },
                ],
                'appl_systemverify_cdds': [
                    {
                        'id': '0c421ce6-65c6-11ef-91c1-46564be27671',
                        'appl_systemverify_cdd_alerts': [
                            {
                                'id': '0c421ce6-65c6-11ef-91c1-46564be27671',
                                'cdd_seq': 1,
                                'message': 'Message 1',
                                'create_date_time': '2023-10-26T10:00:00.0000000+07:00',
                            },
                        ],
                    },
                ],
                'appl_systemverify_frauds': [
                    {
                        'id': '79e11990-822d-11ef-b456-3f63c2fa71c5',
                        'found_status': 'Found',
                        'is_validate_person': None,
                        'create_date_time': '2024-10-04T15:48:50.0000000+07:00',
                    },
                    {
                        'id': '4a399fd6-822e-11ef-9a66-bba8a467a309',
                        'found_status': 'Found',
                        'is_validate_person': None,
                        'create_date_time': '2024-10-04T15:54:39.0000000+07:00',
                    },
                    {
                        'id': '3bee4e9a-822e-11ef-83c2-0f86bbe503bc',
                        'found_status': 'Found',
                        'is_validate_person': None,
                        'create_date_time': '2024-10-04T15:54:15.0000000+07:00',
                    },
                    {
                        'id': '4719ca3c-822f-11ef-9d89-bb24570c3f8c',
                        'found_status': 'Found',
                        'is_validate_person': None,
                        'create_date_time': '2024-10-04T16:01:43.0000000+07:00',
                    },
                ],
                'appl_systemverify_peps': [
                    {
                        'id': '45ecbd7a-4f2d-11ef-a5b0-46564be27671',
                        'appl_systemverify_pep_lists': [
                            {
                                'id': '8a16699e-64f7-11ef-aa1d-46564be27671',
                            },
                        ],
                    },
                ],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [
                    {
                        'id': '45d2b724-822f-11ef-8e15-e7b8d135357c',
                        'appl_systemverify_rmservice_products': [
                            {
                                'id': '70c0de2a-8b71-11ef-9f72-274057323e31',
                                'appl_systemverify_rmservice_cardproducts': [
                                    {
                                        'id': 'b9a102e2-7bc1-11ef-9ea9-26f16a5dcb9c',
                                        'card_status': 'C',
                                    },
                                ],
                            },
                        ],
                    },
                ],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3cffe-8229-11ef-8964-239a973e20ed',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [
                    {
                        'id': '832fb938-8229-11ef-bbb6-9bd548d807a2',
                        'appl_systemverify_rmservice_products': [],
                    },
                ],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3d076-8229-11ef-8965-7387b6234667',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3d166-8229-11ef-8968-8f708ce06a2a',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3d97c-8229-11ef-8969-8380adb42a6e',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': '3903',
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3da12-8229-11ef-896a-73b3c3faa76c',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3da80-8229-11ef-896b-03d2d345c4b6',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3daf8-8229-11ef-896c-5306cf8ed079',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3d0d0-8229-11ef-8966-4bb69d9b44b5',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3d120-8229-11ef-8967-479410a63999',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3db70-8229-11ef-896d-6320d04f0a61',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3dbc0-8229-11ef-896e-8bc979a96d23',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3dc10-8229-11ef-896f-bb0be49898cd',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '6ea3dc60-8229-11ef-8970-87b2d61fd5ef',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': '4',
                'rm_kyc_reason': '321',
                'occode': None,
                'create_date_time': '2024-10-04T15:19:53.0000000+07:00',
            },
            {
                'id': '1332dc52-a25c-11ef-9f17-43bd561d2667',
                'appl_systemverify_watchlists': [],
                'appl_systemverify_cdds': [],
                'appl_systemverify_frauds': [],
                'appl_systemverify_peps': [],
                'appl_systemverify_relateds': [],
                'appl_systemverify_rmservices': [],
                'rm_kyc': None,
                'rm_kyc_reason': None,
                'occode': None,
                'create_date_time': '2024-07-12T13:06:52.0000000+07:00',
            },
        ],
        'saleinfos': [
            {
                'id': '0f962e6c-5556-11ef-821c-46564be27671',
                'staff_type': 'Owner',
            },
            {
                'id': '50e53954-54a1-11ef-bdd6-46564be27671',
                'staff_type': 'Owner',
            },
            {
                'id': '6e4402b4-54a1-11ef-91b6-46564be27671',
                'staff_type': 'Owner',
            },
            {
                'id': 'fb8a1030-54a3-11ef-be61-46564be27671',
                'staff_type': 'Owner',
            },
        ],
        'breInput': [
            {
                'id': '252ac5a8-522c-11ef-8a4c-46564be27671',
                'age_in_months': 280,
                'total_ltav': 85246,
            },
        ],
        'authorizationInfo': [
            {
                'id': '11e6ce70-700d-11ef-ad32-46564be27671',
                'dscr': 15,
                'auth_dscr': None,
                'mlscoreinfo_mlgroups': [
                    {
                        'id': '27037782-70ca-11ef-b337-46564be27671',
                        'ml_grade': 'A',
                        'ml_score': None,
                        'create_date_time': None,
                    },
                ],
                'ncb_grade': 'C',
                'create_date_time': '2024-09-11T14:11:30.8923790+07:00',
            },
            {
                'id': '11e6ea5e-700d-11ef-ad33-46564be27671',
                'dscr': 100,
                'auth_dscr': 1,
                'mlscoreinfo_mlgroups': [
                    {
                        'id': '33b08cf4-70ca-11ef-b338-46564be27671',
                        'ml_grade': 'B',
                        'ml_score': None,
                        'create_date_time': None,
                    },
                ],
                'ncb_grade': 'A',
                'create_date_time': '2024-09-11T14:11:30.8923790+07:00',
            },
        ],
        'mfappl_generalinfo': [
            {
                'application_id': 'APP191000101V',
                'prefinance_from_scb': 'yes',
            },
        ],
        'appl_cpgguideline': [
            {
                'id': '18403f74-8c4e-11ef-9e04-7f74929dbf8a',
                'in_cpg_condition_flag': 'Y',
                'risk_level': 'A',
            },
        ],
        'mfappl_appraisalworkdetails_collateralitems_basecollatdetls': [
            {
                'located_in_city': True,
            },
        ],
        'appl_qc_vehicle_info': [
            {
                'application_id': 'APP191000101V',
                'confirmed_selling_price': 12332,
                'rb_price': 12330,
                'up_price_percent': 13,
                'id': '20d7488e-7f9d-11ef-97fc-430892e8a7a8',
            },
            {
                'application_id': 'APP191000101V',
                'confirmed_selling_price': 12332,
                'rb_price': 12330,
                'up_price_percent': 13,
                'id': 'cc3d0900-7620-49e2-b4bb-b128e0ea1010',
            },
        ],
        'appl_financialinfo': [
            {
                'total_borrower_guarantor_income': 1230023,
                'total_insurance_premium_amount': 0,
                'total_dsr': 8.59,
                'dsr_ex_insurance': 0,
                'insurance_dsr': 8.59,
                'total_guarantor_income': 0,
                'id': 'ee4f74b0-4b56-11ef-8151-9f5c3c43bc16',
            },
        ],
        'appl_collateral_realestate': [
            {
                'appraisal_value': None,
                'land_appraisal_value': None,
                'id': '58f39826-561c-11ef-ad0b-46564be27671',
                'collateral_type': 'LAND',
                'type_of_building': '5',
                'create_date_time': '2024-08-09T13:55:22.3131500+07:00',
            },
            {
                'appraisal_value': None,
                'land_appraisal_value': None,
                'id': '1c0a9206-9b23-11ef-bbd1-e35725f6704e',
                'collateral_type': '1100',
                'type_of_building': None,
                'create_date_time': '2024-11-05T10:07:36.8317980+07:00',
            },
            {
                'appraisal_value': None,
                'land_appraisal_value': None,
                'id': '9e4916f0-9cec-11ef-a106-dfba262600de',
                'collateral_type': '0111',
                'type_of_building': None,
                'create_date_time': '2024-11-07T16:42:35.3468140+07:00',
            },
        ],
        'appl_collateral_security': [
            {
                'id': '89061efc-44e3-11ef-b173-46564be27672',
                'is_owner_same_borrower': True,
                'create_date_time': '2024-07-04T03:52:30.3495870+07:00',
            },
            {
                'id': 'a046460a-9b1e-11ef-a399-372aac24cfb4',
                'is_owner_same_borrower': None,
                'create_date_time': '2024-11-05T09:35:31.2004250+07:00',
            },
        ],
        'appl_guarantee': [
            {
                'id': '1505e65e-50aa-11ef-9e0e-46564be27671',
            },
            {
                'id': '03a336fc-2498-11ef-acdd-bb04205cf958',
            },
        ],
    },
}
    return json_data

def trigger_decision_engine(input_arr, use_data_directly=False):
    wf_name, wf_version, wf_revision, external_id, data_input, http_headers = input_arr

    response = requests.post(
        f'https://ms.nleadsdev.se.scb.co.th/runtime/api/process?workflowType=Process&workflowName={wf_name}&workflowVersion={wf_version}&workflowRevision={wf_revision}&externalId={external_id}&externalSystemCode=ms-invoke&settingsProfile=Default&uiRequest=true&scriptingRuntime=',
        headers=http_headers,
        json=get_data(data_input) if not use_data_directly else data_input
    )

    return response

def generate_output(index, input_json, response_json):
    print(input_json)
    print("========================================")
    print(response_json)
    print("\n")

    request_id, workflow_output = response_json["RequestId"], response_json["WorkflowOutput"]
    url = f'https://console.nleadsdev.se.scb.co.th/#/report/modern/process/{request_id}?workspace=default'
    return [index, json.dumps(input_json), json.dumps(workflow_output), url]



# Execution 
# ==========================================================================================
def orchestrate_execution(input_arr, generate_testcases=True, use_data_directly=False):
    wf_name, version, revision, id, data_inputs, auth_token, excel_folder, *_= input_arr + [None]*3
    http_headers, external_id = setup_params(auth_token, id)

    output_agg = []
    print(data_inputs)
    for row_no, data_input in enumerate(data_inputs, 1):
        response= trigger_decision_engine([wf_name, version, revision, external_id, data_input, http_headers], use_data_directly)
        print(response)
        out = generate_output(row_no, data_input, response.json())
        output_agg.append(out)

    if generate_testcases:
        excel_header_cols = [
            'Test Case No', 
            'Input', 
            'Output', 
            f'Report Link for {wf_name} [DEV ENV]'
        ]
        filepath = os.path.join(os.getcwd(), excel_folder, f'TestCase-{PROCESS_WF_NAME}.xlsx')
        write_preprocess_testcases(filepath, excel_header_cols, output_agg)

    return output_agg


def setup_params(auth_token, id):
    http_headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': auth_token,
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
    external_id = f"{id}-{date.today()}"
    return http_headers, external_id


if __name__ == "__main__": 
    # CONSTANTS
    PROCESS_WF_NAME = 'UW_GuarantorKYC3AUTO_Preprocess'
    WF_VERSION=0
    WF_REVISION=5
    ID='sadeepthab'
    FOLDERNAME = 'data'
    DATA_INPUTS = [{'KYCLevel': 3, 'KYCReason': 307, 'Occupation': 56, 'KYCLevelRM': 3, 'KYCReasonRM': 311}, {'KYCLevel': 3, 'KYCReason': 300, 'Occupation': 88, 'KYCLevelRM': 3, 'KYCReasonRM': 321}, {'KYCLevel': 3, 'KYCReason': 310, 'Occupation': 47, 'KYCLevelRM': 5, 'KYCReasonRM': 301}, {'KYCLevel': 3, 'KYCReason': 313, 'Occupation': 74, 'KYCLevelRM': 3, 'KYCReasonRM': 317}, {'KYCLevel': 2, 'KYCReason': 315, 'Occupation': 44, 'KYCLevelRM': 3, 'KYCReasonRM': 306}, {'KYCLevel': 3, 'KYCReason': 317, 'Occupation': 50, 'KYCLevelRM': 3, 'KYCReasonRM': 315}, {'KYCLevel': 5, 'KYCReason': 303, 'Occupation': 83, 'KYCLevelRM': 3, 'KYCReasonRM': 315}, {'KYCLevel': 3, 'KYCReason': 315, 'Occupation': 95, 'KYCLevelRM': 5, 'KYCReasonRM': 318}, {'KYCLevel': 5, 'KYCReason': 319, 'Occupation': 53, 'KYCLevelRM': 3, 'KYCReasonRM': 316}]
    
    # EPHYMERAL CONSTANTS (Changing per execution)
    AUTH_TOKEN='Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJfcXFNcnNjMGZ2YmlOVFkxVGMtSEJQX2tpLVpwSDZ3X0R0SGJONVFMcnBjIn0.eyJleHAiOjE3MzM0ODI5NzgsImlhdCI6MTczMzQ4MTE3OCwiYXV0aF90aW1lIjoxNzMzNDU4NTYzLCJqdGkiOiI5YjRjMDIwNS0yZTgxLTQwNGMtYWRlNi1hNmVjNzFiNTRhOGUiLCJpc3MiOiJodHRwczovL2tleWNsb2FrLm5sZWFkc2Rldi5zZS5zY2IuY28udGgvcmVhbG1zL25sZWFkcy1kZXYiLCJhdWQiOlsibXMta2V5Y2xvYWsiLCJiYWNrb2ZmaWNlIiwiYWNjb3VudCJdLCJzdWIiOiIzNmUwNTVlMC05YjYxLTRlNTEtYjA1MC05ZWZjOWM0ZTk5MTAiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJjb25zb2xlIiwic2lkIjoiMTI3MzA3ODktNjZmNy00ZjRmLTlmN2QtZTUwYzAyZTAyZjA2IiwiYWNyIjoiMCIsInNjb3BlIjoiZW1haWwgZGF0YXByb3ZpZGVycyBvcGVuaWQgbW9kZWxzIHByb2ZpbGUgYWNyIGNvbmZpZ3VyYXRpb25BcGkgYXVkaXQgdXNlcmRhdGEiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicm9sZSI6WyJEZWNpc2lvbkVuZ2luZVdvcmtmbG93RWRpdG9yIiwiZGVmYXVsdC1yb2xlcy1tYXN0ZXIiLCJHcmFmYW5hQWRtaW5pc3RyYXRvciIsIkRlY2lzaW9uRW5naW5lUHJvdGVjdGVkRGF0YVZpZXdlciIsIkFEV0FkbWluaXN0cmF0b3IiLCJEZWNpc2lvbkVuZ2luZVJlcG9ydFZpZXdlciIsIkRlY2lzaW9uRW5naW5lUmVjb3ZlcnlNYW5hZ2VyIiwiRGVjaXNpb25FbmdpbmVBdWRpdFZpZXdlciIsIkFkbWluaXN0cmF0b3IiLCJEZWNpc2lvbkVuZ2luZVdvcmtmbG93U2lnbmVyIiwiRGVjaXNpb25FbmdpbmVXb3JrZmxvd0V4ZWN1dG9yIiwib2ZmbGluZV9hY2Nlc3MiLCJCT1VzZXIiLCJ1bWFfYXV0aG9yaXphdGlvbiIsIkRlY2lzaW9uRW5naW5lV29ya2Zsb3dWaWV3ZXIiXSwibmFtZSI6InNhZGVlcHRoYS5iYW5kYXJhQHpvcmFsbGFicy5jb20iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJzYWRlZXB0aGEuYmFuZGFyYUB6b3JhbGxhYnMuY29tIiwiZW1haWwiOiJzYWRlZXB0aGEuYmFuZGFyYUB6b3JhbGxhYnMuY29tIn0.Mvfv9J54Wo_YzytZOLiru3Wn7zWf0yCCKFa-33qXn-2ZW61dUsg7svhg-88e-RgAip-k6eJ5K316zn1-82DtjuC2YbRyGbZezTFI500zqKK5DhbBuVVf8ef3EM_mr85PXUojNV-i9FlepVID3rITvPs96mgV8rWQPWkNXmayXrm8asqaBMZIbi5p-O6Sx5SSxMpYjXoJBPeRSlvy1fjJa509-Ml6D38Rhk0k3TLHt0uU6yC_XH4wQypnIed_QtxSAkSG23_1fEpbnwI6VcLgzhtrsyK0qaUDnLOzuYFDdVS3BQB68SttLzYdTAXt4KtdvBmo335cy-LKtdMXfQ5Nsg'
    EXTERNAL_ID=f"{ID}-{date.today()}"
  

    output = orchestrate_execution(['NGL_AutoProcess_GetDependentADWData', 0, 221, EXTERNAL_ID, [{"applicationId": "APP191000101V"}], AUTH_TOKEN, FOLDERNAME], generate_testcases=False, use_data_directly=True)
    
    # with open()
    # Save output to a file

    # orchestrate_execution([PROCESS_WF_NAME, WF_VERSION, WF_REVISION, ID, DATA_INPUTS, AUTH_TOKEN, FOLDERNAME])

    
    







