import datetime

test_get_subscribe_info_by_exchange_class_var = {
  "MaterialClassifiers_Export": [
    "Test_integr",
    "IUSMTR"
  ],
  "Materials_Export": [
    "IUSPP",
    "Test_integr",
    "IUSMTR",
    "IUSI"
  ],
  "RegulationDocs_Export": [
    "IUSMTR"
  ],
  "conversionFactors_Export": [
    "Test_integr",
    "IUSMTR"
  ]
}
request_ids = 'autotest_request_ids'
item_ids = 'autotest_item_id'
assertion_success = ('autotest_request_ids', datetime.datetime(1111, 11, 11, 11, 11, 11, 111000), 'autotest_item_id', 'SUCCESS', None)
assertion_waiting = ('autotest_request_ids', datetime.datetime(1111, 11, 11, 11, 11, 11, 111000), 'autotest_item_id', 'WAITING', None)
assertion_waitings = ('autotest_request_ids', datetime.datetime(1111, 11, 11, 11, 11, 11, 111000), 'autotest_item_id', 'WAITING', None)