from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PlotInputs
import plotly.offline as opy
import plotly.graph_objects as go
from .portfolio_projection import invest, plot_returns, plot_upper_lower_bound_returns

# Create your views here.
def project_1(request):
    """Show a specific project."""
    form = PlotInputs()
    return render(request, 'project_1.html', {'form': form})    
    
def plot_graph(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlotInputs(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            starting_amount_in = form.cleaned_data['starting_amount']
            cagr_in = form.cleaned_data['cagr']
            num_years_in = form.cleaned_data['num_years']
            beginning_year_in = form.cleaned_data['beginning_year']
            annual_topup_in = form.cleaned_data['annual_topup']
            topup_years_in = form.cleaned_data['topup_years']
            
            # Call the invest function to calculate the growth of our portfolio across the years
            results = invest(starting_amount = starting_amount_in
                            ,cagr = cagr_in
                            ,num_years = num_years_in
                            ,beginning_year = beginning_year_in
                            ,annual_topup = annual_topup_in
                            ,topup_years = topup_years_in
                            )                            
            # plot the results 
            graph_1 = plot_returns(results)
            
            # call the invest function again for a compound annual growth rate 5% greater than the one input to obtain an optimistic growth projection for our investment
            results_upper_bound = invest(starting_amount = starting_amount_in
                                        ,cagr = (cagr_in + 5)
                                        ,num_years = num_years_in
                                        ,beginning_year = beginning_year_in
                                        ,annual_topup = annual_topup_in
                                        ,topup_years = topup_years_in
                                        ) 
            # call the invest function again for a compound annual growth rate 5% lower than the one input to obtain an pessimistic growth projection for our investment                           
            results_lower_bound = invest(starting_amount = starting_amount_in
                                        ,cagr = (cagr_in - 5)
                                        ,num_years = num_years_in
                                        ,beginning_year = beginning_year_in
                                        ,annual_topup = annual_topup_in
                                        ,topup_years = topup_years_in
                                        ) 
            
            # Plot our optimistic and pessimistic projections together with our expected projection to illustrate the broad range within which we can expect our actual portfolio to perform
            graph_2 = plot_upper_lower_bound_returns(results[0],results[1],results_upper_bound[1],results_lower_bound[1])
            
            # get django to render the two grapths within the 'Projections' section of project_1.html
            return render(request, 'project_1.html', {'graph_1': graph_1, 'graph_2': graph_2, 'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlotInputs()
        return render(request, 'project_1.html', {'form': form})       