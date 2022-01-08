from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SignUp,Note


# class LoginForm(AuthenticationForm):
#  username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
#  password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))


class UserDetail(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['contact','branch','role','photo']
        labels = {'contact': 'Mob No:','branch':'Branch','role':'Role','photo':'Upload Image'}
        widgets = {'role':forms.TextInput(attrs={'class':'form-control'}),
                   'branch':forms.TextInput(attrs={'class':'form-control'}),
                   'contact':forms.TextInput(attrs={'class':'form-control'}),
                   
        
        
        }




class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name', 'username', 'password1', 'password2']
        labels={'username':'Email Adress'}

class UserNote(forms.ModelForm):
    class Meta:
        model=Note
        fielsd='__all__'
        exclude=['user','uploadingdate','status']
        labels={'branch':'Branch','subject':'Subject','notesfile':'Note','filetype':'FileType','description':'Description'}
        widgets={'description':forms.Textarea(attrs={'class':'form-control'}),
                 'filetype' :forms.Select(attrs={'class':'form-select'}),
                 'subject' :forms.TextInput(attrs={'class':'form-control','placeholder':'Subject..'}),
                 'branch' :forms.Select(attrs={'class':'form-select'}),
                 'notesfile':forms.FileInput(attrs={'class':'form-control'})
        }



