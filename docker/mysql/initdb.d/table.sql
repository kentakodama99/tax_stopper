create table paycheck (
    year INT NOT NULL CHECK(0 <= year),
    month INT NOT NULL CHECK(1 <= month AND month <= 12),
    income1 INT DEFAULT 0,
    income2 INT DEFAULT 0,
    PRIMARY KEY(year, month)
);