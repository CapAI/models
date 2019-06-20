import tensorflow as tf

for example in tf.python_io.tf_record_iterator("/media/jetze/Elements/MarineNet-50k/data/test.tfrecord"):
    result = tf.train.Example.FromString(example)
