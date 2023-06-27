from aeneas.executetask import ExecuteTask
from aeneas.task import Task, TaskConfiguration
from aeneas.textfile import TextFileFormat
from aeneas.language import Language
import aeneas.globalconstants as gc


def get(audioPath: str, textPath: str) -> list:
    config = TaskConfiguration()
    config[gc.PPN_TASK_LANGUAGE] = Language.ENG
    config[gc.PPN_TASK_IS_TEXT_FILE_FORMAT] = TextFileFormat.PLAIN

    # create Task object
    task = Task()
    task.configuration = config

    task.audio_file_path_absolute = audioPath
    task.text_file_path_absolute = textPath

    # process Task
    ExecuteTask(task).execute()

    return task.sync_map.leaves()
