######################################################################################################
##                                                                                                  ##
##                                     Assignment#2   Week_03                                       ##
##                                                                                                  ##
##    Short description: This function is able to cache potentially time-consuming computations.    ##
##                                                                                                  ##
##    Date: 2016/01/24                                                                              ##                
##                                                                                                  ##
##    Version: 1.0                                                                                  ##        
##                                                                                                  ##
######################################################################################################

# The function cacheMatrix creates a special kind of multidimensional object (matrix) which can 
# cache its inverse

cacheMatrix <- function(x = matrix()) 
        {
                m <- NULL
                set <- function(y) {
                        x <<- y
                        m <<- NULL
        }
        get <- function() x
        setmatinv <- function(matinv) m <<- matinv
        getmatinv <- function() m
        list( set = set, get = get, setmatinv=setmatinv, getmatinv=getmatinv)
}


# The function cacheSolve looks at previously saved results for matrix inverse. If there is no 
# previously saved results, it finds matrix inverse, saves it and returns the inverse. If there 
# is previously saved results, it returns the saved results

cacheSolve <- function(x, ...) 
{
        m <- x$getmatinv()
        if (!is.null(m))
        {
                message("Getting cached data")
                return (m)
        }
        data <- x$get()
        m <- solve(data, ...)
        x$setmatinv(m)
        m
}

# Set the default value for the matrix (nrow = ncol <- default value. In this case the default value 
# is set to 5. Works also well with default value sets to 1000 to compare time consuming

matorder<-as.numeric(5)
print(matorder)

tmpmat<-matrix(runif(matorder*matorder),nrow=matorder, ncol=matorder)
print(tmpmat)

# Set the result of cacheMatrix in m, the result of cacheSolver in inmt and print the content
m <- cacheMatrix(tmpmat)
inmt <- cacheSolve(m)
print(inmt)
