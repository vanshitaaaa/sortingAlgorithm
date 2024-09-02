import time

def Bubble_Sort(array, drawrectangle,delay):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                drawrectangle(array, ['MediumOrchid' if x == j or x == j+1 else 'purple' for x in range(len(array))] )
                time.sleep(delay)
    drawrectangle(array, ['MediumOrchid' for x in range(len(array))])


'''def Merge_Sort(array, drawrectangle,delay):
    global middle
    global left
    global right
    if len(array) < 2:
        drawrectangle(array, ['MediumOrchid' for x in range(len(array))])
        
        
 
    middle = int(len(array)/2)
    left = Merge_Sort(array[:middle],drawrectangle,delay)
    right = Merge_Sort(array[middle:],drawrectangle,delay)
 
    return Merge(left, right , drawrectangle , delay)

def Merge(left, right , drawrectangle , delay):
    if not len(left) or not len(right):
        return left or right
 
    global result
    result = []
    global i
    global j
    i = j =0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
            drawrectangle(array, ['MediumOrchid' if x == i or x == j else 'purple' for x in range(len(array))] )
            time.sleep(delay)
        else:
            result.append(right[j])
            j+= 1
            drawrectangle(array, ['MediumOrchid' if x == j  else 'purple' for x in range(len(array))] )
            time.sleep(delay)
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            drawrectangle(array, ['MediumOrchid' if x == i or x == j else 'purple' for x in range(len(array))] )
            time.sleep(delay)
            break
    drawrectangle(array, ['MediumOrchid' for x in range(len(array))])'''
 
    
       
    
def Selection_Sort(array, drawrectangle,delay):
    
    global min_index
    for i in range(len(array)):
        min_index = i
        for j in range(i+1 , len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
        drawrectangle(array, ['MediumOrchid' if x == i or x == min_index else 'purple' for x in range(len(array))] )
        time.sleep(delay)
    drawrectangle(array, ['MediumOrchid' for x in range(len(array))])


         
   
     
    
    

    
    
