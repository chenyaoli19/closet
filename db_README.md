--warmth_level--
1 - one single layer (i.e. a t-shirt)
2 - sweater/light jacket
3 - heavy jacket

--color--
0  - 'white',
13 - 'Black',
1  - 'Orange',
2  - 'Yellow',
3  - 'Yellow Green',
4  - 'Green',
5  - 'Blue Green',
6  - 'Blue',
7  - 'Blue Violet',
8  - 'Violet',
9  - 'Mauve',
10 - 'Mauve Pink',
11 - 'Pink',
12 - 'Red',

--color code--
1 - very light
2 - slight light
3 - medium
4 - slight dark
5 - very dark

mysql> mysql> describe items;
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------+------+-----+---------+----------------+
| Field        | Type                                                                                                                                        | Null | Key | Default | Extra          |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------+------+-----+---------+----------------+
| id           | int(11) unsigned                                                                                                                            | NO   | PRI | NULL    | auto_increment |
| color        | enum('white','Black','Orange','Yellow','Yellow Green','Green','Blue Green','Blue','Blue Violet','Violet','Mauve','Mauve Pink','Pink','Red') | YES  |     | NULL    |                |
| color_code   | enum('1','2','3','4','5')                                                                                                                   | YES  |     | NULL    |                |
| color_solid  | tinyint(1)                                                                                                                                  | YES  |     | NULL    |                |
| loose_tight  | enum('loose','mid','tight')                                                                                                                 | YES  |     | NULL    |                |
| texture      | enum('cotton','leather','denim','silk','knit')                                                                                              | YES  |     | NULL    |                |
| bottom_top   | enum('bottom','top')                                                                                                                        | YES  |     | NULL    |                |
| category     | enum('t-shirt','short-skirt','long-skirt','jeans','pants','shorts','shirt','blouse','jacket','knits','sweater','tank-top')                  | YES  |     | NULL    |                |
| warmth_level | enum('1','2','3')                                                                                                                           | YES  |     | NULL    |                |
| image_url    | varchar(255)                                                                                                                                | YES  |     | NULL    |                |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------+------+-----+---------+----------------+