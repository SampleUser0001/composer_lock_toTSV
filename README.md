# composer.lock to TSV

composer.lockをTSVに変換する。  
扱っているのはpackages配下の、name, version, require-devのみなので、適当に修正すること。

## 準備

1. ```app/files/composer.lock```に対象のファイルを配置する。

## 実行

``` sh
docker-compose up 
```

## 実行結果

```app/files/result.tsv```に出力される。