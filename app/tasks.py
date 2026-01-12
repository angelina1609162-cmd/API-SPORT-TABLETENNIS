from .celery_app import celery_app
@celery_app.task
def fetch_and_save_player(player_name, max_matches=20):
    return {"status":"ok","player":player_name}
