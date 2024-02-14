# import pydantic
#
# # код к теме валидации json vs pydantic
#
# class User(pydantic.BaseModel):
#     firstName: str
#     lastName: str
#     email: str
#
# User(**response.json()) - тут и произойдет считывание json
