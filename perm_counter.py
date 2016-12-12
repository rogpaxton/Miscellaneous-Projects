def permutation_position(perm):

   num_list = perm.split()

   if len(num_list) > 1:
       num_list_rvs = num_list.reverse()
   else:
       num_list_rvs = num_list

   dec = 1

   perm_num = 0

   for i in num_list_rvs:
       number = (ord(i) - 96) * dec
       perm_num += number
       dec += 26

   return perm_num

   
