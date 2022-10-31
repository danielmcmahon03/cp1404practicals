"""
Languages
Estimate: 20 minutes
Actual:   22 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
print(ruby)

programming_languages = [python, ruby, visual_basic]
print(programming_languages)

print("The dynamically typed languages are:")
for programming_language in programming_languages:
    if programming_language.is_dynamic():
        print(programming_language.is_dynamic())
