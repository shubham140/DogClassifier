#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images_hints.py
#                                                                             
# PROGRAMMER: Shubham Chawla
# DATE CREATED:       25/1/2019                          
# REVISED DATE:  27/1/2019
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
# TODO 3: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 3" for the classify_images function 
#       Specifically EDIT and ADD code to define the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
       
        
       
       # TODO: 3a. Set the string variable model_label to be the string that's 
       #           returned from using the classifier function instead of the   
       #           empty string below.
       #
       #  Runs classifier function to classify the images classifier function 
       # inputs: path + filename  and  model, returns model_label 
       # as classifier label
       model_label = ""
       model_label = classifier(images_dir+"/"+key, model)
       model_label = model_label.lower()
       model_label = model_label.strip()
       model_label_list = model_label.split(", ")
       truth = results_dic[key][0]
       if truth in model_label_list:
          results_dic[key] = [truth, model_label, 1]
       else:
            found = False
            for term in model_label_list:

               # splits the term into a word list using split()
               word_list = term.split(" ")

               # if the pet image label hasn't been found AND it exists in the word list
               # like 'poodle' in ['standard', 'poodle'] or 'cat' in ['tabby', 'cat']
               # then found = True, the results are added to results_dic and break is
               # used to break out of the for loop since a match was found
               if (not found) and truth in word_list:
                   found = True
                   results_dic[key] = [truth, model_label, 1]
                   break 

           # If pet image label isn't found within the terms that exist in the list of labels
           # the classifier function produces then set match = 0 (not a match)
            if not found:
               results_dic[key] = [truth, model_label, 0]
                                  
    # Return results dictionary
    return(results_dic)
        
       
