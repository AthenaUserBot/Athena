from git import Repo  
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError # Thx To Seden Team

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), 'requirements.txt'
)


def gen_chlog(repo, diff):
    ch_log = ''
    d_form = '%d/%m/%y'
    for c in repo.iter_commits(diff):
        ch_log += f'%1•%1  %2[{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>%2\n'
    return ch_log


def update_requirements():
    reqs = str(requirements_path)
    try:
        _, ret = execute_command(f'{executable} -m pip install -r {reqs}')
        return ret
    except Exception as e:
        return repr(e)
