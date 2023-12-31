from django.shortcuts import render ,redirect
from django.shortcuts import HttpResponse
from courses.models import Course , Video
from courses.forms import RegistrationForm , LoginForm
from django.views import View
from django.contrib.auth import logout , login 

# from myapp.forms import ContactForm
from django.views.generic.edit import FormView


class SignupView(FormView):
    #created class with formview subclass and remove repetitive code
    template_name='courses/signup.html'
    form_class = RegistrationForm
    # which page to go give it in success URL
    success_url =  '/login'
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        
        user = form.save()
        return super().form_valid(form)



def signout(request):
    logout(request)
    return redirect('home')

'''
#form handling with class based view
class SignupView(View):
    def get(self,request):
        form = RegistrationForm()
        return render(request, template_name='courses/signup.html' , context = {'form': form})
    
    def post(self,request):
        form = RegistrationForm(request.POST)
        if(form.is_valid()):
            user = form.save()
            if(user is not None):
                return redirect('login')
        return render(request, template_name='courses/signup.html' , context = {'form': form})
    
'''
class LoginView(FormView):
    template_name='courses/login.html'
    form_class = LoginForm
    success_url='/'   # home page
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        # user = form.save()

        # if in url next contains value then redirect

        login(self.request,form.cleaned_data)
        # request contain session where se saved this data by calling login

        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)

        return super().form_valid(form)  # this renders us to page in template_name
   


'''
        
class LoginView(View):
    def get(self,request):
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request, template_name='courses/login.html' , context = context)
    
    def post(self,request):
        form = LoginForm(request=request, data = request.POST)
        context = {
            'form' : form
        }
        if(form.is_valid()):
            print(request.user)
            return redirect('home')
        return render(request,template_name='courses/login.html',context=context)
    



'''




# class ContactFormView(FormView):
#     template_name = "contact.html"
#     form_class = ContactForm
#     success_url = "/thanks/"

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)