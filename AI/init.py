from AI.modelingUtil import run_model_task, update_task_status
from DB.DBconfig import output_table, queue_table
from scheduling.loadToDB import get_pending_task

def run_model(model):
    # 대기 중인 작업을 처리하는 로직 구현
    try:
        task = get_pending_task()
        if task:
            task_id, task_data = task
            result = run_model_task(task_data, model)   
            
            # 상태를 확인하여 COMPLETE일 경우 삭제
            if result:
                queue_table.child(task_id).delete()
                print(f"Task {task_id} deleted from queue.")
            else:
                # Failed -> PENING으로 재등록
                print(f"Task {task_id} was not deleted; current status: {task_data.get('status')}")        
                update_task_status(task_data['task_id'], "PENDING")

    except Exception as e:
        print(f"Error processing tasks: {e}")
