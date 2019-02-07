### Big O

##### Big O is the language and metric we use to describe the efficiency of algorithms. Not understanding it can really hurt you in developing an algorithm. You will not be able to discern whether your algorithm is getting faster or slower. Yikes.

> Time Complexity

- the amount of time it takes to parse through data will effect the runtime of the program.

  -- O(1) is constant runtime. As the data gets bigger. The amount of time it takes to retrieve it is the exact same. For example, delivering data over an airplane.
  -- O(n) is Linear runtime. It will eventually be faster than a constant runtime.

> Space Complexity

- when you have a two dimensional array of size nxn, this will require O(n^2)

  -- O(n^2) is quadratic runtime. The program gets a exponentially slower when the dataset gets bigger.

> Drop the Constants

- Big O just describes the rate of increase. So you find the derivative of the function to get the runtime. O(n) is not always better than 0(n^2)

> Drop The Non-Dominant Terms

    -- O(N^2 + N) becomes O(N^2)
    -- O(N + log N) becomes O(N)
    -- O(5*2^n + 1000N^100) becomes O(2^n)


