103万超えたくない<br>
[https://kentakodama99.github.io/tax_stopper/](https://kentakodama99.github.io/tax_stopper/)

### 環境
自宅サーバ前提
#### db
  
* MySQL
  
#### frontend
  
* vuecli
  
#### backend
  
* python(fastapi)
  
#### その他使ったもの
  
* Docker
* phpMyAdmin(db確認用)
##### 設定項目
* docker/env
```
cp docker/env.templete docker/env
```

* `src/app/.env.development`
* `src/app/.env.production`
```
src/app/env.local
cp src/app/.env.development src/app/.env.local
```

### table
```
year INT NOT NULL,
month INT NOT NULL CHECK(1 <= month AND month <= 12),
income1 INT DEFAULT 0,
income2 INT DEFAULT 0,
PRIMARY KEY(year, month)
```
