import os
from pprint import pprint

from SpiffWorkflow.bpmn.parser.BpmnParser import BpmnParser
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow


def run_flow():
    # Load BPMN File
    filename = "test-bpmn-flow.bpmn"
    pprint('== Load BPMN : {filename} =='.format(filename=filename))
    parser = BpmnParser()
    parser.add_bpmn_files([filename])
    workflow = BpmnWorkflow(parser.get_spec("Process_1"))

    # Start Process
    pprint('== Start Process : {process} =='.format(process=workflow.name))
    workflow.do_engine_steps()

    # Complete Task A (Multi-Instance)
    ready_tasks = workflow.get_ready_user_tasks()
    for task in ready_tasks:
        pprint('== Complete Task : {task} =='.format(task=task.task_spec.name))
        task.update_data({'approved': False})
        task.complete()
        workflow.do_engine_steps()

    # Complete Task B1
    ready_tasks = workflow.get_ready_user_tasks()
    for task in ready_tasks:
        pprint('== Complete Task : {task} =='.format(task=task.task_spec.name))
        task.complete()
        workflow.do_engine_steps()

    # Complete Task B2
    ready_tasks = workflow.get_ready_user_tasks()
    for task in ready_tasks:
        pprint('== Complete Task : {task} =='.format(task=task.task_spec.name))
        task.complete()
        workflow.do_engine_steps()


if __name__ == '__main__':
    run_flow()
