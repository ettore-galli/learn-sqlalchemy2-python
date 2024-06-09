CREATE TABLE customer (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    address VARCHAR(200),
    PRIMARY KEY (id)
);

CREATE TABLE item (
    id INTEGER NOT NULL AUTO_INCREMENT,
    code VARCHAR(30) NOT NULL,
    description VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE UNIQUE INDEX idx_item_code ON item (code);

CREATE TABLE price_list (
    id INTEGER NOT NULL AUTO_INCREMENT,
    item_code VARCHAR(30) NOT NULL,
    start_val_date DATETIME NOT NULL,
    price NUMERIC(30, 9) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(item_code) REFERENCES item (code)
);

CREATE UNIQUE INDEX idx_price_list_item_code_start_val_date ON price_list (item_code, start_val_date);

CREATE TABLE invoice (
    id INTEGER NOT NULL,
    invoice_date DATETIME NOT NULL,
    customer_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(customer_id) REFERENCES customer (id)
);

CREATE TABLE invoice_detail (
    id INTEGER NOT NULL AUTO_INCREMENT,
    invoice_id INTEGER NOT NULL,
    item_code VARCHAR(30) NOT NULL,
    quantity NUMERIC(30, 9) NOT NULL,
    actual_unit_price NUMERIC(30, 9) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(invoice_id) REFERENCES invoice (id),
    FOREIGN KEY(item_code) REFERENCES item (code)
)