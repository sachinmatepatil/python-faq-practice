def args_kwargs_demo(*args, **kwargs):
    print("Positional arguments (args):", args)
    print('keyword arguments (kwargs)', kwargs)


args_kwargs_demo(10, 20, 30, name='sachin', age=30, city="pune")

# 🧠 3 Key Takeaways: Why Python Passes Objects by Reference (Not by Value)
#
# 1️⃣ Everything in Python is an object.
# When you assign or pass variables, Python doesn’t copy values — it just passes a reference (pointer) to the same object in memory.
#
# 2️⃣ Efficient memory use.
# Passing references avoids making unnecessary copies, especially for large data (like lists or dictionaries).
# That makes Python faster and more memory-efficient.
#
# 3️⃣ Mutability decides behavior.
#
# Mutable objects (lists, dicts) → changes inside a function affect the original.
#
# Immutable objects (ints, strings, tuples) → appear like “pass-by-value,” because new objects are created on modification.
#
# ✅ In short:
#
# Python passes object references, not actual copies —
# whether changes reflect outside depends on mutability, not on “by value” or “by reference” labels.