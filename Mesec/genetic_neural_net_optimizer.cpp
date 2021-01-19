//   OpenNN: Open Neural Networks Library
//   www.opennn.org
//
//  
//
//   Artificial Intelligence Techniques SL
//   artelnics@artelnics.com

// System includes

#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <time.h>
#include <algorithm>
#include <chrono>
#include <stdint.h>
#include <limits.h>
#include <statistics.h>
#include <regex>
#include <list>
#include <random>
#include <vector>

// Systems Complementaries

#include <cmath>
#include <cstdlib>
#include <ostream>


// OpenNN includes

#include "../opennn/opennn.h"

using namespace OpenNN;
using namespace std;
using namespace chrono;


//konstante za domenu pretrazivanja

const int MIN_NUMBER_OF_HIDDEN_LAYERS = 1;
const int MAX_NUMBER_OF_HIDDEN_LAYERS = 20;

const int MIN_NUMBER_OF_NEURONS_PER_HIDDEN_LAYER = 1;
const int MAX_NUMBER_OF_NEURONS_PER_HIDDEN_LAYER = 20;

double MIN_L2_VALUE = 0.0001;
double MAX_L2_VALUE = 100;

const int NUM_OF_EPOCHS = 5;

enum ActivationFunction {
    RELU,
    LINEAR,
    SIGMOID,
    HYPERBOLIC_TANGENT
};

enum LossMethod {
    SUM_SQUARED_ERROR,
    MEAN_SQUARED_ERROR,
    NORMALIZED_SQUARED_ERROR
};


void setActivationFunction(PerceptronLayer* perceptron_layer, ActivationFunction activation_function);


class Instance {

private:
    NeuralNetwork* neuralNetwork;
    LossMethod lossMethod;
    ActivationFunction activationFunction;
    double L2;

    double fitness;

public:
    Instance(NeuralNetwork* net, LossMethod loss, ActivationFunction activation , double reg) {
        neuralNetwork = net;
        lossMethod = loss;
        L2 = reg;
        activationFunction = activation;
    }

    Instance() {};

    double getFitness() {
		return fitness;
    }
    NeuralNetwork* getNet() {
        return neuralNetwork;

    }
    double getL2() {
        return L2;
    }

    LossMethod getLossMethod() {
		return lossMethod;
    }

    ActivationFunction getActivationFunction() {
        return activationFunction;
    }

    void eval_instance(DataSet& dataset) {

        Tensor<Layer*, 1> layers = neuralNetwork->get_trainable_layers_pointers();

        for (int j = 0; j < layers.size() - 1; j++) {
            PerceptronLayer* perceptron_layer = (PerceptronLayer*)layers(j);
            setActivationFunction(perceptron_layer, activationFunction);
        }
        neuralNetwork->set_display(0);

        TrainingStrategy training_strategy(neuralNetwork, &dataset);

        switch (lossMethod)
        {
        case SUM_SQUARED_ERROR:
            training_strategy.set_loss_method(TrainingStrategy::SUM_SQUARED_ERROR);
            break;
        case MEAN_SQUARED_ERROR:
            training_strategy.set_loss_method(TrainingStrategy::MEAN_SQUARED_ERROR);
            break;
        case NORMALIZED_SQUARED_ERROR:
            training_strategy.set_loss_method(TrainingStrategy::NORMALIZED_SQUARED_ERROR);
            break;
        }
        training_strategy.set_maximum_epochs_number(NUM_OF_EPOCHS);
        training_strategy.set_display(0);
        training_strategy.set_optimization_method(TrainingStrategy::ADAPTIVE_MOMENT_ESTIMATION);
        training_strategy.get_loss_index_pointer()->set_regularization_method(LossIndex::RegularizationMethod::L2);
        training_strategy.get_loss_index_pointer()->set_regularization_weight(L2);
        AdaptiveMomentEstimation* adam = training_strategy.get_adaptive_moment_estimation_pointer();
        adam->set_batch_samples_number(1);

      
        training_strategy.perform_training();

        TestingAnalysis testing_analysis(neuralNetwork, &dataset);
        Tensor<float, 1>  res = testing_analysis.calculate_testing_errors();
        
        fitness = -res(0); //sum squared error
    }
};

Instance genetic_optimizer3Tur(DataSet& dataSet, int num_of_iter, int population_size, int print_every_n);
vector<Instance> createPopulationAndEval(DataSet& dataSet, int pop_size);
Instance currentBest(vector <Instance> pop);
void print(Instance currentBest, int iter);
Instance hybridCrossover(Instance parent1, Instance parent2, const Index input_variables_number, const Index target_variables_number);
Instance hybridMutation(Instance instance, const Index input_variables_number, const Index target_variables_number);
void randomIndexes(int numbers[3], int minIndex, int maxIndex, int num_of_elems);
int indexOfWorst(vector<Instance> instances);

vector<Instance> createPopulationAndEval(DataSet& dataSet, int pop_size) {
    vector<Instance> pop;
    random_device rd;
	default_random_engine generator(rd());
    uniform_real_distribution<double> distribution(MIN_L2_VALUE, MAX_L2_VALUE);
    const Index input_variables_number = dataSet.get_input_variables_number();
    const Index target_variables_number = dataSet.get_target_variables_number();
    for (int i = 0; i < pop_size; i++) {
		int num_of_hidden_layers = rand() % MAX_NUMBER_OF_HIDDEN_LAYERS + MIN_NUMBER_OF_HIDDEN_LAYERS;
        int total_arch_num = num_of_hidden_layers + 2;
        Tensor<Index, 1> architecture(total_arch_num);
        architecture[0] = input_variables_number;
        for (int j = 0; j < num_of_hidden_layers; j++) {
			int num_of_neurons_in_hidden_layer = rand() % MAX_NUMBER_OF_NEURONS_PER_HIDDEN_LAYER + MIN_NUMBER_OF_NEURONS_PER_HIDDEN_LAYER;
            architecture[1 + j] = num_of_hidden_layers;
        }
		architecture[total_arch_num - 1] = target_variables_number;


     
        LossMethod lossMethod = static_cast<LossMethod>(rand() % NORMALIZED_SQUARED_ERROR);
		ActivationFunction activationFunction = static_cast<ActivationFunction>(rand() % HYPERBOLIC_TANGENT);

        double L2reg = distribution(generator);

        NeuralNetwork* neural_network = new NeuralNetwork(NeuralNetwork::Approximation, architecture);
       
            
        Instance instance(neural_network, lossMethod, activationFunction, L2reg);
        instance.eval_instance(dataSet);
        pop.push_back(instance);

    }
    return pop;
}

void setActivationFunction(PerceptronLayer* perceptron_layer, ActivationFunction activation_function) {
    switch (activation_function)
    {
    case RELU:
        perceptron_layer->set_activation_function(PerceptronLayer::ActivationFunction::RectifiedLinear);
        break;
    case LINEAR:
        perceptron_layer->set_activation_function(PerceptronLayer::ActivationFunction::Linear);
        break;
    case SIGMOID:
        perceptron_layer->set_activation_function(PerceptronLayer::ActivationFunction::Logistic);
        break;
    case HYPERBOLIC_TANGENT:
        perceptron_layer->set_activation_function(PerceptronLayer::ActivationFunction::HyperbolicTangent);
        break;
    }
}



Instance genetic_optimizer3Tur(DataSet& dataSet, int num_of_iter, int population_size, int print_every_n) {

    vector<Instance> population = createPopulationAndEval(dataSet, population_size);
    const Index input_variables_number = dataSet.get_input_variables_number();
    const Index target_variables_number = dataSet.get_target_variables_number();


    for (int i = 0; i < num_of_iter; i++) {

        if (i > 0 && i % print_every_n == 0) {
             print(currentBest(population), i);
		}

        //uzmi random 3 
        vector<Instance> random_instances_3;
        int randomInd[3];
        randomIndexes(randomInd, 0, population_size - 1, 3);
        for (int j = 0; j < 3; j++) {
            Instance elem = population[randomInd[j]];
			random_instances_3.push_back(elem);
        }


        //uzmi 2 najbolja
        //treceg izbrisi
        int indexWorst = indexOfWorst(random_instances_3);
        random_instances_3.erase(random_instances_3.begin()+indexWorst);
        population.erase(population.begin() + randomInd[indexWorst]);
        Instance parent1 = random_instances_3[0];
        Instance parent2 = random_instances_3[1];

        //"krizaj"
        Instance crossover = hybridCrossover(parent1, parent2, input_variables_number, target_variables_number);

        //"mutiraj"
        Instance mutated = hybridMutation(crossover, input_variables_number, target_variables_number);

        //evaluiraj i stavi u populaciju
        mutated.eval_instance(dataSet);
        population.push_back(mutated);
    }
    return currentBest(population);
}

void print(Instance currentBest, int iter) {

    printf("Suma kvadriranih pogresaka najbolje jedinke u %d. iteraciji = %f\n", iter, abs(currentBest.getFitness()));
}


int indexOfWorst(vector<Instance> instances) {
    int worst = 0;
    for (int i = 1; i < instances.size(); i++) {
        if (instances[worst].getFitness() > instances[i].getFitness()) {
            worst = i;
        }
	}
    return worst;
}

 void randomIndexes(int numbers[3], int minIndex, int maxIndex, int num_of_elems)
{

    int new_num;
    for (int i = 0; i < num_of_elems; i++) {
        numbers[i] = -1;
    }
    for (int counter = 0; counter < num_of_elems; counter++)
    {
        do {
            new_num = rand() % maxIndex + minIndex;
            for (int i = 0; i < num_of_elems; i++) {
                if (new_num == numbers[i]) {
                    new_num = 0;
                    break;
                }
            }
        } while (new_num == 0);
        numbers[counter] = new_num;
    }
}


Instance hybridMutation(Instance instance, const Index input_variables_number, const Index target_variables_number) {
    random_device rd;
    default_random_engine generator(rd());
    uniform_real_distribution<double> distribution(0, 1);

    double r = distribution(generator);
    if (r <= 0.15) {
        //mutiraj jednu komponentu
        r = distribution(generator);
        if (r <= 0.25) {
            int num_of_hidden_layers = rand() % MAX_NUMBER_OF_HIDDEN_LAYERS + MIN_NUMBER_OF_HIDDEN_LAYERS;
            int total_arch_num = num_of_hidden_layers + 2;
            Tensor<Index, 1> architecture(total_arch_num);
            architecture[0] = input_variables_number;
            for (int j = 0; j < num_of_hidden_layers; j++) {
                int num_of_neurons_in_hidden_layer = rand() % MAX_NUMBER_OF_NEURONS_PER_HIDDEN_LAYER + MIN_NUMBER_OF_NEURONS_PER_HIDDEN_LAYER;
                architecture[1 + j] = num_of_hidden_layers;
            }
            architecture[total_arch_num - 1] = target_variables_number;
            NeuralNetwork* net = new NeuralNetwork(NeuralNetwork::Approximation, architecture);

            return Instance(net, instance.getLossMethod(), instance.getActivationFunction(), instance.getL2());
            
        }

        else if (r <= 0.5) {
            LossMethod lossMethod = static_cast<LossMethod>(rand() % NORMALIZED_SQUARED_ERROR);
            return Instance(instance.getNet(), lossMethod, instance.getActivationFunction(), instance.getL2());
		}
        else if (r <= 0.75) {
            ActivationFunction activation = static_cast<ActivationFunction>(rand() % HYPERBOLIC_TANGENT);
            return Instance(instance.getNet(), instance.getLossMethod(), activation, instance.getL2());
        }
        else {
            uniform_real_distribution<double> dist(MIN_L2_VALUE, MAX_L2_VALUE);
            double L2reg = dist(generator);
            return Instance(instance.getNet(), instance.getLossMethod(), instance.getActivationFunction() , L2reg);
        }

    }
    else {
        return instance;
    }
    

}

Instance hybridCrossover(Instance parent1, Instance parent2, const Index input_variables_number, const Index target_variables_number) {
    random_device rd;
    default_random_engine generator(rd());
    uniform_real_distribution<double> distribution(0, 1);

    double rand = distribution(generator);
	Tensor<Index, 1> child_architecture = rand < 0.5 ? (parent1.getNet())->get_architecture() : (parent2.getNet())->get_architecture();
     
    rand = distribution(generator);
    ActivationFunction activationfunction_child = rand < 0.5 ? parent1.getActivationFunction() : parent2.getActivationFunction();
    
    rand = distribution(generator);
    LossMethod lossmethod_child = rand < 0.5 ? parent1.getLossMethod() : parent2.getLossMethod();

    double l2_child = (parent1.getL2() + parent2.getL2()) / 2;

    NeuralNetwork* childNet = new NeuralNetwork(NeuralNetwork::Approximation, child_architecture);

    return Instance(childNet, lossmethod_child, activationfunction_child, l2_child);
}


Instance currentBest(vector<Instance> pop) {
    double current_best = -DBL_MAX;
    Instance best;
    for (Instance f : pop) {
        int fit = f.getFitness();
        if (fit > current_best) {
            current_best = fit;
            best = f;
        }
    }
    return best;
}



int main(void)
{
    try
    {
        
        DataSet data_set("./sin_function.csv", ',', true);
        data_set.split_samples_random(0.7, 0.0, 0.3);
        
        Instance bestInstance = genetic_optimizer3Tur(data_set, 10000, 20, 10);
        
        cout << "------------------------" << endl;
        printf("Arhitektura najbolje mreze (skriveni slojevi + output sloj)");
        Tensor<Layer*, 1> layers = bestInstance.getNet()->get_trainable_layers_pointers();
        for (int j = 0; j < layers.size() - 1; j++) {
            PerceptronLayer* perceptron_layer = (PerceptronLayer*)layers(j);
            printf(" %ld ", perceptron_layer->get_neurons_number());
        }
        printf("\n");

        printf("Aktivacijska funkcija = ");
        switch (bestInstance.getActivationFunction())
        {
            case RELU:
				printf("RELU\n");
				break;
			case LINEAR:
				printf("Linearna\n");
				break;
			case SIGMOID:
				printf("Sigmoida\n");
				break;
			case HYPERBOLIC_TANGENT:
				printf("Tangens hiperbolni\n");
				break;
        }

        printf("Funkcija gubitka = ");

        switch (bestInstance.getLossMethod())
        {
        case SUM_SQUARED_ERROR:
            printf("Suma kvad. pogresaka\n");
            break;
        case MEAN_SQUARED_ERROR:
            printf("Srednja suma kvad. pogresaka\n");         
            break;
        case NORMALIZED_SQUARED_ERROR:
			printf("Normalizirana kvadratna pogreska\n");
            break;
        }

		printf("L2 reg = %f\n", bestInstance.getL2());

		printf("Suma kvadratnih pogresaka na skupu za treniranje = %f\n", abs(bestInstance.getFitness()));


        return 0;
    }
    catch(exception& e)
    {
        cerr << e.what() << endl;

        return 1;
    }
}


// OpenNN: Open Neural Networks Library.
// Copyright(C) 2005-2020 Artificial Intelligence Techniques, SL.
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
// You should have received a copy of the GNU Lesser General Public
// License along with this library; if not, write to the Free Software
// Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
