/*
 * MinimaxPlayer.cpp
 *
 *  Created on: Apr 17, 2015
 *      Author: wong
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
    // To be filled in by you
		//storage for at leat 16 sucessors kind of extra but whatever too late now
		int ** fullSuccList = new int*[16];
		for (int i=0; i<16; i++){
			fullSuccList[i]=new int[2];
		}
		for (int i=0; i<16; i++){
			fullSuccList[i][0]=-1;
			fullSuccList[i][1]=-1;
		}
		generateSucessorCoordinates(b, fullSuccList, 'O');
		// for (int i=0; i<16; i++){
		// 	std::cout << "row: " << fullSuccList[i][0] << ", col: " << fullSuccList[i][1] << '\n';
		// }
		//putting sucessor coordinates into appropriatly sized array
		int resizeLen=0;
		for (int i=0; i<16; i++){
			if (fullSuccList[i][0]==-1 &&fullSuccList[i][1]==-1){
				resizeLen=i;
				break;
			}
		}
		int ** resizedSuccList = new int*[resizeLen];
		for (int i=0; i<resizeLen; i++){
			resizedSuccList[i]=new int[2];
		}
		for (int i=0; i<resizeLen; i++){
			resizedSuccList[i][0]=fullSuccList[i][0];
			resizedSuccList[i][1]=fullSuccList[i][1];
		}
		// std::cout << "okay bitches, here's the low down" << '\n';
		// std::cout << "resizeLen:" << resizeLen << '\n';
		// std::cout<< "contents of resizedSuccList:\n";
		// for (int i=0; i<resizeLen; i++){
		// 	std::cout << resizedSuccList[i][0] << ", " << resizedSuccList[i][1] << '\n';
		// }
		// std::cout << "low down out\n";
		//array to stor corresponding minimax vals that get returned
		int minimaxValues[resizeLen];
		for (int i=0; i<resizeLen; i++){
			minimaxValues[i]=10000;
		}

		//okay now it gets messy...

		for(int itr=0; itr< resizeLen; itr++){
			//make a board with the move at resizedSuccList[itr]
			OthelloBoard cpyBoard=*b;
			OthelloBoard * nxtBoard= &cpyBoard;
			nxtBoard->play_move(resizedSuccList[itr][0], resizedSuccList[itr][1], 'O');
			//generate sucessors for this new board
			int ** nxtFullSuccList=new int*[16];
			for(int i=0; i<16; i++){
				nxtFullSuccList[i]=new int[2];
			}
			for (int i=0; i<16; i++){
				nxtFullSuccList[i][0]=-1;
				nxtFullSuccList[i][1]=-1;
			}
			generateSucessorCoordinates(nxtBoard, nxtFullSuccList, 'X');
			int nxtResizeLen=0;
			for (int i=0; i<16; i++){
				if (nxtFullSuccList[i][0]==-1 && nxtFullSuccList[i][1]==-1){
					nxtResizeLen=i;
					break;
				}
			}
			int ** nxtResizedSuccList = new int*[nxtResizeLen];
			for (int i=0; i<nxtResizeLen; i++){
				nxtResizedSuccList[i]=new int[2];
			}
			for (int i=0; i<nxtResizeLen; i++){
				nxtResizedSuccList[i][0]=nxtFullSuccList[i][0];
				nxtResizedSuccList[i][1]=nxtFullSuccList[i][1];
			}
			//call minimax on this board
			int minmaxval= minimaxFunction(nxtBoard, nxtResizedSuccList, nxtResizeLen, 'X');
			minimaxValues[itr]=minmaxval;
			// std::cout << "minimax returned:"<< minmaxval << '\n';
			// std::cout << "contents of minimaxValues: " << minimaxValues[itr] << '\n';
			//store val returned from minimax for later comparison
		}
		int tmp=minimaxValues[0];
		int index=0;
		for (int i=0; i<resizeLen; i++){
		// 	std::cout << "minimaxvalue[" <<i<<"]: " << minimaxValues[i] << '\n';
			if (minimaxValues[i]<tmp){
				tmp=minimaxValues[i];
				index=i;
			}
		}
		// std::cout << "just checkin"<< index<<"\n";
		// std::cout << "col: " << resizedSuccList[index][0] << "\n";
		// std::cout << "row: " << resizedSuccList[index][1] << "\n";
		col=resizedSuccList[index][0];
		row=resizedSuccList[index][1];
}

MinimaxPlayer* MinimaxPlayer::clone() {
	MinimaxPlayer* result = new MinimaxPlayer(symbol);
	return result;
}

void MinimaxPlayer::generateSucessorCoordinates(OthelloBoard * b, int** storageArray, char player){
	int i=0;
	for (int col=0; col<4; col++){
		for (int row=0; row<4; row++){
			if(b->is_legal_move(col, row, player)){
				storageArray[i][0]=col;
				storageArray[i][1]=row;
				i++;
			}
		}
	}
}
int MinimaxPlayer::utilityFn(OthelloBoard * b){
	int weight=(b->count_score('X') - b->count_score('O'));
	return weight;
}
int MinimaxPlayer::minimaxFunction(OthelloBoard * b, int** succCoors, int lenSuccCoors, char playerChar){
	//base case
	if(b->has_legal_moves_remaining(playerChar)==false){
		int weight= utilityFn(b);
		return weight;
	}
	int best;
	int val;
	if (playerChar=='X'){
		best=-10000;
		for(int itr=0; itr<lenSuccCoors; itr++){
			OthelloBoard cpyBoard = * b;
			OthelloBoard * nxtBoard =  &cpyBoard;
			nxtBoard->play_move(succCoors[itr][0], succCoors[itr][1],'X');
			int ** nxtFullSuccList=new int*[16];
			for(int i=0; i<16; i++){
				nxtFullSuccList[i]=new int[2];
			}
			for (int i=0; i<16; i++){
				nxtFullSuccList[i][0]=-1;
				nxtFullSuccList[i][1]=-1;
			}
			generateSucessorCoordinates(nxtBoard, nxtFullSuccList, 'O');
			int nxtResizeLen=0;
			for (int i=0; i<16; i++){
				if (nxtFullSuccList[i][0]==-1 && nxtFullSuccList[i][1]==-1){
					nxtResizeLen=i;
					break;
				}
			}
			int ** nxtResizedSuccList = new int*[nxtResizeLen];
			for (int i=0; i<nxtResizeLen; i++){
				nxtResizedSuccList[i]=new int[2];
			}
			for (int i=0; i<nxtResizeLen; i++){
				nxtResizedSuccList[i][0]=nxtFullSuccList[i][0];
				nxtResizedSuccList[i][1]=nxtFullSuccList[i][1];
			}
			val=minimaxFunction(nxtBoard, nxtFullSuccList, nxtResizeLen, 'O');
			if(val>best){
				best=val;
			}
		}
		return best;
	}
	else{
		best=10000;
		for(int itr=0; itr<lenSuccCoors; itr++){
			OthelloBoard cpyBoard = * b;
			OthelloBoard * nxtBoard =  &cpyBoard;
			nxtBoard->play_move(succCoors[itr][0], succCoors[itr][1],'O');
			int ** nxtFullSuccList=new int*[16];
			for(int i=0; i<16; i++){
				nxtFullSuccList[i]=new int[2];
			}
			for (int i=0; i<16; i++){
				nxtFullSuccList[i][0]=-1;
				nxtFullSuccList[i][1]=-1;
			}
			generateSucessorCoordinates(nxtBoard, nxtFullSuccList, 'X');
			int nxtResizeLen=0;
			for (int i=0; i<16; i++){
				if (nxtFullSuccList[i][0]==-1 && nxtFullSuccList[i][1]==-1){
					nxtResizeLen=i;
					break;
				}
			}
			int ** nxtResizedSuccList = new int*[nxtResizeLen];
			for (int i=0; i<nxtResizeLen; i++){
				nxtResizedSuccList[i]=new int[2];
			}
			for (int i=0; i<nxtResizeLen; i++){
				nxtResizedSuccList[i][0]=nxtFullSuccList[i][0];
				nxtResizedSuccList[i][1]=nxtFullSuccList[i][1];
			}
			val=minimaxFunction(nxtBoard, nxtFullSuccList, nxtResizeLen, 'X');
			if(val<best){
				best=val;
			}
		}
		return best;

	}




}
