# 39_02_linear_regression.py
import tensorflow as tf


def linear_regression_1():
    x = [1, 2, 3]
    y = [1, 2, 3]

    w = tf.Variable(5.0)
    b = tf.Variable(-3.0)

    # SGD: Stochastic Gradient Descent
    optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

    for i in range(1000):
        with tf.GradientTape() as tape:
            hx = w * x + b                          # broadcast
            loss = tf.reduce_mean((hx - y) ** 2)    # vector, broadcast

        gradient = tape.gradient(loss, [w, b])
        optimizer.apply_gradients(zip(gradient, [w, b]))

        if i % 10 == 0:
            print(i, loss.numpy())
    print()

    # 퀴즈
    # x가 5와 7일 때의 결과를 예측하세요
    print('5 :', (w * 5 + b).numpy())       # 5 : 5.0000014
    print('7 :', (w * 7 + b).numpy())       # 7 : 7.000002

    print('* :', (w * [5, 7] + b).numpy())  # * : [5.0000014 7.000002 ]


    # reduce: 차원 감소
    # [1, 3, 5, 7] -> 4
    # print(sum([1, 3, 5, 7]) / 4)



linear_regression_1()

