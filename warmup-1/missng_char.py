def missing_char(str, n):
  a = list(str)
  a[n] = ''
  return ''.join(a)