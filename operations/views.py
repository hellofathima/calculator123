from django.shortcuts import render
from django.views.generic import View,TemplateView
from django import forms
from django.http import HttpResponseRedirect
from django.template import loader
from typing import Any
# Create your views here.
class CalculatorForm(forms.Form):
     
     num1=forms.IntegerField()
     num2=forms.IntegerField()

     def clean(self):
        self.cleaned_data=super().clean()
        num1=self.cleaned_data.get("num1")
        num2=self.cleaned_data.get("num2")
        if num1<=1:
            msg="plz provide no >0"
            self.add_error("num1",msg)
        if num2<=1:
            msg="plz provide no >0"
            self.add_error("num2",msg)

class HelloWorldView(View):
    def get(self,request,*args,**kwargs):
        print("print helloworld")
        return render(request,'helloworld.html')
    
class RegistrationForm(forms.Form):
     name=forms.CharField(label="Firstname",max_length=100)
     email=forms.EmailField()
     password=forms.CharField(widget=forms.PasswordInput)
     phone=forms.CharField()
     username=forms.CharField()
     address=forms.CharField(widget=forms.Textarea)

     def clean(self):
          self.cleaned_data=super().clean()
          phone=self.cleaned_data.get("phone")


          if len(phone)!=10:
               msg="invalid phone number"
               self.add_error("phone",msg)

class SignUpView(View):
     def get(self,request,*args,**kwargs):
          form=RegistrationForm()
          return render(request,"signup.html",{"form":form})
     

     def post(self,request,*args,**kwargs):
        
        # name=request.POST.get("name")
        # email=request.POST.get("email")
        # password=request.POST.get("Password")
        # print(name,email,password)



        # ===============To initialize form===========#
        form=RegistrationForm(request.POST)
        # ======vallidation=========#
        if form.is_valid():
            
            print(form.cleaned_data)#dictionry of cleaned data
            return render(request,"login.html")

        else:
            print("form with errors")
            return render(request,"signup.html",{"form":form})
            
            
               
          
        


class ContactForm(forms.Form):
     
        subject = forms.CharField(max_length=100)
        message = forms.CharField(widget=forms.Textarea)
        sender = forms.EmailField()

class ContactView(View):
     def get(self,request,*args,**kwargs):
          form=ContactForm()

          return render(request,"contact.html",{"form":form})
     
class BmsForm(forms.Form):
    weight=forms.IntegerField(label="enter weight in kg")
    height=forms.IntegerField(label="enete height in cm")

     #method override for form vallidation
    def clean(self):
        self.cleaned_data=super().clean()
        weight=self.cleaned_data.get("weight")
        height=self.cleaned_data.get("height")
        # print(self.cleaned_data)
        if weight>800:
             msg="invalid weight"
             self.add_error("weight",msg)
        if height>200:
             msg="invalid height"
             self.add_error("height",msg)
class BmsView(View):
     
     def get(self,request,*args,**kwargs):
          form=BmsForm()
          return render(request,"bmi.html",{"form":form})
     
     def post(self,request,*args,**kwargs):
        form=BmsForm(request.POST)
        if form.is_valid():
               h_incm=form.cleaned_data.get('height')
               w_in_kg=form.cleaned_data.get('weight')
               h_meter=int(h_incm)/100
               bmi=w_in_kg/(h_meter**2)
               return render(request,"bmi.html",{"result":bmi,"form":form})

        else:
                return render(request,"bmi.html",{"form":form})

       
             
class SalaryCalculateForm(forms.Form):
     
          bp=forms.IntegerField(label="enter Basicpay")
          hra=forms.IntegerField(label="enter HRA")
          sa=forms.IntegerField(label="enter special allowance")

          ta=forms.IntegerField(label="enter Travel allownce")
          pf=forms.IntegerField(label="enter Pf")

          def clean(self):
                self.cleaned_data=super().clean()

                bp=self.cleaned_data.get("bp")
                hra=self.cleaned_data.get("hra")
                sa=self.cleaned_data.get("sa")
                ta=self.cleaned_data.get("ta")
                pf=self.cleaned_data.get("pf")
                
                if bp<=1:
                    msg="plz provide vallid amount"
                    self.add_error("bp",msg)
                if hra<=1:
                    msg="plz provide vallid amount"
                    self.add_error("hra",msg)
                if sa<=1:
                    msg="plz provide vallid amount"
                    self.add_error("sa",msg)
                if ta<=1:
                    msg="plz provide vallid amount"
                    self.add_error("ta",msg)
                if pf<=1:
                    msg="plz provide vallid amount"
                    self.add_error("pf",msg)

class SalaryView(View):
     def get(self,request,*args,**kwargs):
        form=SalaryCalculateForm()
        return render(request,"salary.html",{"form":form})
     def post(self,request,*args,**kwargs):
        form=SalaryCalculateForm(request.POST)
        if form.is_valid():
                bp=form.cleaned_data.get("bp")
                hra=form.cleaned_data.get("hra")
                sa=form.cleaned_data.get("sa")
                ta=form.cleaned_data.get("ta")
                pf=form.cleaned_data.get("pf")
                netsalary=int(bp+hra+sa+ta)-int(pf)
                return render(request,"salary.html",{"result":netsalary,"form":form})
        else:
             return render(request,"salary.html",{"form":form})



class GdmngView(View):
    def get(self,request,*args,**kwargs):
        print("gooodmng")
        return render(request,"gdmng.html")
    
    
class GdafterNoonView(View):
    def get(self,request,*args,**kwargs):
        print("gooodafternoon")
        return render(request,"goodafternoon.html")
    
    
    
class AdditionView(View):
    def get(self,request,*args,**kwargs):
        form=CalculatorForm()
        return render(request,"add.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        # print("inside post")
        form=CalculatorForm(request.POST)
        if form.is_valid():
        
            print(form.cleaned_data)
    
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            res=int(n1)+int(n2)
        # print("additon result",res)
        
            return render(request,"add.html",{"result":res,"form":form})
            
        else:
             return render(request,"add.html",{"form":form})



class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        form=CalculatorForm()
        return render(request,"sub.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        # print("inside post")
       form=CalculatorForm(request.POST)
       if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
             
        # print(request.POST)
           
            res=int(n1)-int(n2)
        # print("subtraction",res)
        
            return render(request,"sub.html",{"result":res,"form":form})
    
class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
            form=CalculatorForm()
            return render(request,"multi.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        # print("inside post")
            print(request.POST)
            n1=request.POST.get("num1")
            n2=request.POST.get("num2")
            res=int(n1)*int(n2)
            print("mult res result",res)
        
            return render(request,"multi.html",{"result":res})
    
    
class DivisionView(View):
    def get(self,request,*args,**kwargs):
            form=CalculatorForm()
        
            return render(request,"div.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        # print("inside post")
            print(request.POST)
            n1=request.POST.get("num1")
            n2=request.POST.get("num2")
            res=int(n1)/int(n2)
            print("divres",res)
        
            return render(request,"div.html",{"result":res})
    

# class CubeView(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,"cube.html")
#     def post(self,request,*args,**kwargs):
#         n1=request.POST.get("num1")
#         res=int(n1)**3
#         print("cube result",res)
#         return render(request,"cube.html",{"result":res})



class IndexView(View):
    def get(self,request,*args,**kwargs):
       return render(request,"index.html") 

class OperationsView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"operation.html")
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        print(request.POST)


        # requestdotPOST={"num1":100,"num2":200,"mul":""}


        if "add" in request.POST:
             res=n1+n2
        elif "sub" in request.POST:
             res=n1-n2
        elif "mul" in request.POST:
             res=n1*n2
        else:
             res=n1/n2
        return render(request,"operation.html",{"result":res})