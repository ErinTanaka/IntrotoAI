/*
 * MinimaxPlayer.cpp
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
 */
#include <iostream>
#include <assert.h>
#include "MinimaxPlayer.h"
#include <cstdlib>

using std::vector;

MinimaxPlayer::MinimaxPlayer(char symb) :
		Player(symb) {

}

MinimaxPlayer::~MinimaxPlayer() {

}

void MinimaxPlayer::get_move(OthelloBoard* b, int& col, int& row) {
    // To be filled in by you
		//declare place to store coordinates and fill with -1's
		std::cout << "hello motha fuckers\n";
		int** moves = new int*[16];
		for(int i = 0; i < 16; i++){
			moves[i] = new int[2];
		}
		for(int i=0; i<16; i++){
			moves[i][0]=-1;
			moves[i][1]=-1;
		}
		//generate coordinates of next moves
		successorCoor(b, 'O', moves);
		//count number of sucessors
		std::cout << "printing contents of moves\n";
		for(int f=0; f<16; f++){
			std::cout << moves[f][0] << "," << moves[f][1] << "\n";
		}


		int numSuccessors;
		for(int j=0; j<16; j++){
			if(moves[j][0]==-1){
				numSuccessors=j;
				break;
			}
		}

		//place to store list of coordinates minus excess space
		int** nextSucc = new int*[numSuccessors];
		for(int i = 0; i < numSuccessors; i++){
			nextSucc[i] = new int[2];
		}
		//copy values over from old array
		for(int i=0; i<numSuccessors; i++){
				nextSucc[i][0]=moves[i][0];
				nextSucc[i][1]=moves[i][1];
		}
		std::cout << "printing contents of nextSucc\n";
		for(int f=0; f<numSuccessors; f++){
			std::cout << nextSucc[f][0] << "," << nextSucc[f][1] << "\n";
		}


		//place to store all minimax vals
		int minmaxVals[numSuccessors];
		//get minimax vall for each generated sucessor
		for(int i=0; i<numSuccessors; i++){
			std::cout << "for loop" << '\n';
			OthelloBoard tmpboard= *b;
		  OthelloBoard * tmp=&tmpboard;
			std::cout << "callin playmove" << '\n';
			tmp->play_move(nextSucc[i][0], nextSucc[i][1],'O');
			//place to store tmp's sucessors
			tmp->display();
			std::cout << "passed playmove" << '\n';

			int** tmpmoves = new int*[16];
			for(int j = 0; j < 16; j++){
				tmpmoves[j] = new int[2];
			}
			for(int j=0; j<16; j++){
				tmpmoves[j][0]=-1;
				tmpmoves[j][1]=-1;
			}
			successorCoor(tmp, 'X', tmpmoves);
			//count tmp's sucessors
			int tmpNumSuccessors;
			for(int j=0; j<16; j++){
				if(tmpmoves[j][0]==-1){
					tmpNumSuccessors=j;
					break;
				}
			}
			// trimmed list of successors
			//int actualNextSuccessors[tmpNumSuccessors][2];
			int** actualNextSuccessors = new int*[tmpNumSuccessors];
			for(int j = 0; j < tmpNumSuccessors; j++){
				actualNextSuccessors[j] = new int[2];
			}
			for(int j=0; j<tmpNumSuccessors; j++){
				actualNextSuccessors[j][0]=tmpmoves[j][0];
				actualNextSuccessors[j][1]=tmpmoves[j][1];
			}
			std::cout << "callin minimax\n";
			//minmaxVals[i]=miniMaxFn(tmp, actualNextSuccessors, tmpNumSuccessors, 'X');
			std::cout << "back in get move\n";
		}
		int location;
		int lowezt=minmaxVals[0];
		for(int i=0; i<numSuccessors; i++){
			if (minmaxVals[i]<lowezt){
				lowezt=minmaxVals[i];
				location=i;
			}
		}
		std::cout << "hello motha fuckers\n";
		std::cout << nextSucc[location][0];
		std::cout << nextSucc[location][1];
		row=nextSucc[location][0];
		col=nextSucc[location][1];



}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}


void MinimaxPlayer::successorCoor(OthelloBoard * currentBoard, char symb, int ** coorList){
	int counter=0;
	for(int r=0; r<4; r++){
		for(int c=0; c<4; c++){
			if (currentBoard->is_cell_empty(c, r) && currentBoard->is_legal_move(c, r, symbol)) {
				coorList[counter][1]=r;
				coorList[counter][0]=c;
				counter++;
			}
		}
	}
}

//depth + 1 represents the sucessors of the current board so we need to ba able to call the find best move on the current board and pass that into the thingy
//but that may lead to neverending recursion???? umm not actually sure



int MinimaxPlayer::utilityFn(OthelloBoard * currentBoard){
	int score=currentBoard->count_score('X')-currentBoard->count_score('O');
	return score;
}

int MinimaxPlayer::miniMaxFn(OthelloBoard*  b, int ** succArray, int len, char symbol){
	//base caseno more move left to make return  value for comparison
	if(b->has_legal_moves_remaining(symbol)==false){
		std::cout << "in minimax base case" << '\n';
		return utilityFn(b);
	}
	for (int n = 0; n < len; n++) {
		std::cout << succArray[n][0] << "," << succArray[n][1] << '\n';
	}
	//int nextSucc[16][2];
	// int** nextSucc = new int*[16];
	// for(int i = 0; i < 16; i++){
	// 	nextSucc[i] = new int[2];
	// }
	// //fill array with -1
	// for(int i=0; i<16; i++){
	// 	nextSucc[i][0]=-1;
	// 	nextSucc[i][1]=-1;
	// }

	int best;
	int val;
  //int len=sizeof(succArray)/sizeof(int*);
	//human
	if(symbol=='X'){
		std::cout << "conditional X" << '\n';
		best=-10000;
		for(int i=0; i<len; i++){
			OthelloBoard board= *b;
			OthelloBoard * tempBoard=&board;
			int** nextSucc = new int*[16];
			for(int j = 0; j < 16; j++){
				nextSucc[j] = new int[2];
			}
			//fill array with -1
			for(int j=0; j<16; j++){
				nextSucc[j][0]=-1;
				nextSucc[j][1]=-1;
			}
			tempBoard->display();
			std::cout << "before tempBoard->play_move" << '\n';
			std::cout << succArray[i][0] << "," << succArray[i][1] << '\n';

			tempBoard->play_move(succArray[i][0], succArray[i][1],'X');
			tempBoard->display();
			successorCoor(tempBoard, 'O', nextSucc);
			for (int n = 0; n < len; n++) {
				std::cout << nextSucc[n][0] << "," << nextSucc[n][1] << '\n';
			}
			//choppy choppy
			//get the "number of successors"
			int numSuccessors;
			for(int j=0; j<16; j++){
				if(nextSucc[j][0]==-1){
					numSuccessors=j;
					break;
				}
			}
			//copy generated list of successors to a new list of coordinates and reset oglist for next for loop iteration
			//int actualNextSuccessors[numSuccessors][2];
			int** actualNextSuccessors = new int*[numSuccessors];
			for(int j = 0; j < numSuccessors; j++){
				actualNextSuccessors[j] = new int[2];
			}
			for(int j=0; j<numSuccessors; j++){
				actualNextSuccessors[j][0]=nextSucc[j][0];
				actualNextSuccessors[j][1]=nextSucc[j][1];
				//nextSucc[j][0]=-1;
				//nextSucc[j][1]=-1;
			}
			//recursively call minimaxe fn on the move in succArray
			std::cout << "callin my minimax recursively" << '\n';
			for (int n = 0; n < numSuccessors; n++) {
				std::cout << actualNextSuccessors[n][0] << "," << actualNextSuccessors[n][1] << '\n';
			}
			val=miniMaxFn(tempBoard, actualNextSuccessors, numSuccessors, 'O');
			if(val>best){
				best=val;
			}
		}
		return best;
	}
	else{
		std::cout << "conditional O" << '\n';

		best=10000;
		for(int i=0; i<len; i++){
			//OthelloBoard tempBoard= b;
			//tempBoard = tempBoard.play_move(succArray[i][1], succArray[i][0], 'O');
			OthelloBoard board= *b;
			OthelloBoard * tempBoard=&board;
			int** nextSucc = new int*[16];
			for(int j = 0; j < 16; j++){
				nextSucc[j] = new int[2];
			}
			//fill array with -1
			for(int j=0; j<16; j++){
				nextSucc[j][0]=-1;
				nextSucc[j][1]=-1;
			}
			tempBoard->play_move(succArray[i][0], succArray[i][1],'X');

			successorCoor(tempBoard, 'X', nextSucc);
			for (int n = 0; n < len; n++) {
				std::cout << nextSucc[n][0] << "," << nextSucc[n][1] << '\n';
			}
			//choppy choppy
			//get the "number of successors"
			int numSuccessors;
			for(int j=0; j<16; j++){
				if(nextSucc[j][0]==-1){
					numSuccessors=j;
					break;
				}
			}
			//copy generated list of successors to a new list of coordinates and reset oglist for next for loop iteration
			//int actualNextSuccessors[numSuccessors][2];
			int** actualNextSuccessors = new int*[numSuccessors];
			for(int j = 0; j < numSuccessors; j++){
				actualNextSuccessors[j] = new int[2];
			}
			for(int j=0; j<numSuccessors; j++){
				actualNextSuccessors[j][0]=nextSucc[j][0];
				actualNextSuccessors[j][1]=nextSucc[j][1];
				//nextSucc[j][0]=-1;
				//nextSucc[j][1]=-1;
			}
			//recursively call minimaxe fn on the move in succArray
			val=miniMaxFn(tempBoard, actualNextSuccessors, numSuccessors, 'X');
			if(val<best){
				best=val;
			}
		}
		return best;
	}
}
