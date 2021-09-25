# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from queue import PriorityQueue


# Немножко больше, чем в задании, но уж очень захотелось


class Node:
    def __init__(self, frequency, symbol, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(string_: str):
    queue_ = PriorityQueue()
    for char in set(string_):
        freq = string_.count(char)
        queue_.put(Node(freq, char))
    while queue_.qsize() > 1:
        left = queue_.get()
        right = queue_.get()
        queue_.put(Node(left.frequency + right.frequency, None, left, right))
    return queue_.get()


def __encode(root: Node, string_: str, huffman_dict: dict):
    if root is None:
        return
    if root.left is None and root.right is None:
        huffman_dict[root.symbol] = string_ if len(string_) > 0 else '1'
    __encode(root.left, string_ + '0', huffman_dict)
    __encode(root.right, string_ + '1', huffman_dict)


def __decode(root: Node, index: int, string_: str, result: list):
    if root is None:
        return index
    if root.left is None and root.right is None:
        result.append(root.symbol)
        return index
    index += 1
    root = root.left if string_[index] == '0' else root.right
    return __decode(root, index, string_, result)


def huffman_encode(string_: str):
    root = build_huffman_tree(string_)
    huffman_dict = {}
    __encode(root, '', huffman_dict)
    return ''.join(huffman_dict[char] for char in string_), root


def huffman_decode(root: Node, encoded_string: str):
    decoded = []
    index = -1
    while index < len(encoded_string) - 1:
        index = __decode(root, index, encoded_string, decoded)
    return ''.join(decoded)


if __name__ == '__main__':
    test_cases = [
        'From fairest creatures we desire increase,',
        'That thereby beauty’s rose might never die,',
        'But as the riper should by time decrease,',
        'His tender heir mught bear his memeory:',
        'But thou, contracted to thine own bright eyes,',
        'Feed’st thy light’st flame with self-substantial fuel,',
        'Making a famine where abundance lies,',
        'Thyself thy foe, to thy sweet self too cruel.',
        'Thou that art now the world’s fresh ornament',
        'And only herald to the gaudy spring,',
        'Within thine own bud buriest thy content',
        'And, tender churl, makest waste in niggarding.',
        'Pity the world, or else this glutton be,',
        'To eat the world’s due, by the grave and thee.',
    ]

    for case in test_cases:
        text, tree = huffman_encode(case)
        print(text)

        res = huffman_decode(tree, text)
        print(res)
        if res != case:
            print('FAILURE')
        print('*' * 120)
