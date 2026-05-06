from .forms import HouseForm 
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from .models import Houses 
from .serializer import HousesSerializers 

import pickle
import json 
import os
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from xhtml2pdf import pisa
from datetime import datetime

class CustomerView(viewsets.ModelViewSet): 
    queryset = Houses.objects.all() 
    serializer_class = HousesSerializers 


def status(location,sqft,bhk,bath):
    import os
    base_path = os.path.dirname(__file__)
    columns_path = os.path.join(base_path, "columns.json")
    model_path = os.path.join(base_path, "banglore_home_prices_model.pickle")
    
    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
    with open(model_path, 'rb') as f:
            __model = pickle.load(f)
    try:
        loc_index =  __data_columns.index(location.lower())
        print("Entered into the try9999")
    except:
        return "Provide a location in banglore"
    try:
        sqft = float(sqft)
        bath = int(bath)
        bhk = int(bhk)
    except (ValueError, TypeError):
        return "Invalid input values"

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    
    prediction = __model.predict([x])[0]
    return round(max(0, prediction), 2)

       
@login_required(login_url='login')
def price_prediction(request):
    json_data = '''
{
  "data_columns": [
    "total_sqft",
    "bath",
    "bhk",
    "1st block jayanagar",
    "1st phase jp nagar",
    "2nd phase judicial layout",
    "2nd stage nagarbhavi",
    "5th block hbr layout",
    "5th phase jp nagar",
    "6th phase jp nagar",
    "7th phase jp nagar",
    "8th phase jp nagar",
    "9th phase jp nagar",
    "aecs layout",
    "abbigere",
    "akshaya nagar",
    "ambalipura",
    "ambedkar nagar",
    "amruthahalli",
    "anandapura",
    "ananth nagar",
    "anekal",
    "anjanapura",
    "ardendale",
    "arekere",
    "attibele",
    "beml layout",
    "btm 2nd stage",
    "btm layout",
    "babusapalaya",
    "badavala nagar",
    "balagere",
    "banashankari",
    "banashankari stage ii",
    "banashankari stage iii",
    "banashankari stage v",
    "banashankari stage vi",
    "banaswadi",
    "banjara layout",
    "bannerghatta",
    "bannerghatta road",
    "basavangudi",
    "basaveshwara nagar",
    "battarahalli",
    "begur",
    "begur road",
    "bellandur",
    "benson town",
    "bharathi nagar",
    "bhoganhalli",
    "billekahalli",
    "binny pete",
    "bisuvanahalli",
    "bommanahalli",
    "bommasandra",
    "bommasandra industrial area",
    "bommenahalli",
    "brookefield",
    "budigere",
    "cv raman nagar",
    "chamrajpet",
    "chandapura",
    "channasandra",
    "chikka tirupathi",
    "chikkabanavar",
    "chikkalasandra",
    "choodasandra",
    "cooke town",
    "cox town",
    "cunningham road",
    "dasanapura",
    "dasarahalli",
    "devanahalli",
    "devarachikkanahalli",
    "dodda nekkundi",
    "doddaballapur",
    "doddakallasandra",
    "doddathoguru",
    "domlur",
    "dommasandra",
    "epip zone",
    "electronic city",
    "electronic city phase ii",
    "electronics city phase 1",
    "frazer town",
    "gm palaya",
    "garudachar palya",
    "giri nagar",
    "gollarapalya hosahalli",
    "gottigere",
    "green glen layout",
    "gubbalala",
    "gunjur",
    "hal 2nd stage",
    "hbr layout",
    "hrbr layout",
    "hsr layout",
    "haralur road",
    "harlur",
    "hebbal",
    "hebbal kempapura",
    "hegde nagar",
    "hennur",
    "hennur road",
    "hoodi",
    "horamavu agara",
    "horamavu banaswadi",
    "hormavu",
    "hosa road",
    "hosakerehalli",
    "hoskote",
    "hosur road",
    "hulimavu",
    "isro layout",
    "itpl",
    "iblur village",
    "indira nagar",
    "jp nagar",
    "jakkur",
    "jalahalli",
    "jalahalli east",
    "jigani",
    "judicial layout",
    "kr puram",
    "kadubeesanahalli",
    "kadugodi",
    "kaggadasapura",
    "kaggalipura",
    "kaikondrahalli",
    "kalena agrahara",
    "kalyan nagar",
    "kambipura",
    "kammanahalli",
    "kammasandra",
    "kanakapura",
    "kanakpura road",
    "kannamangala",
    "karuna nagar",
    "kasavanhalli",
    "kasturi nagar",
    "kathriguppe",
    "kaval byrasandra",
    "kenchenahalli",
    "kengeri",
    "kengeri satellite town",
    "kereguddadahalli",
    "kodichikkanahalli",
    "kodigehaali",
    "kodigehalli",
    "kodihalli",
    "kogilu",
    "konanakunte",
    "koramangala",
    "kothannur",
    "kothanur",
    "kudlu",
    "kudlu gate",
    "kumaraswami layout",
    "kundalahalli",
    "lb shastri nagar",
    "laggere",
    "lakshminarayana pura",
    "lingadheeranahalli",
    "magadi road",
    "mahadevpura",
    "mahalakshmi layout",
    "mallasandra",
    "malleshpalya",
    "malleshwaram",
    "marathahalli",
    "margondanahalli",
    "marsur",
    "mico layout",
    "munnekollal",
    "murugeshpalya",
    "mysore road",
    "ngr layout",
    "nri layout",
    "nagarbhavi",
    "nagasandra",
    "nagavara",
    "nagavarapalya",
    "narayanapura",
    "neeladri nagar",
    "nehru nagar",
    "ombr layout",
    "old airport road",
    "old madras road",
    "padmanabhanagar",
    "pai layout",
    "panathur",
    "parappana agrahara",
    "pattandur agrahara",
    "poorna pragna layout",
    "prithvi layout",
    "r.t. nagar",
    "rachenahalli",
    "raja rajeshwari nagar",
    "rajaji nagar",
    "rajiv nagar",
    "ramagondanahalli",
    "ramamurthy nagar",
    "rayasandra",
    "sahakara nagar",
    "sanjay nagar",
    "sarakki nagar",
    "sarjapur",
    "sarjapur  road",
    "sarjapura - attibele road",
    "sector 2 hsr layout",
    "sector 7 hsr layout",
    "seegehalli",
    "shampura",
    "shivaji nagar",
    "singasandra",
    "somasundara palya",
    "sompura",
    "sonnenahalli",
    "subramanyapura",
    "sultan palaya",
    "tc palaya",
    "talaghattapura",
    "thanisandra",
    "thigalarapalya",
    "thubarahalli",
    "thyagaraja nagar",
    "tindlu",
    "tumkur road",
    "ulsoor",
    "uttarahalli",
    "varthur",
    "varthur road",
    "vasanthapura",
    "vidyaranyapura",
    "vijayanagar",
    "vishveshwarya layout",
    "vishwapriya layout",
    "vittasandra",
    "whitefield",
    "yelachenahalli",
    "yelahanka",
    "yelahanka new town",
    "yelenahalli",
    "yeshwanthpur"
  ]
}
'''

    # Parse the JSON object
    data = json.loads(json_data)

    # Extract the location columns starting from the 4th column
    location_columns = data["data_columns"][3:]
    # print(location_columns,"[][][][][[[]]]")
    if request.method=='POST':
        location = request.POST.get('location')
        sqft = request.POST.get('square_feet')
        bathroom = request.POST.get('bathroom')
        bedroom = request.POST.get('bedroom')
        print(location,sqft,bathroom,bedroom,"qwqwqwqwqwqwqwqwqwqwqwqwqwqwqwqwqw")
        result = status(location, sqft, bedroom, bathroom)
        # to_split = str(result)
        # splitted_amount = to_split.split('.')
        # # Convert to crore and lakh
        # cror = int(result) / 100
        # crore = str(cror)
        # split_cr = crore.split('.')
        # print(len(splitted_amount[0]),"12121212121212121212121")
        # if len(split_cr[0]) == 3:
        #     crore_number = split_cr[0]
        #     crore_number = int(crore_number)
        #     lakhs_number = split_cr[1]
        #     lakhs_number = int(lakhs_number)
        #     print(crore_number,lakhs_number,"cr,lkhs")
        #     if crore_number >= 2 and lakhs_number >= 2:
        #         result = f"{crore_number} crores {lakhs_number} lakhs"
        #     elif crore_number < 2 and lakhs_number >= 2:
        #         result = f"{crore_number} crore {lakhs_number} lakhs"
        #     elif crore_number >= 2 and lakhs_number < 2:
        #         result = f"{crore_number} crores {lakhs_number} lakh"
        # elif len(split_cr[0]) == 2:
        #     result = f"{split_cr[1]} lakhs"


        if isinstance(result, str):
            # If result is an error message string from status function
            pass
        elif result <= 0:
            result = "Please enter realistic values (e.g., 500+ sqft)"
        else:
            result_str = str(result) + " Lakhs"
            # Save to history
            Houses.objects.create(
                user=request.user,
                location=location,
                sqft=sqft,
                bathroom=bathroom,
                bedroom=bedroom,
                predicted_price=result_str
            )
            result = "Estimated Price : " + result_str

        context = {
            "data": result,
            "locations": location_columns,
            "selected_location": location,
            "sqft": sqft,
            "bathroom": int(bathroom) if bathroom else 0,
            "bedroom": int(bedroom) if bedroom else 0
        }
        return render(request, 'form.html', context) 
    return render(request, 'form.html',{"locations":location_columns})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('price_prediction')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('price_prediction')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'login.html')
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    # Prepare data for charts
    base_path = os.path.dirname(__file__)
    columns_path = os.path.join(base_path, "columns.json")
    with open(columns_path, "r") as f:
        data_columns = json.load(f)['data_columns']
    
    locations = data_columns[3:]
    
    # Select some representative locations for comparison
    popular_locations = ['whitefield', 'sarjapur  road', 'electronic city', 'kanakpura road', 'thanisandra', 'yelahanka', 'hebbal', 'marathahalli', 'raja rajeshwari nagar', 'bannerghatta road']
    
    # Filter only those that actually exist in the data columns
    popular_locations = [loc for loc in popular_locations if loc in locations]
    
    # Get predictions for these locations (1000 sqft, 2 BHK, 2 Bath)
    chart_data = []
    for loc in popular_locations:
        price = status(loc, 1000, 2, 2)
        if not isinstance(price, str):
            chart_data.append({'location': loc.title(), 'price': price})
    
    # Sort by price
    chart_data = sorted(chart_data, key=lambda x: x['price'], reverse=True)
    
    labels = [item['location'] for item in chart_data]
    prices = [item['price'] for item in chart_data]

    context = {
        'labels': json.dumps(labels),
        'prices': json.dumps(prices),
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def download_report(request):
    location = request.GET.get('location', '')
    sqft = request.GET.get('sqft', '')
    bathroom = request.GET.get('bathroom', '')
    bedroom = request.GET.get('bedroom', '')
    result = request.GET.get('result', '')
    
    context = {
        'location': location,
        'sqft': sqft,
        'bathroom': bathroom,
        'bedroom': bedroom,
        'result': result,
        'date': datetime.now().strftime('%d %b %Y'),
    }
    
    template_path = 'report_template.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="valuation_report_{location}.pdf"'
    
    template = render(request, template_path, context)
    pisa_status = pisa.CreatePDF(template.content, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + template.content + '</pre>')
    return response

@login_required(login_url='login')
def history(request):
    user_history = Houses.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'history.html', {'history': user_history})

@login_required(login_url='login')
def delete_history(request, pk):
    try:
        prediction = Houses.objects.get(pk=pk, user=request.user)
        prediction.delete()
        messages.success(request, 'Prediction record deleted successfully.')
    except Houses.DoesNotExist:
        messages.error(request, 'Record not found.')
    return redirect('history')

@login_required(login_url='login')
def emi_calculator(request):
    context = {}
    if request.method == 'POST':
        p = float(request.POST.get('amount', 0))
        r = float(request.POST.get('interest', 0))
        n = int(request.POST.get('tenure', 0)) * 12 # Convert years to months
        
        if p > 0 and r > 0 and n > 0:
            # Monthly interest rate
            mr = r / (12 * 100)
            # EMI Formula: P * r * (1+r)^n / ((1+r)^n - 1)
            emi = p * mr * ((1 + mr)**n) / (((1 + mr)**n) - 1)
            total_payment = emi * n
            total_interest = total_payment - p
            
            context = {
                'emi': round(emi, 2),
                'total_payment': round(total_payment, 2),
                'total_interest': round(total_interest, 2),
                'principal': p,
                'interest_rate': r,
                'tenure': n / 12,
                'calculated': True
            }
    return render(request, 'emi_calculator.html', context)

@login_required(login_url='login')
def compare_locations(request):
    base_path = os.path.dirname(__file__)
    columns_path = os.path.join(base_path, "columns.json")
    with open(columns_path, "r") as f:
        data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]

    context = {'locations': locations}

    if request.method == 'POST':
        sqft = request.POST.get('square_feet', '1000')
        bhk = request.POST.get('bedroom', '2')
        bath = request.POST.get('bathroom', '2')
        selected = request.POST.getlist('selected_locations')

        # Limit to 5 locations max
        selected = selected[:5]

        results = []
        for loc in selected:
            price = status(loc, sqft, bhk, bath)
            if not isinstance(price, str) and price > 0:
                results.append({
                    'location': loc.title(),
                    'location_raw': loc,
                    'price': price,
                    'price_per_sqft': round(price * 100000 / float(sqft), 2) if float(sqft) > 0 else 0,
                })

        results = sorted(results, key=lambda x: x['price'], reverse=True)

        # Find cheapest & most expensive
        if results:
            cheapest = min(results, key=lambda x: x['price'])
            expensive = max(results, key=lambda x: x['price'])
            for r in results:
                r['is_cheapest'] = r['location'] == cheapest['location']
                r['is_expensive'] = r['location'] == expensive['location']
                if expensive['price'] > 0:
                    r['bar_width'] = round((r['price'] / expensive['price']) * 100)
                else:
                    r['bar_width'] = 0

        labels = [r['location'] for r in results]
        prices = [r['price'] for r in results]

        context.update({
            'results': results,
            'labels': json.dumps(labels),
            'prices': json.dumps(prices),
            'sqft': sqft,
            'bhk': bhk,
            'bath': bath,
            'selected_locations': selected,
            'compared': True,
        })

    return render(request, 'comparison.html', context)

@login_required(login_url='login')
def user_profile(request):
    user = request.user
    # Total predictions made by the user
    total_predictions = Houses.objects.filter(user=user).count()
    # Recent 5 predictions
    recent = Houses.objects.filter(user=user).order_by('-created_at')[:5]
    context = {
        'total_predictions': total_predictions,
        'recent_predictions': recent,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def recommendations(request):
    base_path = os.path.dirname(__file__)
    columns_path = os.path.join(base_path, "columns.json")
    with open(columns_path, "r") as f:
        data_columns = json.load(f)['data_columns']
    locations = data_columns[3:]

    context = {'active_page': 'recommendations'}

    if request.method == 'POST':
        budget = float(request.POST.get('budget', 0))
        bhk = int(request.POST.get('bhk', 2))
        
        # Estimate sqft based on BHK
        sqft = bhk * 600
        bath = max(1, bhk - 1) # Simple logic for bathrooms

        recommendations = []
        
        # We can't iterate through ALL 240+ locations on every request, it's slow.
        # Let's pick a diverse set of ~40 popular locations for recommendations
        sample_locations = [
            'whitefield', 'sarjapur  road', 'electronic city', 'kanakpura road', 
            'thanisandra', 'yelahanka', 'hebbal', 'marathahalli', 
            'raja rajeshwari nagar', 'bannerghatta road', 'hennur road', 
            'jp nagar', ' Uttarahalli', 'HSR Layout', 'Electronic City Phase II',
            '7th Phase JP Nagar', 'Bellandur', 'Rajaji Nagar', 'Begur Road',
            'Varthur', 'Kengeri', 'Binny Pete', 'Kothanur', 'Horamavu',
            'Ramamurthy Nagar', 'Malleshwaram', 'Old Madras Road', 'Yeshwanthpur',
            'Kaggadasapura', 'Kanakapura', 'Hosur Road', 'Bisuvanahalli',
            'Jakkur', 'Hennur', 'Thigalarapalya', 'Hosa Road', 'Kudlu Gate',
            'Panathur', 'Brookefield', 'Babusapalaya'
        ]
        
        # Filter existing
        sample_locations = [loc for loc in sample_locations if loc.lower() in [l.lower() for l in locations]]

        for loc in sample_locations:
            price = status(loc, sqft, bhk, bath)
            if not isinstance(price, str) and price > 0:
                # If within budget or max 20% over
                if price <= budget * 1.2:
                    diff = budget - price
                    recommendations.append({
                        'location': loc.title(),
                        'price': price,
                        'sqft': sqft,
                        'diff': diff,
                        'status': 'Under Budget' if diff >= 0 else 'Slightly Over'
                    })

        # Sort by proximity to budget
        recommendations = sorted(recommendations, key=lambda x: abs(x['diff']))[:12]

        context.update({
            'recommendations': recommendations,
            'budget': budget,
            'bhk': bhk,
            'searched': True
        })

    return render(request, 'recommendations.html', context)
