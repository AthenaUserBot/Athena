from athena.func import extract_text

from athena import UPSTREAMREPO, HEROKUAPIKEY, HEROKUAPP

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

@muinrobot(pattern='^.update')
async def updater(ups):
    conf = await extract_text(ups)
    off_repo = UPSTREAMREPO
    force_update = False
    repo = None

    try:
        txt = "`Güncelleme başarısız oldu! Bazı sorunlarla karşılaştık.`\n\n**LOG:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await ups.edit_text(f'"NOT_FOUND"')
        repo.__del__()
        return
    except GitCommandError as error:
        await ups.edit_text('"GIT_ERROR"')
        repo.__del__()
        return
    except InvalidGitRepositoryError as error:
        if conf != 'now':
            await ups.edit_text('update git not found')
            return
        repo = Repo.init()
        origin = repo.create_remote('upstream', off_repo)
        origin.fetch()
        force_update = True
        repo.create_head('master', origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != 'master':
        await ups.edit_text('INVALID BRANCH')
        repo.__del__()
        return

    try:
        repo.create_remote('upstream', off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote('upstream')
    ups_rem.fetch(ac_br)

    changelog = gen_chlog(repo, f'HEAD..upstream/{ac_br}')
    if not changelog and not force_update:
        await ups.edit_text('Güncelleme bulunamadı!')
        repo.__del__()
        return

#    if conf != "now" and not force_update:

    if force_update:
        await ups.edit_text('**Zorla Güncelleniyor..**')
    else:
        await ups.edit_text('**Güncelleniyor..**')

    if HEROKUAPIKEY is not None:
        import heroku3
        heroku = heroku3.from_key(HEROKUAPIKEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not HEROKUAPP:
            await ups.edit_text('INVALID HEROKU APPNAME')
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKUAPP:
                heroku_app = app
                break
        if heroku_app is None:
            await ups.edit(
                'INVALID HEROKU'
            )
            repo.__del__()
            return
        await ups.edit_text('**Heroku üzerinde güncelleniyor..**')
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKUAPIKEY + "@")
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except GitCommandError as error:
            await ups.edit_text(f'{txt}\n`ERROR:\n{error}`')
            repo.__del__()
            return
        await ups.edit_text('💕 Güncelleme başarıyla tamamlandı!')

    else:
        # Klasik güncelleyici, oldukça basit.
        try:
            ups_rem.pull(ac_br)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await update_requirements()
        await ups.edit_text('💕 Güncelleme başarıyla tamamlandı!')
        # Bot için Heroku üzerinde yeni bir instance oluşturalım.
        args = [sys.executable, "brighteninglotion.py"]
        execle(sys.executable, *args, environ)
        return

