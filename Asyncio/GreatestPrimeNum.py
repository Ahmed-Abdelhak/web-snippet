"""
Writing a simple Async endpoint using Quart Framework and Asyncio
!Note: Flask is not compitable with Asyncio
"""
import asyncio
from quart import Quart

app = Quart(__name__)

"""
@params: the given max range number
"""
@app.route("/greatest_prime/<num>")
async def get_greatest_prime(num):
      n = await greatest_prime(int(num))
      return f"{n}"


not_primes = set()  # acts as a private member of my class
async def is_prime(n):
      if n in not_primes: return False
      async def calculate_if_prime():    
            for i in range(2, n):         # Async iterators could be used
                  if (n % i) == 0:
                        not_primes.add(n)  # Memoization
                        return False

      await asyncio.create_task(calculate_if_prime())
      return True   


async def greatest_prime(n):
      primes = []
      async def iteration(n):
            for i in range(2, n+1):  # Async iterators could be used
                  if await is_prime(i):
                        primes.append(i)

      await asyncio.create_task(iteration(n))
      return primes.pop()



if __name__ == "__main__":
    app.run()

