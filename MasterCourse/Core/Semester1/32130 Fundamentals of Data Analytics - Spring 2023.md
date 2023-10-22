# 1. Methods for cleaning data    
    
## 1.1 Resolve missing data issues:   
**1.1.1 Ignore the record**    
**1.1.2 Fill the missing values manually:**    
> The missing values are filled manually, by the most probable value or attribute mean. This cannot be used with large datasets and it is a time-consuming process.    
  
**1.1.3 Fill missing values with calculated values:**    
> Like: Missing value --> NULL or 0/1    
> Mean or other value    
  
## 1.2Resolve noisy data issues  
**1.2.1 Binning**  
**1.2.2 Clustering**  
**1.2.3 Regression**  
  
  
# 2. Data integration    
## 2.1 Methods for detecting redundancies      
  
**Pearson correlation coefficient:**    
    >.5 then a strong positive correlation    
    <-0.5 then a strong negative correlation implies    
    0 implies no correlation    
    -0.5 to 0.5 weak linear relationship between the two variables

**Note: Although Pearson's correlation coefficient can measure linear relationships, it may not capture non-linear relationships**

**chi-squared test：**  
<img width="308" alt="image" src="https://github.com/Chenbai404/Chenbai404.github.io/assets/54025529/c56e87e3-0b32-432d-81b0-bdc3688e326b">  
  
**observed values:** actual count  
**expected values:** predicted on the basis of an assumption, model or theory  
**The degrees of freedom:** Usually, Degrees of freedom = (number of columns - 1) x (number of rows - 1)
**Note: more info to Statistics Learning**
