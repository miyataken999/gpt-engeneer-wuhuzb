from fastapi import APIRouter, HTTPException
from .crud import create_team, get_teams, get_team
from .schemas import TeamCreate, TeamRead

router = APIRouter()

@router.post("/teams/")
async def create_team_endpoint(team: TeamCreate):
    return create_team(db, team)

@router.get("/teams/")
async def read_teams():
    return get_teams(db)

@router.get("/teams/{team_id}")
async def read_team(team_id: int):
    return get_team(db, team_id)