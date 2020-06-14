import sys

class Node:
    def __init__(self,key=None,frequency=0,leftChild=None,rightChild=None,parent=None,code=None,depth=0):
        self.key=key
        self.frequency=frequency
        self.leftChild=leftChild
        self.rightChild=rightChild
        self.parent=parent
        self.code=code

    def add_leftChild(self,other):
        self.leftChild=other
        other.parent=self

    def add_rightChild(self,other):
        self.rightChild=other
        other.parent=self

def smaller_freq(tree1,tree2):
    if tree1.frequency<=tree2.frequency:
        return tree1
    else:
        return tree2
    

def combine(tree1,tree2):
    new_parent=Node(frequency=tree1.frequency+tree2.frequency)
    smaller_tree=smaller_freq(tree1,tree2)
    if smaller_tree==tree1:
        new_parent.add_leftChild(smaller_tree)
        new_parent.add_rightChild(tree2)
    if smaller_tree==tree2:
        new_parent.add_leftChild(smaller_tree)
        new_parent.add_rightChild(tree1)
    return new_parent

def extract_min(tree_list):
    frequency_list=[a.frequency for a in tree_list]
    smallest=min(frequency_list)
    index=frequency_list.index(smallest)
    return tree_list.pop(index)


def build_tree(Q):
    while len(Q)>1:
        v=extract_min(Q)
        w=extract_min(Q)
        Q.append(combine(v,w))
    return extract_min(Q)


def create_graph(tree):
    L=[tree]
    graph=[]
    while L!=[]:
        v=L.pop()
        if v==None:
            continue
        else:
            graph.append(v)
            L.append(v.leftChild)
            L.append(v.rightChild)

    new_graph=[v for v in graph if v.key!=None]
    return new_graph
    
    
def get_depth_and_code(graph,key):
    for v in graph:
        if v.key==key:
            current=v
            break
    node=current
    code=[]
    depth=0
    while current.parent!=None:
        current_parent=current.parent
        depth+=1
        if current.parent.leftChild==current:
            code.append('0')
            current=current.parent
            continue
        if current.parent.rightChild==current:
            code.append('1')
            current=current.parent
            continue
    code.reverse()
    node.code=''.join(code)
    node.depth=depth


def analyze_string(word):
    characters=[]
    frequency=[]
    for char in word:
        if char not in characters:
            characters.append(char)
    for char in characters:
        frequency.append(word.count(char))
    return dict(zip(characters,frequency))

def encode(graph,word):
    for node in graph:
        word=word.replace(node.key,node.code)
    return word
    

def huffman(word):
    assert len(word)>=2 and len(set([char for char in word]))!=1, 'Word must be at least 2 characters long and contain at least 2 distinct characters!'
    characters_frequency=analyze_string(word)
    queue=[]
    for char in characters_frequency.keys():
        queue.append(Node(char,characters_frequency[char]))
    tree=build_tree(queue)
    graph=create_graph(tree)
    for key in characters_frequency.keys():
        get_depth_and_code(graph,key)
    cost=0
    for node in graph:
        cost+=node.frequency*node.depth
    encoded=encode(graph,word)
    graph.sort(key=lambda x: x.key)
    print('The word\n\n{}\n\nhas been encoded to\n\n{}\n\nThe encoded word has optimal cost {}\n\nThe following Huffman code was used\n\n'.format(word,encoded,str(cost)))
    for g in graph:
        print('{} : {}\n'.format(g.key,g.code))
    print('\nEncoding done, have a nice day! :)')




print('Huffman Coding')
print('\u00a9 Dimas Fakhri Arsaputra 2020\n')
try:
    if sys.argv[1].upper()=='HELP':
        print('If you want to encode a clause, type the following:\n')
        print('python3 huffman.py ENCODE <YOUR CLAUSE>\n')
        print('Note that you only need to " " if the clause contains more than 2 words (i.e. at least one empty space)')
    if sys.argv[1].upper()=='ENCODE':
        try:
            huffman(sys.argv[2])
        except IndexError:
            print('Argument missing!')
    if sys.argv[1].upper()!='HELP' and sys.argv[1].upper()!='ENCODE':
        print('Command not found')
except IndexError:
    print('Type HELP after huffman.py for help!')

    
'''
#Test Instances
string1='hehe'
string2='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcbbccbaaaaacbcbcbcbcbcbcbcbcbdededededaaaaaedededededddddddfffff'
'''
        
        

        
