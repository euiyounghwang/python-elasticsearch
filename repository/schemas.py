from pydantic import BaseModel, Field, NonNegativeInt, validator
from datetime import datetime
from pytz import timezone as tz
from enum import Enum
from typing import List, Union
import uuid

# --
# API Model
# --



class Sort_Order(str, Enum):
    desc = 'DESC'
    asc = 'ASC'
    
    
class Search(BaseModel):
    include_basic_aggs: bool = True
    pit_id: str = ""
    query_string: str = "performance"
    size: int = 20
    # sort_order: str = "DESC"
    sort_order: Sort_Order = Sort_Order.desc
    start_date : str = "2021 01-01 00:00:00"
    ids_filters : list = ["*"]
    
    def to_json(self):
        return {
            'include_basic_aggs' : self.include_basic_aggs,
            'pit_id' : self.pit_id,
            'query_string' : self.query_string,
            'size' : self.size,
            'sort_order' : self.sort_order,
            'start_date' : self.start_date,
            'ids_filters' : self.ids_filters
        }
    
    
class Performance(BaseModel):
    data_size: str = "600gb"
    
    def to_json(self):
        return {
            'data_size' :  self.data_size
        }

    
class MessageSchema(BaseModel):
    message: str