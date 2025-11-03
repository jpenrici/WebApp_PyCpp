from django.shortcuts import render
from .forms import NumberSequenceForm
from .cpp_bridge import compute_permutations

def index(request):
    """
    Renders the form and processes user input.
    """
    if request.method == 'POST':
        form = NumberSequenceForm(request.POST)
        if form.is_valid():
            # Parse input numbers
            raw = form.cleaned_data['numbers']
            try:
                nums = [int(x.strip()) for x in raw.split(',')]
                result, duration = compute_permutations(nums)
                return render(request, 'calc/result.html', {
                    'numbers': nums,
                    'result': result,
                    'duration': duration,
                })
            except ValueError:
                form.add_error('numbers', 'Invalid input. Use comma-separated integers.')
    else:
        form = NumberSequenceForm()

    return render(request, 'calc/index.html', {'form': form})
