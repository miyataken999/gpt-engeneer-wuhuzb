from sqlalchemy.orm import Session
from .models import Team
from .schemas import TeamCreate, TeamRead

def create_team(db: Session, team: TeamCreate):
    db_team = Team(name=team.name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def get_teams(db: Session):
    return db.query(Team).all()

def get_team(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()