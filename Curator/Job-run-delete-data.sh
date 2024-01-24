#!/bin/bash
set -e

today=$(date '+%Y%m%d')

# 오늘날짜 기준으로 삭제 할 날짜의 수를 지정
delete_days=2

# 오늘날짜에서 지정 날짜를 빼서 result변수에 할당
result=`expr $today - $delete_days`

# 엘라스틱 쿼리문 
curl -X POST "localhost:9200/test_idx/_delete_by_query?conflicts=proceed&pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "ymd": '$result'
    }
  }
}'