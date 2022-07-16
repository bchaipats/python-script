# namespaces
# attribute is any name following a dot, for example, z.real real is the attribute of z
# module's attributes and the global names defined in the module share the same name space.

# When invoking a script file, a module called __main__ is created and used as its own global namespace.

# The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function.

# A scope is a textual region of a Pytohn program where a namespace is directly accessible.

# At execution time, there are 3 or 4 nested scopes whose namespaces are directly accessible:
# - the innermost scope, which is searched first, contains the local names
# - the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
# - the next-to-last scope contains the current module's global names
# - the outermost scope (searched last) is the namespace containing built-in names

# nonlocal statement can be used to rebind variables found outside of the innermost scope to make it read-write enabled.
# the global scope of a function defined in a module is that module's namespace.
# if no global or nonlocal statement is in effect - assignments to names always go into the innermost scope.
# Assignments do not copy data -- they just bind names to obejcts. The same is true for deletions: the statement del x removes the binding of x from the namespace referenced by the local scope. In fact, all operations that introduce new names use the local scope: in particular, import statements and function efinitions bind the module or function name in the local scope.

# The global statement can be used to indicate that particular variables live in the global scope and should be rebound there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there.

# Example:

def scope_test():
	def do_local():
		# local assignment won't change the spam variable of the enclosing scope.
		spam = "local spam"

	def do_nonlocal():
		# nonlocal statement causes the spam variable to be the variable of the nearest enclosing scope.
		nonlocal spam
		spam = "nonlocal spam"

	def do_global():
		# global statement is the outer most scope and is basically the module's namespace.
		global spam
		spam = "global spam"

	spam = "test spam"
	do_local()
	print("After local assignment:", spam)

	do_nonlocal()
	print("After nonlocal assignment:", spam)

	do_global()
	print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
