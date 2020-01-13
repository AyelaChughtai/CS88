create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-- Comment out the unfinished questions while you
-- are working so as to avoid errors in the tests.

-- All short dogs
create table short_dogs as
select name, fur, height as size from dogs where height < 40;

-- The size of each dog
create table size_of_dogs as
SELECT dogs.name, sizes.size FROM dogs, sizes WHERE height > min AND height <= max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
SELECT d1.name from dogs as d1, dogs as d2, parents WHERE d1.name == parents.child and d2.name == parents.parent ORDER BY d2.height DESC;

-- Height and name of every dog that shares height 10's digit  
-- with at least one other dog and has the highest 1's digit of all dogs 
-- that have the same 10's digit
create table tallest_ as 
select name, height, COUNT(*) as c from dogs GROUP BY height/10 HAVING max(height % 10) and c > 1;
create table tallest as
select height,name from tallest_;
 -- HAVING Count > 1 AND MOD(height, 10) == max;

