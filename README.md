<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">

</head>
<body>
 The first elements of a sorted list is names a pivot. And the comparision between pivos is made to other elements in the list.
 If the elements are less then pivot then they are put to "less" list if greater to "greater" list and if equal to "equal" list. Next the smaller list are sorted in the same way until the lenght of list is equal zero. In return the less and greater list are sorting not equal.
 For x = [7, 2, 5, 4, 10, 12, 5, 4, 4] the results of next iterations is: <br>
  
Number_of_elements=9 and pivot=7 //
less [2, 5, 4, 5, 4, 4] equal [7] greater [10, 12] //
Number_of_elements=6 and pivot=2 //
less [] equal [2] greater [5, 4, 5, 4, 4] //
Number_of_elements=5 and pivot=5 // 
less [4, 4, 4] equal [5, 5] greater [] // 
Number_of_elements=3 and pivot=4 // 
less [] equal [4, 4, 4] greater [] // 
Number_of_elements=2 and pivot=10 // 
less [] equal [10] greater [12] // 
[2, 4, 4, 4, 5, 5, 7, 10, 12] //

This program uses recurion method to sort elements. 
</body>
</html>


