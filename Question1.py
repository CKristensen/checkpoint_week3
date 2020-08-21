def fraud_detection(customers, salary, taxes):
  fraud_list = []
  for c, s, t in zip(customers, salary, taxes):
    if((s >555000)&(t/s < 0.3)):
      fraud_list.append(c)
  return fraud_list

customers = ['James’', '‘John’', '‘Robert’', '‘Mary’', '‘Patricia’', '‘Jennifer’', 'Carl']
salary = [155000, 755000,  455000, 1255000, 635000, 575000, 555100]
taxes = [55800, 317100, 182000, 3, 171450, 71400, 166000]

print(fraud_detection(customers, salary, taxes))