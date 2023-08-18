"""

"""


import phantom.rules as phantom
import json
from datetime import datetime, timedelta


@phantom.playbook_block()
def on_start(container):
    phantom.debug('on_start() called')

    # call 'send_email_1' block
    send_email_1(container=container)

    return

@phantom.playbook_block()
def send_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug("send_email_1() called")

    # phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    playbook_input_to = phantom.collect2(container=container, datapath=["playbook_input:to"])
    playbook_input_body = phantom.collect2(container=container, datapath=["playbook_input:body"])
    playbook_input_from = phantom.collect2(container=container, datapath=["playbook_input:from"])
    playbook_input_subject = phantom.collect2(container=container, datapath=["playbook_input:subject"])

    parameters = []

    # build parameters list for 'send_email_1' call
    for playbook_input_to_item in playbook_input_to:
        for playbook_input_body_item in playbook_input_body:
            for playbook_input_from_item in playbook_input_from:
                for playbook_input_subject_item in playbook_input_subject:
                    if playbook_input_to_item[0] is not None and playbook_input_body_item[0] is not None:
                        parameters.append({
                            "to": playbook_input_to_item[0],
                            "body": playbook_input_body_item[0],
                            "from": playbook_input_from_item[0],
                            "subject": playbook_input_subject_item[0],
                        })

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.act("send email", parameters=parameters, name="send_email_1", assets=["smtp"])

    return


@phantom.playbook_block()
def on_finish(container, summary):
    phantom.debug("on_finish() called")

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################

    return