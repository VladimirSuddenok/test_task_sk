-- пользователь
CREATE TABLE p_user(
    id UUID DEFAULT uuid_generate_v4 (),
    firstname VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    middlename VARCHAR(100) NULL,
    fio VARCHAR(300) NULL,
    sex VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (id)
);

-- друзья пользователя
CREATE TABLE friend_record(
    id SERIAL,
    user_id UUID NOT NULL,
    friend_id UUID NOT NULL,
    FOREIGN KEY (user_id) REFERENCES p_user (id),
    FOREIGN KEY (friend_id) REFERENCES p_user (id)
);

--триггер на вставку fio

-- заказ
CREATE TABLE p_order(
    id UUID DEFAULT uuid_generate_v4 (),
    number INT NOT NULL,
    user_id UUID NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES p_user (id) 
);

-- товар
CREATE TABLE product(
    id UUID DEFAULT uuid_generate_v4 (),
    name VARCHAR(100) NOT NULL,
    descriptions VARCHAR(300) NULL,
    left_in_stock INT NOT NULL,
    PRIMARY KEY (id)
);

-- тип валюты
CREATE TABLE type_currency(
    id SERIAL,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

-- цена товара
CREATE TABLE price(
    id SERIAL,
    product_id UUID NOT NULL,
    amount INT NOT NULL,
    type_currency_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_id) REFERENCES product (id),
    FOREIGN KEY (type_currency_id) REFERENCES type_currency (id)
);

-- список товаров из заказа
CREATE TABLE product_record(
    id SERIAL, 
    order_id UUID NOT NULL,
    product_id UUID NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (order_id) REFERENCES p_order (id),
    FOREIGN KEY (product_id) REFERENCES product (id)
);