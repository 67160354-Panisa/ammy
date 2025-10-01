class Stack:
    def __init__(self):
        self.items = []  # ใช้ list เก็บข้อมูลใน stack

    def push(self, item):
        self.items.append(item)  # เพิ่มข้อมูลเข้าไปใน stack

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"  # ถ้า stack ว่าง
        return self.items.pop()  # ลบและคืนค่าข้อมูลบนสุด

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]  # คืนค่าข้อมูลบนสุดโดยไม่ลบออก

    def is_empty(self):
        return len(self.items) == 0  # ตรวจสอบว่า stack ว่างหรือไม่

    def size(self):
        return len(self.items)  # คืนค่าจำนวนสมาชิกใน stack


# -------- โปรแกรมสำหรับทดสอบ --------
s = Stack()
print("Is empty?", s.is_empty())

for i in range(1, 6):
    s.push(i)

print("Size after push:", s.size())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())