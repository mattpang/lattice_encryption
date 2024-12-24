## Aims

Started 24/12/2024

Learn about lattice encryption, learning with errors and implement it from scratch in pure python. Try to do a toy implemenation that is resistance to quantum computing. 

Based on notes:

https://courses.grainger.illinois.edu/cs598dk/fa2019/Files/lecture10.pdf


Those notes were too basic. and doesn't really cover the link between a lattice and LWE. That was cast as a classroom example using a linear system. 

This paper covers using rings and LWE for a lattice hard probelm: 

https://www.iacr.org/archive/eurocrypt2010/66320288/66320288.pdf


Proper python implemenation can be found [here](https://github.com/GiacomoPope/kyber-py), but it isn't for use only for study.


# Todo

~~lwe linear system~~

refactor it into something less gross. 

look into wtf a ring LWE is from the paper. 

### Structure

Maybe make this a package

Use pytests