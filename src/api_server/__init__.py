todo_list = []
done_list = []
task_type = [
    {"type": 1, "name": "添加待办事项"},
    {"type": 2, "name": "删除待办事项"},
    {"type": 3, "name": "修改待办事项"},
    {"type": 4, "name": "查询待办事项"},
    {"type": 5, "name": "查看任务详情"},
    {"type": 6, "name": "查看已完成任务"},
    {"type": 7, "name": "完成任务"},
    {"type": 8, "name": "退出程序"},
]


def start() -> None:
    print("欢迎使用任务管理程序！")
    print_task_type()
    first_range = True
    while True:
        input_task_type = 0
        input_type = 0
        if first_range:
            input_type = input("请输入任务指令：")
            if not input_type.isdigit():
                print("指令输入错误，请重新输入！")
                continue
            input_task_type = int(input_type)
        else:
            input_type = input("请输入任务指令(输入task查看指令列表)：")
            if not input_type.isdigit() and input_type != "task":
                print("指令输入错误，请重新输入！")
                continue
            if input_type == "task":
                print_task_type()
                first_range = True
                continue
            input_task_type = int(input_type)
        first_range = False
        match input_task_type:
            case 1:
                add_todo()
                continue
            case 2:
                delete_todo()
                continue
            case 3:
                modify_todo()
                continue
            case 4:
                print_todo_list()
                continue
            case 5:
                print_task_detail()
                continue
            case 6:
                print_done_list()
                continue
            case 7:
                complete_task()
                continue
            case 8:
                break
            case _:
                print("指令输入错误，请重新输入！")


# 添加待办事项
def add_todo() -> None:
    todo = {}
    todo["name"] = input("请输入任务名称：")
    todo["description"] = input("请输入任务描述：")
    todo["deadline"] = input("请输入任务截止时间：")
    todo_list.append(todo)
    print("任务添加成功！")


# 删除待办事项
def delete_todo() -> None:
    print_todo_list()
    input_type = input("请输入要删除的任务编号：")
    if not input_type.isdigit() or int(input_type) < 1 or int(input_type) > len(todo_list):
        print("任务编号输入错误，请重新输入！")
        return
    todo_index = int(input_type)
    todo_list.remove(todo_list[todo_index - 1])
    print("任务删除成功！")


# 修改待办事项
def modify_todo() -> None:
    print_todo_list()
    input_type = input("请输入要修改的任务编号：")
    if not input_type.isdigit() or int(input_type) < 1 or int(input_type) > len(todo_list):
        print("任务编号输入错误，请重新输入！")
        return
    todo_index = int(input_type)
    todo = todo_list[todo_index - 1]
    todo["name"] = input("请输入新的任务名称(直接回车不做修改)：")
    todo["description"] = input("请输入新的任务描述(直接回车不做修改)：")
    todo["deadline"] = input("请输入新的任务截止时间(直接回车不做修改)：")
    print("任务修改成功！")


# 查看任务详情
def print_task_detail() -> None:
    task_status = input("请输入要查询的任务状态（待办/已完成）：")
    while True:
        if task_status not in ["待办", "已完成"]:
            print("任务状态输入错误，请重新输入！")
            continue
        break
    if task_status == "待办":
        print_todo_list()
        while True:
            input_type = input("请输入要查看的任务编号：")
            if not input_type.isdigit() or int(input_type) < 1 or int(input_type) > len(todo_list):
                print("任务编号输入错误，请重新输入！")
                continue
            break
        todo_index = int(input_type)
        todo = todo_list[todo_index - 1]
        print(f"任务名称：{todo['name']}")
        print(f"任务描述：{todo['description']}")
        print(f"任务截止时间：{todo['deadline']}")
    else:
        print_done_list()
        while True:
            input_type = input("请输入要查看的任务编号：")
            if not input_type.isdigit() or int(input_type) < 1 or int(input_type) > len(done_list):
                print("任务编号输入错误，请重新输入！")
                continue
            break
        done_index = int(input_type)
        done = done_list[done_index - 1]
        print(f"任务名称：{done['name']}")
        print(f"任务描述：{done['description']}")
        print(f"任务截止时间：{done['deadline']}")
        print(f"任务完成时间：{done['complete_time']}")


# 完成任务
def complete_task() -> None:
    print_todo_list()
    while True:
        input_type = input("请输入要完成的任务编号：")
        if not input_type.isdigit() or int(input_type) < 1 or int(input_type) > len(todo_list):
            print("任务编号输入错误，请重新输入！")
            continue
        break
    todo_index = int(input_type)
    todo = todo_list[todo_index - 1]
    todo["complete_time"] = input("请输入任务完成时间：")
    done_list.append(todo)
    todo_list.remove(todo)
    print("任务已完成，休息一下吧！")


# 打印待办列表
def print_todo_list() -> None:
    for index, todo in enumerate(todo_list):
        print(f"{index + 1}. {todo['name']} - {todo['deadline']}")


# 打印已完成列表
def print_done_list() -> None:
    for index, done in enumerate(done_list):
        print(f"{index + 1}. {done['name']} - {done['deadline']} - ")


# 打印任务类型
def print_task_type() -> None:
    for item in task_type:
        print(f"{item['type']}. {item['name']}")
