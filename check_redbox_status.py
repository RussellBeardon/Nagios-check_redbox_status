

#!/usr/bin/python
'''
check_redbox.py

Author =  Russell Beardon
Date = 10/10/2017

requires pysnmp,sys

USAGE
    check_redbox.py target community
'''
import sys

# VARIABLES

# get from command line arguments
target = sys.argv[1]
community = sys.argv[2]

oid = "1.3.6.1.4.1.9854.2.3.0"

# FUNCTIONS
def snmp_get (oid,target,community = "public"):
    from pysnmp.entity.rfc3413.oneliner import cmdgen

    cmdGen = cmdgen.CommandGenerator()

    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((target, 161)),
        oid
    )

    # Check for errors and print out results
    if errorIndication:
        return(errorIndication)
    else:
        if errorStatus:
            return('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
                )
            )
        else:
            for name, val in varBinds:
                return(val);
result = snmp_get(community = community, oid=oid, target=target)
# exit with success
if result == 1:
    print ("OK - SNMP returned value of 1:RECORDING")
    exit(0)
elif result > 1:
    if result == 2:
        status = "PANIC"
    elif result == 3:
        status = "BROKEN"
    elif result == 4:
        status = "NOT LICENSED"
    elif result == 5:
        status = "REPLAY ONLY"
    elif result == 6:
        status = "NO CALL STORE"
    elif result == 7:
        status = "STANDBY"
    elif result == 8:
        status = "RESUME AVAILABLE"
    elif result == 9:
        status = "SLAVE RESUMING STANDBY"
    elif result == 10:
        status = "NAS RECOVERY"
    else:
        status = "UNKNOWN ERROR";

    print "CRITICAL - Error {}".format(result)
    print result
    exit(2);

print(result)

