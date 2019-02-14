#!/usr/bin/env python3.6

###############################################################################
## This code is tutorial code for tensor flow
## we will read some pictures of numbers (28x28 pixles) and train the 
## NN to recognize the numbers on the right, finding the right weights and biases
###############################################################################
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/test_data-TensorFlow/", one_hot=True)

# Parameter 

# layers
n_nodes_hl1 = 500		# 500 nodes in Hidden layer 1
n_nodes_hl2 = 500
n_nodes_hl3 = 500
n_classes = 10
batch_size = 100 		# immer 100 bilder auf einmal

x = tf.placeholder('float', [None, 784]) 	#784 is 28x28 pixels
y = tf.placeholder('float', [None, n_classes])

def neuralnetworkmodel(data):
	#general structure of Neuronal network -> layers get input and output data that are initialized with random (for the start) biases and weights
	hidden_1_layer = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
			'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))}
	
	hidden_2_layer = {'weights': tf.Variable(tf.random_normal([ n_nodes_hl1, n_nodes_hl2])),
			'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}

	hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
			'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}

	output_layer= {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
			'biases': tf.Variable(tf.random_normal([n_classes]))}

	#input data will be multiplied with the weights and then the Biases are added
	l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
	l1 = tf.nn.relu(l1) 		#relu = rectifier linear unit 

	l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
	l2 = tf.nn.relu(l2) 		#relu = rectifier linear unit 
	
	l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
	l3 = tf.nn.relu(l3) 		#relu = rectifier linear unit 

	output = tf.matmul( l3 , output_layer['weights']) + output_layer['biases']
	return output


def trainneuralnetwork(x):
	prediction = neuralnetworkmodel(x)
	cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y)) 	#prediction is what the NW thinks - and y is the read value of the picture
	optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)	# we want to optimize the costs (== discrepance between numbers and real numbers
	# epocs are the TF word for learning iterarions
	epocs = 10;

	with tf.Session() as s:
		s.run(tf.global_variables_initializer())	
		
		for ep in range(epocs):
			epoc_loss = 0
			for i in range(int(mnist.train.num_examples / batch_size )) :
				epoc_x, epoc_y = mnist.train.next_batch(batch_size)
				i,c = s.run([optimizer,cost], feed_dict={x:epoc_x, y:epoc_y})
				epoc_loss += c
				print("Epoch: %s\%s\tloss: %s" % (ep+1, epocs, epoc_loss))
				
			correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
			accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

			print('Accuracy:%s' % ( accuracy.eval({x:mnist.test.images, y:mnist.test.labels})))

trainneuralnetwork(x)
