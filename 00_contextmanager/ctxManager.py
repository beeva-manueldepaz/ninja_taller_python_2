# with open("fichero.txt") as f:
#   f.write("asfasdf2")
#
# print("xxx")

from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entro en ctx manager")

    f = open("output_example_0.txt", "w")

    yield f

    f.close()

with my_context_manager() as f2:
    f2.write("Esto se escribe en fichero")

# Todo terminar
