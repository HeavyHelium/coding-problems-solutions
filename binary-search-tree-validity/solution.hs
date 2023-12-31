data BTree = Nil | Node Int BTree BTree

valid :: BTree -> Bool -- validity of a binary search tree
valid Nil = True
valid (Node val Nil Nil) = True
valid (Node val left@(Node left_val _ _) Nil) = left_val <= val && valid left
valid (Node val Nil right@(Node right_val _ _)) = right_val >= val && valid right
valid (Node val left@(Node left_val _ _) right@(Node right_val _ _)) =
  left_val <= val
    && right_val >= val
    && valid left
    && valid right

tree1 =
  Node
    8
    (Node 3 (Node 1 Nil Nil) (Node 6 (Node 4 Nil Nil) (Node 7 Nil Nil)))
    (Node 10 Nil (Node 14 (Node 13 Nil Nil) Nil))

tree2 =
  Node
    8
    (Node 3 (Node 1 Nil Nil) (Node 6 (Node 4 Nil Nil) (Node 7 Nil Nil)))
    (Node 10 Nil (Node 14 (Node 15 Nil Nil) Nil))

main :: IO ()
main = do
  print $ valid tree1 == True
  print $ valid tree2 == False