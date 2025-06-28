from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = HttpResponse(content_type='application/pdf')
    pisa_status = pisa.CreatePDF(html, dest=result)
    return result if not pisa_status.err else HttpResponse('PDF generation failed')

def pdf_view(request):
    data = {
        'name': 'V Kokila',
        'course': 'MCA',
        'date': '2025-06-27'
    }
    return render_to_pdf('pdf_template.html', data)
def members(request):
    return HttpResponse("Hello world!")

# Create your views here.
