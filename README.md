# Trading program
Crazy tr8 is a free and open source crypto-trading bot written in Pyhton. It is designed to support Zondacrypto exchange. It is still under development.

## Disclaimer
This software is for educational purposes only. Do not risk money which you are afraid to lose. USE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.

### Instalation
- Create database manually in your database system or by typing this command in a terminal:
```
psql -u postgres -c "create database crazy_tr8"
```
- Run "create_schema.sql" file on newly created database or type this command in a terminal:
```
psql -u postgres -d crazy_tr8 -f create_schema.sql
```
- Start the program with your database details: 
```
--datasource schema://user:password@host:1234/dbname
```