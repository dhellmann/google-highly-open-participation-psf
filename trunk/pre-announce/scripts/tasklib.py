import os

class Task:
    def __init__(self, summary, descr, tags, owner):
        self.summary = summary
        self.descr = descr
        self.tags = tags
        self.owner = owner

    def __repr__(self):
        return "Task: '%s'" % (self.summary,)

def load_task_from_file(filename):
    global_d = {}
    local_d = {}
    
    try:
        execfile(filename, global_d, local_d)
    except:
        pass

    if local_d.get('ignore', False):
        print 'ignoring:', filename
        return

    summary = local_d['summary'].strip()
    description = local_d['description'].strip()
    tags = set(local_d['tags'].split(','))
    owner = local_d['owner'].strip()

    task = Task(summary, description, tags, owner)
    return task

def gather_tasks(startdir):
    tasks = set()
    
    startdir = os.path.abspath(startdir)

    for (dirpath, dirnames, filenames) in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.txt'):
                fullpath = os.path.join(dirpath, filename)
                task = load_task_from_file(fullpath)
                if task:
                    tasks.add(task)

    return tasks
