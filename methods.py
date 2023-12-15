import pdfkit
import numpy
import sympy

# Get the NumPy and SymPy methods
numpy_methods = dir(numpy)
sympy_methods = dir(sympy)

# Create a list of tuples, where each tuple contains a method name, description, syntax, and use
methods = []
for method in numpy_methods:
    method_description = getattr(numpy, method).__doc__
    method_syntax = "numpy." + method
    method_use = "numpy." + method + "(...)"
    methods.append((method, method_description, method_syntax, method_use))

for method in sympy_methods:
    method_description = getattr(sympy, method).__doc__
    method_syntax = "sympy." + method
    method_use = "sympy." + method + "(...)"
    methods.append((method, method_description, method_syntax, method_use))

# Define the HTML code for the PDF file
html = """
<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
      <th>Syntax</th>
      <th>Use</th>
    </tr>
  </thead>
  <tbody>
"""

# Add the NumPy and SymPy methods to the HTML code
for method in methods:
    html += """
    <tr>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
      <td>%s</td>
    </tr>
  """ % method

    html += """
  </tbody>
</table>
"""

# Generate the PDF file
pdfkit.from_string(html, output_path="methods.pdf")

# Print a message to the user
print("PDF file generated successfully!")
