from django.shortcuts import redirect, render
from .cpp_bridge import compute_permutations


def index(request):
    return render(request, "calc/index.html")

def result(request):
    if request.method == "POST":
        numbers = [int(x) for x in request.POST["numbers"].split(",")]
        count, duration = compute_permutations(numbers)
        context = {
            "numbers": numbers,
            "count": count,
            "duration": f"{duration:.4f}",
        }
        return render(request, "calc/result.html", context)
    return redirect("index")
