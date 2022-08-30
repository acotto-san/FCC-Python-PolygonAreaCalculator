class Rectangle:
  
  def __init__(self,width,height):
    self.set_width(width)
    self.height = height
    
  def set_width(self,width):
    self.width =  width
    
  def set_height(self,height):
    self.height = height
    
  def get_area(self):
    return (self.width * self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  
  def get_picture(self):
    picture = ""
    if self.height > 50 or self.width > 50:
      picture = "Too big for picture."
    else:
      for i in range(self.height):
        for x in range(self.width):
          picture += "*"
        if i !=  self.height:
          picture += "\n"
    return picture
  
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
  
  def get_amount_inside(self,shape):
    return (self.get_area()//shape.get_area())
  
  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width,self.height)
    
  
class Square(Rectangle):
  
  def __init__(self,side_length):
    self.width =  side_length
    self.height = side_length
    
  def set_side(self,side_length):
    self.width =  side_length
    self.height = side_length
    
  def set_width(self,side_length):
    self.set_side(side_length)
    
  def set_height(self,side_length):
    self.set_side(side_length)
    
  def __str__(self):
    return "Square(side={})".format(self.width)


