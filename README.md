### Big O

##### Big O is the language and metric we use to describe the efficiency of algorithms. Not understanding it can really hurt you in developing an algorithm. You will not be able to discern whether your algorithm is getting faster or slower. Yikes.

![Image of Graph](https://cdn-images-1.medium.com/max/1600/1*U4dZWeXgNNrYaedRCuzTIg.png)

> Time Complexity

    --the amount of time it takes to parse through data will effect the runtime of the program.

    -- O(1) is constant runtime. As the data gets bigger. The amount of time it takes to retrieve it is the exact same. For example, delivering data over an airplane.
    -- O(n) is Linear runtime. It will eventually be faster than a constant runtime.

> Space Complexity

    --when you have a two dimensional array of size nxn, this will require O(n^2)

    -- O(n^2) is quadratic runtime. The program gets a exponentially slower when the dataset gets bigger.

> Drop the Constants

    -- Big O just describes the rate of increase. So you find the derivative of the function to get the runtime. O(n) is not always better than 0(n^2)

> Drop The Non-Dominant Terms

    -- O(N^2 + N) becomes O(N^2)
    -- O(N + log N) becomes O(N)
    -- O(5*2^n + 1000N^100) becomes O(2^n)

> Multi-Part Algorithms: Add vs Mulitply

    - You multiply the run times when for loops are nested and add them otherwise.

> Amortized Time

    - takes into account the runtime will change complexity when inserting new elements. When new insertions are made, the runtime is O(n) but most of the period will be faster -> O(1).

> Log N Runtimes

    - A binary search in a sorted array. You compare x to the midpoint and sort through the left if x is smaller or right if x is bigger.

> Recursive Runtimes

    - Ususally, but not always, the runtime will be O(branches^depth), where branches is the number of times each recursive call branches.
    - The base of an exponent *matters*!, unlike the base of a log
