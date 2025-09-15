from __future__ import annotations

from typing import Optional, List, Annotated
from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, Field

from .person import PersonBase

class CourseworkBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Persistent Coursework ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )
    title: str = Field(
        ...,
        description="Title of the coursework.",
        json_schema_extra={"example": "Cloud Computing"},
    )

    semester: str = Field(
        ...,
        description="Latest semester when the coursework is offered.",
        json_schema_extra={"example": "Fall 2025"},
    )

    professor: PersonBase = Field(
        ...,
        description="Professor overseeing the coursework (carries a persistent uni).",
        json_schema_extra={
            "example": {
                "uni": "df123",
                "first_name": "Donald",
                "last_name": "Ferguson",
                "email": "donald.ferguson@cs.columbia.edu",
            }
        }
    )

    people: List[PersonBase] = Field(
        default_factory=list,
        description="People linked to this coursework (each carries a persistent uni).",
        json_schema_extra={
            "example": [
                {
                    "uni": "abc1234",
                    "first_name": "Ada",
                    "last_name": "Lovelace",
                    "email": "ada@example.com",
                    "addresses": [
                        {
                            "id": "550e8400-e29b-41d4-a716-446655440000",
                            "street": "123 Main St",
                            "city": "London",
                            "state": None,
                            "postal_code": "SW1A 1AA",
                            "country": "UK",
                        }
                    ]
                }
            ]
        },
    )


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Cloud Computing",
                    "semester": "Fall 2025",
                    "professor": {
                        "uni": "df123",
                        "first_name": "Donald",
                        "last_name": "Ferguson",
                        "email": "donald.ferguson@cs.columbia.edu",
                    },
                    "people": [
                        {
                            "uni": "abc1234",
                            "first_name": "Ada",
                            "last_name": "Lovelace",
                            "email": "ada.lovelace@example.com",
                            "addresses": [
                                {
                                    "id": "550e8400-e29b-41d4-a716-446655440000",
                                    "street": "123 Main St",
                                    "city": "London",
                                    "state": None,
                                    "postal_code": "SW1A 1AA",
                                    "country": "UK",
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }


class CourseworkCreate(CourseworkBase):
    """Creation payload for a Coursework."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Cloud Computing",
                    "semester": "Fall 2025",
                    "professor": {
                        "uni": "df123",
                        "first_name": "Donald",
                        "last_name": "Ferguson",
                        "email": "donald.ferguson@cs.columbia.edu",
                    },
                    "people": [
                        {
                            "uni": "abc1234",
                            "first_name": "Ada",
                            "last_name": "Lovelace",
                            "email": "ada.lovelace@example.com",
                            "addresses": [
                                {
                                    "id": "550e8400-e29b-41d4-a716-446655440000",
                                    "street": "123 Main St",
                                    "city": "London",
                                    "state": None,
                                    "postal_code": "SW1A 1AA",
                                    "country": "UK",
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }

class CourseworkUpdate(BaseModel):
    """Partial update for a Coursework; supply only fields to change."""
    title: Optional[str] = Field(
        None,
        description="New title of the coursework.",
        json_schema_extra={"example": "Advanced Cloud Computing"},
    )
    semester: Optional[str] = Field(
        None,
        description="New semester when the coursework is offered.",
        json_schema_extra={"example": "Spring 2026"},
    )
    professor: Optional[PersonBase] = Field(
        None,
        description="New professor overseeing the coursework (carries a persistent uni).",  
    )
    people: Optional[List[PersonBase]] = Field(
        None,
        description="Replace the entire set of people with this list.",
        json_schema_extra={
            "example": [
                {
                    "uni": "kj2634",
                    "first_name": "Kusuma",
                    "last_name": "Jaipiam",
                    "email": "kj2634@columbia.edu",
                }
            ]
        },
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
                    "title": "Advanced Cloud Computing",
                    "semester": "Spring 2026",
                    "professor": {
                        "uni": "df123",
                        "first_name": "Donald",
                        "last_name": "Ferguson",
                        "email": "donald.ferguson@cs.columbia.edu",
                    },
                    "people": [
                        {
                            "uni": "kj2634",
                            "first_name": "Kusuma",
                            "last_name": "Jaipiam",
                            "email": "kj2634@columbia.edu",
                        }
                    ],
                    "created_at": "2025-01-15T10:20:30Z",
                }
            ]
        }
    }


class CourseworkRead(CourseworkBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Coursework ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
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
                    "id": "99999999-9999-4999-8999-999999999999",
                    "title": "Cloud Computing",
                    "semester": "Fall 2025",
                    "professor": {
                        "uni": "df123",
                        "first_name": "Donald",
                        "last_name": "Ferguson",
                        "email": "donald.ferguson@cs.columbia.edu",
                    },
                    "people": [
                        {
                            "uni": "kj2634",
                            "first_name": "Kusuma",
                            "last_name": "Jaipiam",
                            "email": "kj2634@columbia.edu",
                        }
                    ],
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }
