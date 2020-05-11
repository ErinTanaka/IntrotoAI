/*
 * MinimaxPlayer.cpp
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
 *	Minimax: Madison Dhanens 5/4/2018
 */
#include <iostream>
#include <assert.h>
#include "MinimaxPlayer.h"

using std::vector;

MinimaxPlayer::MinimaxPlayer(char symb) :
		Player(symb) {

}

MinimaxPlayer::~MinimaxPlayer() {

}

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {

		//std::cout << "in get move\n";
		//int sucCoors[16][2];
		int** sucCoors = new int*[16];
		for(int i = 0; i < 16; i++)
		    sucCoors[i] = new int[2];

		for(int q=0; q<16; q++)
			for(int j=0; j<2; j++){
				sucCoors[q][j] = -1;
			}

		//std::cout << "before successor\n";
		successors(b, sucCoors, 'O');
		//std::cout << "after successor\n";

		//std::cout << "sucCoors: " << sucCoors[0][0] << "and" << sucCoors[0][1] << "\n";

		int a=0;
		while(sucCoors[a][0] != -1){
			a++;
		}

		//std::cout <<"a: " << a << "\n";

		int** valid = new int*[a];
		for(int i = 0; i < a; ++i)
				valid[i] = new int[2];

		for(int x=0; x<a; x++)
			for(int y=0; y<2; y++)
				valid[x][y] = sucCoors[x][y];

		//std::cout << "Valid: " << valid[0][0] << "and" << valid[0][1] << "\n";

		//std::cout << "after making valid\n";
		int vals[a];

		//possible additional successor call?
		for(int i=0; i<a; i++){
			// OthelloBoard* next;
			// next = b;
			OthelloBoard nt = *b;
			OthelloBoard* next = &nt;
			//std::cout << "before play move\n";
			//std::cout << valid[i][1] << " and " << valid[i][0] << "\n";
/*erins swithinc the indexes*/next->play_move(valid[i][0], valid[i][1], 'O');
			//std::cout << "before first minimax call\n";
//erin added This
			int** stoopid = new int*[16];
			for(int itr = 0; itr < 16; ++itr){
		 			stoopid[itr] = new int[2];
			}
			for(int itr=0; itr<16; itr++){
				for(int jeff=0; jeff<2; jeff++){
					stoopid[itr][jeff] = -1;
				}
			}
			//make successor array
			successors(next, stoopid, 'O');

			int anton=0;
			while(stoopid[anton][0] != -1){
				anton++;
			}

			//chop array so it only holds valid coordinates
			//int valid[a][2];
			int** vladimir = new int*[anton];
			for(int itr = 0; itr < anton; ++itr){
					vladimir[itr] = new int[2];
			}

			for(int x=0; x<anton; x++){
				for(int y=0; y<2; y++){
					vladimir[x][y] = stoopid[x][y];
				}
			}

			vals[i] = minimaxFn(next, vladimir, 'O', anton);
			//std::cout << "---BACK---\n";
		}

		//std::cout << "out of building the val array\n";

		int solution = -1000;
		int index=0;
		for(int x=0; x<a; x++){
			if(vals[x] > solution){
				//std::cout << "in solution check\n";
				solution = vals[x];
				index = x;
				//std::cout << "out of solution check\n";
			}
		}

		//send back coordinates of best move
		row = sucCoors[index][0];
	  col = sucCoors[index][1];
}

void MinimaxPlayer::successors(OthelloBoard* curBoard, int** validCoor, char symb){

	int place=0;

	for (int c = 0; c < 4; c++) {
		for (int r = 0; r < 4; r++) {
			// std::cout << c << r << "\n";
			// std::cout << place << "\n";
			if (curBoard->is_cell_empty(c, r) && curBoard->is_legal_move(c, r, symb)) {
				//std::cout << "before storing\n";
				validCoor[place][0] = r;	//0=place
				validCoor[place][1] = c;
				//std::cout << "after storing valid coordinates\n";
				place++;
	 		}
	 	}
	 }

}

int MinimaxPlayer::utility(OthelloBoard* b){
	int a = b->count_score('X');
	int c = b->count_score('O');
	//int weight = b.count_score(b, 'X') - b.count_score(b, 'O');
	int weight = a - c;
	return weight;
}

//how to pass succ correctly????????v
int MinimaxPlayer::minimaxFn(OthelloBoard* board, int** succ, char player, int size){

	//std::cout << "in the minimax\n";

	//check if at end of game
	if(board->has_legal_moves_remaining(player)==false){
		//std::cout << "RETURN function\n";
		return utility(board);
	}

	int best;
	int value;

	//DOUBLE CHECK WHICH IS IS MIN/MAX X/O

	if(player == 'X'){
		best = -10000;
		for(int i=0; i<size; i++){
			// OthelloBoard* next;
			// next = board;
			OthelloBoard nt = *board;
			OthelloBoard* next = &nt;
			next->play_move(succ[i][0], succ[i][1], 'X');

			//initialize successor array with -1
			//int s[16][2];
			int** s = new int*[16];
			for(int i = 0; i < 16; ++i)
			     s[i] = new int[2];

			for(int i=0; i<16; i++)
				for(int j=0; j<2; j++)
					s[i][j] = -1;

			//make successor array
			successors(next, s, 'O');

			//std::cout << "MMX after successor\n";

			//get length of successor array that holds valid points
			int a=0;
			while(s[a][0] != -1){
				a++;
			}

			//chop array so it only holds valid coordinates
			//int valid[a][2];
			int** valid = new int*[a];
			for(int i = 0; i < a; ++i)
			    valid[i] = new int[2];

			for(int x=0; x<a; x++)
				for(int y=0; y<2; y++)
					valid[x][y] = s[x][y];

			value = minimaxFn(next, valid, 'O', a);
			if(value > best)
				best = value;
			}
			return best;
	}

	else if(player == 'O'){
		best = 10000;
		for(int i=0; i<size; i++){
			// OthelloBoard* next;
			// next = board;
			OthelloBoard nt = *board;
			OthelloBoard* next = &nt;
			next->play_move(succ[i][0], succ[i][1], 'O');

			//initialize successor array with -1
			//int s[16][2];

			int** s = new int*[16];
			for(int i = 0; i < 16; ++i)
			    s[i] = new int[2];

			for(int i=0; i<16; i++)
				for(int j=0; j<2; j++)
					s[i][j] = -1;

			//make successor array
			successors(next, s, 'X');

			//get length of successor array that holds valid points
			int a=0;
			while(s[a][0] != -1){
				a++;
			}

			//chop array so it only holds valid coordinates
			//int valid[a][2];
			int** valid = new int*[a];
			for(int i = 0; i < a; ++i)
					valid[i] = new int[2];

			for(int x=0; x<a; x++)
				for(int y=0; y<2; y++)
					valid[x][y] = s[x][y];

			value = minimaxFn(next, valid, 'X', a);
			if(value < best)
				best = value;
			}
			return best;
	}

}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}

