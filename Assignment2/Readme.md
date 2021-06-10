**getCompoundInterest** – Calculates the compound interest based on input P, R, T values. Variables are typecasted to remove any overflow and Rate is taken as percentage. Moreover, it calculates the amount iteratively. It doesn’t require to acess state variables, hence its pure.

**reqLoan** – This function helps the creditor to calculate the final amount he would have to pay to the owner(using getCompoundInterest)  and issues the amount of loan in the name of the creditor in the loans mapping. It then emits the request after adding the load on the mapping successfully.

**viewDues** – it helps ONLY the owner to VIEW the pending amount of loan to be settled. Just type in creditor’s address and it will return the pending amount. Since it is a view-only method, it doesn’t cause any state changes.

**settleDues** – This is also a ‘owner-only-accesible’ method, but it may lead to state changes. It takes in the creditor’s address. If the loan is settles, it marks the dues as 0 and returns true. It will return false if the dues, by any means remain unsettled.

**Example** – Let there be two accounts, A(owner) and B(creditor).

Suppose B took a loan of 100 units with interest rate of 9% which he is paying back in 2 years. From B, we will call reqLoan function with above parameters. It will return 118 and will make an entry in the loans mapping under key B.

Now we call viewDues from A to get the amount it has to get back. Now call settleDues to clear the loan and it will change the amount B still owes to 0. The loan has been cleared successfully.
