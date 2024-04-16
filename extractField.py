import re
import json

inputText = """Abstract Algebra Groups, rings, fields, vector spaces, ... STEM
Anatomy Central nervous system, circulatory system, ... STEM
Astronomy Solar system, galaxies, asteroids, ... STEM
Business Ethics Corporate responsibility, stakeholders, regulation, ... Other
Clinical Knowledge Spot diagnosis, joints, abdominal examination, ... Other
College Biology Cellular structure, molecular biology, ecology, ... STEM
College Chemistry Analytical, organic, inorganic, physical, ... STEM
College Computer Science Algorithms, systems, graphs, recursion, ... STEM
College Mathematics Differential equations, real analysis, combinatorics, ... STEM
College Medicine Introductory biochemistry, sociology, reasoning, ... Other
College Physics Electromagnetism, thermodynamics, special relativity, ... STEM
Computer Security Cryptography, malware, side channels, fuzzing, ... STEM
Conceptual Physics Newton’s laws, rotational motion, gravity, sound, ... STEM
Econometrics Volatility, long-run relationships, forecasting, ... Social Sciences
Electrical Engineering Circuits, power systems, electrical drives, ... STEM
Elementary Mathematics Word problems, multiplication, remainders, rounding, ... STEM
Formal Logic Propositions, predicate logic, first-order logic, ... Humanities
Global Facts Extreme poverty, literacy rates, life expectancy, ... Other
High School Biology Natural selection, heredity, cell cycle, Krebs cycle, ... STEM
High School Chemistry Chemical reactions, ions, acids and bases, ... STEM
High School Computer Science Arrays, conditionals, iteration, inheritance, ... STEM
High School European History Renaissance, reformation, industrialization, ... Humanities
High School Geography Population migration, rural land-use, urban processes, ... Social Sciences
High School Gov’t and Politics Branches of government, civil liberties, political ideologies, ... Social Sciences
High School Macroeconomics Economic indicators, national income, international trade, ... Social Sciences
High School Mathematics Pre-algebra, algebra, trigonometry, calculus, ... STEM
High School Microeconomics Supply and demand, imperfect competition, market failure, ... Social Sciences
High School Physics Kinematics, energy, torque, fluid pressure, ... STEM
High School Psychology Behavior, personality, emotions, learning, ... Social Sciences
High School Statistics Random variables, sampling distributions, chi-square tests, ... STEM
High School US History Civil War, the Great Depression, The Great Society, ... Humanities
High School World History Ottoman empire, economic imperialism, World War I, ... Humanities
Human Aging Senescence, dementia, longevity, personality changes, ... Other
Human Sexuality Pregnancy, sexual differentiation, sexual orientation, ... Social Sciences
International Law Human rights, sovereignty, law of the sea, use of force, ... Humanities
Jurisprudence Natural law, classical legal positivism, legal realism, ... Humanities
Logical Fallacies No true Scotsman, base rate fallacy, composition fallacy, ... Humanities
Machine Learning SVMs, VC dimension, deep learning architectures, ... STEM
Management Organizing, communication, organizational structure, ... Other
Marketing Segmentation, pricing, market research, ... Other
Medical Genetics Genes and cancer, common chromosome disorders, ... Other
Miscellaneous Agriculture, Fermi estimation, pop culture, ... Other
Moral Disputes Freedom of speech, addiction, the death penalty, ... Humanities
Moral Scenarios Detecting physical violence, stealing, externalities, ... Humanities
Nutrition Metabolism, water-soluble vitamins, diabetes, ... Other
Philosophy Skepticism, phronesis, skepticism, Singer's Drowning Child, ... Humanities
Prehistory Neanderthals, Mesoamerica, extinction, stone tools, ... Humanities
Professional Accounting Auditing, reporting, regulation, valuation, ... Other
Professional Law Torts, criminal law, contracts, property, evidence, ... Humanities
Professional Medicine Diagnosis, pharmacotherapy, disease prevention, ... Other
Professional Psychology Diagnosis, biology and behavior, lifespan development, ... Social Sciences
Public Relations Media theory, crisis management, intelligence gathering, ... Social Sciences
Security Studies Environmental security, terrorism, weapons of mass destruction, ... Social Sciences
Sociology Socialization, cities and community, inequality and wealth, ... Social Sciences
US Foreign Policy Soft power, Cold War foreign policy, isolationism, ... Social Sciences
Virology Epidemiology, coronaviruses, retroviruses, herpesviruses, ... Other
World Religions Judaism, Christianity, Islam, Buddhism, Jainism, ... Humanities"""

fieldNames = ["Humanities", "Social Sciences", "STEM", "Other"]

# Extract field names from inputText
extractedFields = re.findall(r"\b(" + "|".join(fieldNames) + r")\b", inputText)

print(extractedFields, len(extractedFields))
subjects = ['abstract_algebra', 'anatomy', 'astronomy', 'business_ethics', 'clinical_knowledge', 'college_biology', 'college_chemistry', 'college_computer_science', 'college_mathematics', 'college_medicine', 'college_physics', 'computer_security', 'conceptual_physics', 'econometrics', 'electrical_engineering', 'elementary_mathematics', 'formal_logic', 'global_facts', 'high_school_biology', 'high_school_chemistry', 'high_school_computer_science', 'high_school_european_history', 'high_school_geography', 'high_school_government_and_politics', 'high_school_macroeconomics', 'high_school_mathematics', 'high_school_microeconomics', 'high_school_physics', 'high_school_psychology', 'high_school_statistics', 'high_school_us_history', 'high_school_world_history', 'human_aging', 'human_sexuality', 'international_law', 'jurisprudence', 'logical_fallacies', 'machine_learning', 'management', 'marketing', 'medical_genetics', 'miscellaneous', 'moral_disputes', 'moral_scenarios', 'nutrition', 'philosophy', 'prehistory', 'professional_accounting', 'professional_law', 'professional_medicine', 'professional_psychology', 'public_relations', 'security_studies', 'sociology', 'us_foreign_policy', 'virology', 'world_religions']

subjectFields = {}
for i in range(len(subjects)):
    subjectFields[subjects[i]] = extractedFields[i]

print(subjectFields)

# Save subjectFields as a JSON file
with open('subjectFields.json', 'w') as json_file:
    json.dump(subjectFields, json_file)