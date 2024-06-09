-- OPERAZIONI


INSERT INTO `sqlalchemy-tutorial`.customer
(name, address)
VALUES('Ettore', 'Via dei Tigli, 2/B');
INSERT INTO `sqlalchemy-tutorial`.customer
(name, address)
VALUES('Luigino', 'Via ...');
INSERT INTO `sqlalchemy-tutorial`.customer
(name, address)
VALUES('Pierino', 'Via ...');



INSERT INTO `sqlalchemy-tutorial`.item
(code, description)
VALUES('MN001', 'Matita nera');

INSERT INTO `sqlalchemy-tutorial`.item
(code, description)
VALUES('PN001', 'Penna nera');

INSERT INTO `sqlalchemy-tutorial`.item
(code, description)
VALUES('PR001', 'Penna rossa');

INSERT INTO `sqlalchemy-tutorial`.item
(code, description)
VALUES('FR001', 'Frullatore');



INSERT INTO `sqlalchemy-tutorial`.price_list
(item_code, start_val_date, price)
VALUES('PR001', '2024-06-09', 3.31);

INSERT INTO `sqlalchemy-tutorial`.price_list
(item_code, start_val_date, price)
VALUES('PR001', '2024-06-10', 3.53);



INSERT INTO `sqlalchemy-tutorial`.invoice
(invoice_number, invoice_date, customer_id)
VALUES(101, '2024-06-09', 1); 

INSERT INTO `sqlalchemy-tutorial`.invoice
(invoice_number, invoice_date, customer_id)
VALUES(102, '2024-06-09', 1); 

INSERT INTO `sqlalchemy-tutorial`.invoice
(invoice_number, invoice_date, customer_id)
VALUES(103, '2024-06-09', 1); 



INSERT INTO `sqlalchemy-tutorial`.invoice_detail
(invoice_number, item_code, quantity, actual_unit_price)
VALUES(101, 'MN001', 1, 3.31);

INSERT INTO `sqlalchemy-tutorial`.invoice_detail
(invoice_number, item_code, quantity, actual_unit_price)
VALUES(101, 'PN001', 1, 3.31);

INSERT INTO `sqlalchemy-tutorial`.invoice_detail
(invoice_number, item_code, quantity, actual_unit_price)
VALUES(102, 'PR001', 1, 5.16);

INSERT INTO `sqlalchemy-tutorial`.invoice_detail
(invoice_number, item_code, quantity, actual_unit_price)
VALUES(103, 'FR001', 1, 39.99);