from django.contrib import admin, messages
from myapp.models import Contact,Product
# Register your models here.

admin.site.register(Contact)
# admin.site.register(Product)

def make_active(modeladmin, request, queryset): 
        queryset.update(is_active = 1) 
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!") 
  
def make_inactive(modeladmin, request, queryset): 
    queryset.update(is_active = 0) 
    messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!") 

def make_category1(modeladmin, request, queryset): 
    queryset.update(category = 1) 
    messages.success(request, "Selected Record(s) Marked as category1 Successfully !!") 

def make_category2(modeladmin, request, queryset): 
    queryset.update(category = 2) 
    messages.success(request, "Selected Record(s) Marked as category2 Successfully !!") 

def make_category3(modeladmin, request, queryset): 
    queryset.update(category = 3) 
    messages.success(request, "Selected Record(s) Marked as category3 Successfully !!")






class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category','subcategory', 'price','description', 'launching_date', 'image')
    list_filter = ("category", 'is_active')
    search_fields = ['product_name', 'category']
    prepopulated_fields = {'product_name':('category',)}
    actions = [make_category1,make_category2,make_category3]

    def active(self, obj): 
        return obj.is_active == 1
    active.boolean = True

      
  
    
admin.site.register(Product, ProductAdmin)


