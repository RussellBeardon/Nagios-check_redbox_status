# Nagios-check_redbox_status
Nagios plugin to check the recorder status of a RedBox Recorder system

Requires Python, pySNMP library installed on Nagios server.

Redbox SNMP service needs to be running on the RedBox Recorder.

INSTRUCTIONS FOR USER

1. Insert check_redbox_status.py into libexec folder

2. Add Nagios Command, $USER4$ is the SNMP community for the Redbox

define command {
        command_name    check_redbox_status
        command_line    /bin/python $USER1$/check_redbox_status.py $HOSTNAME$ $USER4$
        }

3. Add service to host definition 

define service {
        hostgroup    redbox
        use     windows_extra_service
        service_description     Redbox recorder status
        check_command check_redbox_status
        }

