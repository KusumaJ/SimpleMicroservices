from __future__ import annotations

from typing import Optional, List, Annotated
from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, Field

from .coursework import CourseworkBase

class AssignmentBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Persistent Assignment ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    title: str = Field(
        ...,
        description="Title of the assignment.",
        json_schema_extra={"example": "Assignment 1"},
    )
    description: str = Field(
        ...,
        description="Description of the assignment.",
        json_schema_extra={"example": "Complete the cloud computing project."},
    )
    due_date: date = Field(
        ...,
        description="Due date for the assignment.",
        json_schema_extra={"example": "2025-12-31"},
    )
    coursework: CourseworkBase = Field(
        ...,
        description="Coursework associated with this assignment.",
        json_schema_extra={
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "title": "Cloud Computing",
                "semester": "Fall 2025",
                "professor": {
                    "uni": "df123",
                    "first_name": "Donald",
                    "last_name": "Ferguson",
                    "email": "donald.ferguson@cs.columbia.edu",
                }
            }
        }
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "title": "Assignment 1",
                    "description": "Complete the cloud computing project.",
                    "due_date": "2025-12-31",
                    "coursework": {
                        "id": "550e8400-e29b-41d4-a716-446655440001",
                        "title": "Cloud Computing",
                        "semester": "Fall 2025",
                        "professor": {
                            "uni": "df123",
                            "first_name": "Donald",
                            "last_name": "Ferguson",
                            "email": "donald.ferguson@cs.columbia.edu",
                        }
                    },
                    "created_at": "2025-01-15T10:20:30Z"
                }
            ]
        }
    }


class AssignmentCreate(AssignmentBase):
    """Creation payload for an Assignment."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Assignment 1",
                    "description": "Complete the cloud computing project.",
                    "due_date": "2025-12-31",
                    "coursework": {
                        "id": "550e8400-e29b-41d4-a716-446655440001",
                        "title": "Cloud Computing",
                        "semester": "Fall 2025",
                        "professor": {
                            "uni": "df123",
                            "first_name": "Donald",
                            "last_name": "Ferguson",
                            "email": "donald.ferguson@cs.columbia.edu",
                        }
                    }
                }
            ]
        }
    }

class AssignmentUpdate(BaseModel):
    """Partial update for an Assignment; supply only fields to change."""
    id: Optional[UUID] = Field(
        default_factory=uuid4,
        description="Persistent Assignment ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    title: Optional[str] = Field(
        None,
        description="Title of the assignment.",
        json_schema_extra={"example": "Assignment 1"},
    )
    description: Optional[str] = Field(
        None,
        description="Description of the assignment.",
        json_schema_extra={"example": "Complete the cloud computing project."},
    )
    due_date: Optional[date] = Field(
        None,
        description="Due date for the assignment.",
        json_schema_extra={"example": "2025-12-31"},
    )
    coursework: Optional[CourseworkBase] = Field(
        None,
        description="Coursework associated with this assignment.",
        json_schema_extra={
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "title": "Cloud Computing",
                "semester": "Fall 2025",
                "professor": {
                    "uni": "df123",
                    "first_name": "Donald",
                    "last_name": "Ferguson",
                    "email": "donald.ferguson@cs.columbia.edu",
                }
            }
        }
    )
    created_at: Optional[datetime] = Field(
        None,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Assignment 1",
                    "description": "Complete the cloud computing project.",
                    "due_date": "2025-12-31",
                    "coursework": {
                        "id": "550e8400-e29b-41d4-a716-446655440001",
                        "title": "Cloud Computing",
                        "semester": "Fall 2025",
                        "professor": {
                            "uni": "df123",
                            "first_name": "Donald",
                            "last_name": "Ferguson",
                            "email": "donald.ferguson@cs.columbia.edu",
                        }
                    }
                }
            ]
        }
    }
    
    


class AssignmentRead(AssignmentBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Assignment ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Assignment 1",
                    "description": "Complete the cloud computing project.",
                    "due_date": "2025-12-31",
                    "coursework": {
                        "id": "550e8400-e29b-41d4-a716-446655440001",
                        "title": "Cloud Computing",
                        "semester": "Fall 2025",
                        "professor": {
                            "uni": "df123",
                            "first_name": "Donald",
                            "last_name": "Ferguson",
                            "email": "donald.ferguson@cs.columbia.edu",
                        }
                    }
                }
            ]
        }
    }