class VarNode:
  name=None
  type=None
  id=-1
  useAddress=False

  def __init__(self,Name,Type,Id,UseAddr):
    self.name=Name
    self.type=Type
    self.id=Id
    self.useAddress=UseAddr


class FunNode:
  isDefined=False
  name=None
  type=None
  arguments=[]

  def __init__(self,Name,Type,IsDefined,Arguments):
    self.isDefined=IsDefined
    self.name=Name
    self.type=Type
    self.arguments=Arguments


class ArrayNode:
  name=None
  type=None
  size=0

  def __init__(self,Name,Type,Size):
    self.type=Type
    self.name=Name
    self.size=Size

class Block:
  funcNode=None
  isfunction=False    #是否是函数
  varMap={}
  arrayMap={}
  BreakLabel=None     #如果break，将会跳到哪个label
  ContinueLable=None  #如果continue，将会跳到哪个label
  GotoLabel=None      #如果goto，将会跳到哪个label
