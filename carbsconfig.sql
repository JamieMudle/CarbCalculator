CREATE DATABASE carbscollector;

USE carbscollector;

CREATE TABLE carbsandportions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(100),
    carbohydrates FLOAT(50),
    weight FLOAT(50),
    portionsize FLOAT(50),
    result FLOAT(50)
);

