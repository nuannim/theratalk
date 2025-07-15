from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

print(pwd_context.hash("folk"))
print(pwd_context.verify("folk", "$2b$12$OytzNbjYs7xyrwCMujrNJOIMD2Pm/jnLovsLPNcMpR6isdPrRkpd6"))