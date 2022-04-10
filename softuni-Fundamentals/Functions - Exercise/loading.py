def progress_loading(loading):

    if loading == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    else:
        return f"{loading}% [{'%' * (loading // 10)}{'.' * (10 - loading // 10)}]\nStill loading..."

number = int(input())
print(progress_loading(number))