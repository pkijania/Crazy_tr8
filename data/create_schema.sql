-- Table: history

-- DROP TABLE IF EXISTS history;

CREATE TABLE IF NOT EXISTS history
(
    id character varying(50) primary key,
	price character varying(50),
    date character varying(50),
    ema_long character varying(50),
    ema_short character varying(50),
    macd character varying(50),
    rsi character varying(50),
    adx character varying(50)
)
