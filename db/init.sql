CREATE DATABASE elevators_db;
use elevators_db;

CREATE TABLE elevators_tbl (
  building_id INT,
  num_of_floors INT,
  elevator_id INT,
  full_capacity INT,
  remaining_capacity INT,
  current_floor INT,
  next_requested_floor INT
);

INSERT INTO elevators_tbl(
  building_id,
  num_of_floors,
  elevator_id,
  full_capacity,
  remaining_capacity,
  current_floor,
  next_requested_floor
  )
VALUES
  (23, 32, 3, 6, 22, 11,  10),
  (23, 42, 2, 6, 22, 11,  10),
  (23, 52, 1, 6, 12, 12,  10);