errMessage ="""\'
Error: Exception occurred while invoking job with run number 5768: Exception('* 10001: user-defined error:  [10001] "OPS_SCHEMA"."AM.JOB_SCHEDULER.PROCEDURES::PR_INVOKE_JOB": line 33 col 4 (at pos 1138): [10001] (range 3) user-defined error exception: user-defined error 10001] "VSSOD_SCHEMA"."DUMMY_JOB_WITH_7MIN_EXCEP": line 19 col 2 (at pos 526): [10001] (range 3) user-defined error exception: This is a forced custom exception with delay of 7min from invocation SQLSTATE: HY000\r\n',)\'"""
errMessage =errMessage.replace('\"', '')
errMessage =errMessage.replace('\'', '')
errMessage =errMessage.replace('\`', '')
print errMessage