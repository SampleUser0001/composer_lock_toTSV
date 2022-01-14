# composer.lock to TSV

composer.lockをTSVに変換する。  
扱っているのはpackages配下の、name, version, require-devのみなので、適当に修正すること。

## 準備

1. ```app/files```に対象のファイルを配置する。

## 実行

``` sh
# 実行ファイル名には「{}」を含めること。
docker-compose run python ${composer.lockのファイル名} ${実行結果ファイル名} 
```

## 実行結果

```app/files```配下に出力される。