# Astar
使用A*算法解决两道题目：

### 森林宝石的秘密通道

在一个神秘的森林⾥，有⼀块由 9 个小方格组成的魔法石板。石板上有 8 个宝石，每个宝石上刻有 1-8 中的一个数字（每个数字都不重复）。石板上还有一个空位，用 0表示。通过移动空位周围的宝石，你可以改变宝石的位置。传说中，当宝石按照某个特定的顺序排列时（本题设为 1 3 5 7 0 2 6 8 4），魔法石板将会显露出通往一个宝藏的秘密通道。现在，你站在这块魔法石板前，需要找到⼀种最少步骤的移动方法，将宝石排列成目标顺序。为了解开这个谜题，请使用 A*算法来设计一个程序，帮助你从初始状态成功解锁秘密通道。

### 杰克的金字塔探险

在一个神秘的王国里，有一个名叫杰克的冒险家，他对宝藏情有独钟。传说在那片广袤的土地上，有一座名叫金字塔的奇迹，隐藏着无尽的财富。杰克决定寻找这座⾦字塔，挖掘隐藏在其中的宝藏。金字塔共有 N 个神秘的房间，其中 1 号房间位于塔顶，N号房间位于塔底。在这些房间之间，有先知们预先设计好的 M 条秘密通道。这些房间按照它们所在的楼层顺序进行了编号。杰克想从塔顶房间⼀直探险到塔底，带走其中的宝藏。然而，杰克对寻宝路线有着特别的要求：（1）他希望走尽可能短的路径，但为了让探险更有趣和挑战性，他想尝试 K 条不同的较短路径。（2）他希望在探险过程中尽量节省体力，所以在选择通道时，他总是从所在楼层的高处到低处。现在问题来了，给你一份金字塔内房间之间通道的列表，每条通道用（X_i, Y_i, D_i）表示，表示房间 X_i和房间 Y_i 之间有⼀条长度为 D_i 的下行通道。你需要计算出杰克可以选择的 K 条最短路径的⻓度，以便了解他在探险过程中的消耗程度。
