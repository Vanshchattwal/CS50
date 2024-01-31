def main():
   usrcmd = input()
   print(replace(usrcmd))

def replace(usrcmd):
   usrcmd = usrcmd.replace(':)','🙂').replace(':(','🙁')
   return usrcmd

main()