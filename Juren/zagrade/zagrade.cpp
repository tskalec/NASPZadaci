#include <iostream>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>
#include <bits/stdc++.h>

#define VELICINA_POLJA 500005

using namespace std;

int main(void){

    int n,sum,min;
	long long broj_kombinacija;
    long long broj_simetricnih=0;
	string input;

    vector<long long> nizpozitivan(VELICINA_POLJA,0);
    vector<long long> niznegativan(VELICINA_POLJA,0);

    scanf("%d",&n);
    for(int i=0;i<n;i++){
		cin >>input;

		sum=0;
		min=0;

		for(int j=0;input[j]!='\0';j++){
			if(input[j]=='(')	sum++;
			else				sum--;

			if(sum<min) min=sum;

		}
		if(min<0 && sum!=min){
			}else{
				if(sum>0) nizpozitivan[sum]++;
				if(sum<0) niznegativan[-sum]++;
				if(sum==0) broj_simetricnih++;
			}
	}

	long long rezultat=0;
	for(int i=0;i<VELICINA_POLJA;i++){
		broj_kombinacija=niznegativan[i]<nizpozitivan[i]?niznegativan[i]:nizpozitivan[i];
		rezultat=rezultat+broj_kombinacija;
	}

	rezultat=rezultat+broj_simetricnih/2;

    cout <<rezultat;
	return 0;
}
