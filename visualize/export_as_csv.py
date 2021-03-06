
import tensorflow as tf
import tensorflow.keras as keras

from nodeconfeu_watch.reader import AccelerationReader

dataset = AccelerationReader({
        "james": ['./data/james-v2'],
        "conor": ['./data/conor-v2']
    },
    test_ratio=0.2, validation_ratio=0.2,
    classnames=['swiperight', 'swipeleft', 'upup', 'waggle', 'clap2', 'random'])

dataset.dataframe().to_csv('./exports/dataset.csv', index=False)
