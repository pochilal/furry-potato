import matplotlib.pyplot as plt
from random import choice

if __name__ == "__main__":

    #生成数据
    x_list = [0]
    y_list = [0]
    for i in range(50000):
        x_list.append(x_list[-1]+choice([-1, 1])*choice([0, 1, 2, 3, 4]))
        y_list.append(y_list[-1]+choice([-1, 1])*choice([0, 1, 2, 3, 4]))

    #预设画布
    plt.figure(dpi=128, figsize=(10,6))

    #描点绘图
    #plt.plot(x_list[-1], y_list[-1], linewidth=4)
    plt.scatter(x_list, y_list, c=list(range(len(x_list))), cmap=plt.cm.Greens, edgecolors='none', s=10)
    plt.scatter(x_list[0], y_list[0], c='green', edgecolors='none', s=100)
    plt.scatter(x_list[-1], y_list[-1], c='red', edgecolors='none', s=100)

    #坐标轴设置
    plt.title('Random Walking', fontsize=16)
    # plt.xlabel('x', fontsize=12)
    # plt.ylabel('y', fontsize=12)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    #plt.axis([0, 105, 0, 10050])
    plt.tick_params(axis='both', which='major', labelsize=10)

    #显示/保存图片
    #plt.show()
    plt.savefig('test.png')
