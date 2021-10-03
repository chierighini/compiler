// ConsoleApplication1.cpp : Este arquivo contém a função 'main'. A execução do programa começa e termina ali.
//

#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<stdio.h>
#include<conio.h>
#define INFINITY 9999
#define MAX 10

int main()
{
	int G [ MAX ] [ MAX ] = { 
		{ 0 , 10 , 0 , 30 , 100 } , 
		{ 10 , 0 , 50 , 0 , 0 } , 
		{ 0 , 50 , 0 , 20 , 10 } , 
		{ 30 , 0 , 20 , 0 , 60 } , 
		{ 100 , 0 , 10 , 60 , 0 } } , 
		i , j , n = 5 , u = 0 ;
	int cost [ MAX ] [ MAX ] , distance [ MAX ] , pred [ MAX ] ;
	int visited [ MAX ] , count , mindistance , nextnode ;
	//pred[] stores the predecessor of each node
	//count gives the number of nodes seen so far
	//create the cost matrix
	
	for (i = 0; i < n; i = i + 1)
	{
		for ( j = 0 ; j < n ; j = j + 1 ) {
			if (G [ i ] [ j ] == 0) {
				cost [ i ] [ j ] = INFINITY ;
			}
			else {
				cost [ i ] [ j ] = G [ i ] [ j ] ;
			}
		}
	}

	for ( i = 0 ; i < n ; i = i + 1 )
	{
		distance [ i ] = cost [ u ] [ i ] ;
		pred [ i ] = u ;
		visited [ i ] = 0 ;
	}
	distance [ u ] = 0 ;
	visited [ u ] = 1 ;
	count = 1 ;
	while ( count < n - 1 )
	{
		mindistance = INFINITY;
		for ( i = 0 ; i < n ; i = i + 1 ) {
			if ( distance [ i ] < mindistance && ! visited [ i ] )
			{
				mindistance = distance [ i ] ;
				nextnode = i ;
			}
		}
		visited [ nextnode ] = 1 ;
		for (i = 0 ; i < n ; i = i + 1) {
			if ( ! visited [ i ] ) {
				if ( mindistance + cost [ nextnode ] [ i ] < distance [ i ] )
				{
					distance [ i ] = mindistance + cost [ nextnode ] [ i ] ;
					pred [ i ] = nextnode ;
				}
			}
		}
		count = count + 1 ;
	}

	for (i = 0 ; i < n ; i = i + 1) {
		if (i != u)
		{
			j = i ;
			while ( j != u )
			{
				j = pred [ j ] ;
				
			}
		}
	}
	return 0 ;
}