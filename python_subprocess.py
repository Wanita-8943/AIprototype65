import subprocess #สำหรับ รัน terminal command

if __name__ == "__main__":
    # # basic
    # subprocess.run(["ls", "-ltr"])
    # subprocess.run(["python", "python_script101.py","--x","8"])
   

    process = subprocess.Popen(["python", "python_script101.py","--x","8"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    print(out.decode('utf-8'))

#HW สั่งรัน python_script101.py 50 รอบ โดย x = 1,3,5,7,... 
# แล้วให้เอา output ของ xt มารวมกัน แล้ว print ออกมา
    
    # print('HW1')
    # x = range(1, 100, 2)
    # print('x = ',list(x))
    # process = subprocess.Popen(["python", "python_script101.py","--x", f"{x}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # out, err = process.communicate()
    # print(out.decode('utf-8'))

    # process = subprocess.Popen(["python", "python_script_101.py", "--x", f"{x}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # for i in range(1, 100, 2):
    #     process = subprocess.Popen(["python", "python_script_101.py", "--x", f"{i}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     out, err = process.communicate()
    #     x = out.decode('utf-8')
    #     # print(f"(Input x: {i}")
    #     # print(x)
    #     print(out.decode('utf-8'))
    #     xt = list(i)
    #     print(xt)
    #     print('sum = ', xt)
