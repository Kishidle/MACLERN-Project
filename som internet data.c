/*
	Self Organizing Map(SOM) Code
	Created by: Ramon Arca
				Darren Garcia
	For MACLERN 2016 X22	
*/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

float randomizeMap(float map[]){
	
	int x;
	int y;
	
	for(x = 0; x < #; x++){ // # should be size of map
		for(y = 0; y < #; y++){
			
			map[x][y] = (float) rand() / (float) RAND_MAX;
		}
	}
	
	return map;
}

int main(){
	
	srand(time(NULL));
	float dataArr[5] = {0}; //this is the data, array size should be how big it is.
	float map[][] = {0}; //this is the SOM map, array size should be determined from the input size
	float learningRate = 0.9; //placeholder learning rate
	int radius = 0;
	
	randomizeMap(&map);
	
		
	
	
	
	return 0;
}
