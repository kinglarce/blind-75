def numDecodings(s):
    dp = [0 for _ in range(len(s)+1)]
    
    dp[0] = 1
    
    dp[1] = 0 if s[0] == '0' else 1
    
    for i in range(2, len(dp)):
        one_digit =  s[i-1]
        if one_digit != '0':
            dp_val = dp[i-1]
            dp[i] = dp_val
            
        two_digit = int(s[i-2:i])
        if two_digit >= 10 and two_digit <= 26:
            dp_val = dp[i-2]
            dp[i] += dp_val
            
    return dp[len(s)]

def numDecodings(s):
  
  dp = { len(s): 1}
  print(dp, ' - ', len(s))
  
  for i in range(len(s)-1, -1, -1):
      if s[i] == '0':
          dp[i] = 0
      else:
          dp[i] = dp[i+1]
      print('1st dp : ', dp)
      
      if (i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in "0123456")):
          dp[i] += dp[i + 2]
      print('2nd dp : ', dp)
  
  return dp[0]

numDecodings("226")