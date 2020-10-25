# geo_distance_lin_alg

## Introduction

As big data analytics become increasingly prevalent in modern day businesses, there is an increasing demand for efficient algorithms for geospatial distance calculations. As ride sharing and logistics companies try to optimize their delivery routes, their data engineers scramble to process large amounts of datasets for insight generation. The problem is that most companies and research institutions tend to depend on Google’s Distance Matrix API for distance calculation. The API provides information that pertain to distance, routes, and directions for every pair of latitude and longitude provided to it. However, the API is not free and can cost up to 10 USD for every 1000 distances calculated. This could amount to hundreds of thousands of dollars for companies that have large amounts of data and services to process and manage.

## How to use

Enter the 4 addresses required (start point, end point, start point for orthogonal vector, end point for orthogonal vector) in calculate_geo_distance.py. THe script will calculate the distance for you.
	
## Explanation of algorithm  

In this project, I shall propose a simple algorithm for cities with grid plans—a type of city plan in which streets run at right angles to each other, forming a grid. The initial input will be processed to generate a pair of latitude-longitude coordinates. The differences in their latitudes and longitudes will give us a direction vector that would be parallel to one of the coordinate axes in the city. A 90 degrees rotation matrix will be applied onto the vector to transform it into its orthogonal pair. This new vector would be perpendicular to the original direction vector and parallel to the other coordinate axis in the city. The orthogonal vectors can be stored for future distance calculations within the city.

After finding the two orthogonal vectors that form the basis for the grid of the city, the next step is to find the “mid-point” of the Manhattan distance between the two coordinates. It is not the halfway mark for the distance that a person must travel but the end of the path that one has to travel along one of the orthogonal vectors before taking a turn and travelling in the perpendicular direction to reach the destination. It is circled in red in the image below.

![midpoint image](https://github.com/samueltan97/manhattan_haversine_calculator/blob/master/images/midpoint.png)

To find the “mid-point”, we need to build an augmented matrix. The two orthogonal vectors would form the coefficient portion of the augmented matrix. The differences in latitude and longitude between the start and destination would form the augmented column of the augmented matrix. By solving this augmented matrix, we are able to get the coefficients for the two orthogonal vectors that would form the two orthogonal paths that would give us the Manhattan distance. We can get our “mid-point” by adding one of the weighted orthogonal vector to the coordinates of the start point. By applying the Haversine formula twice—once on the distance between the start point and the mid-point and the second time on the mid-point and the destination—we are able to calculate the Manhattan distance between two points.

### Example in Philadelphia

Let us try to find the distance between Reading Terminal Market and Race Street Pier. First, we need to provide the algorithm with two locations (Pennsylvania Convention Center and the 12/13th & Locust Street Station) that are on the same road. 

![example image](https://github.com/samueltan97/manhattan_haversine_calculator/blob/master/images/example.png)

![orthogonal image](https://github.com/samueltan97/manhattan_haversine_calculator/blob/master/images/orthogonal.png)

|                                 | Latitude    | Longitude   |
| ------------------------------- | ----------- | ----------- |
| Pennsylvania Convention Center  | 39.9543931  | -75.1609668 |
| 12/13th & Locust Street Station | 39.947944   | -75.162363  |
| Reading Terminal Market         | 39.9533113  | -75.15943   |
| Race Street Pier                | 39.9556634  | -75.1504502 |

To develop the first orthogonal vector, we first try to find the unit vector that lies in the direction from Pennsylvania Convention Center to the 12/13th & Locust Street Station. Following which, we rotate the vector by 90 degrees to get the orthogonal pair before building a coefficient matrix, A, with the two orthogonal vectors

![latex1 image](https://github.com/samueltan97/manhattan_haversine_calculator/blob/master/images/latex1.png)

![latex2 image](https://github.com/samueltan97/manhattan_haversine_calculator/blob/master/images/latex2.png)

Next, we need to calculate the actual difference in latitude and longitude between the start and end points. The Haversine formula requires the latitudes and longitudes to be converted into radians.

![latex3 image](https://github.com/samueltan97/manhattan_haversine_calculator/blob/master/images/latex3.png)

|                         | Latitude (in radians) | Longitude (in radians) |
| ----------------------- | --------------------- | ---------------------- |
| Reading Terminal Market | 0.697316829259256     | -1.3117795174222018    |
| Race Street Pier        | 0.6973139773912581    | -1.311419482177454     |

Now that we have the weights for the different orthogonal vectors, we will be able to construct the “mid-point” by adding one of the orthogonal vectors (multiplied by its weight) to the coordinates of the Reading Terminal Market. After constructing the “mid-point”, we should be able to find the Manhattan distance between Reading Terminal Market (marked by S) and Race Street Pier (marked by E). The distance calculated by Google is approximately 1.3 miles. My algorithm gives us 1.37 miles which is within 0.5% error. 

![latex4 image](https://github.com/samueltan97/manhattan_haversine_calculator/blob/master/images/latex4.png)

