from pydantic import ConfigDict, BaseModel


class BseResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )
