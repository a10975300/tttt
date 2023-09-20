from xadmin.filters import MultiSelectFieldListFilter
from django.contrib import messages
from django.http import HttpResponseRedirect

import xadmin
from .models import Nud_list
from xadmin.layout import Main, Fieldset, Side, Row
from import_export import resources
from utils.notification import Notification

# define dfm user interface
class NudAdmin(object):
    list_display = ["year", "nud_id", "funnel", "source", "key_focus_area", "risk",
                    "nud_level", "title", "objective", "weekly_status", "assessment_status","risk_level","nud_owner",
                    "funnel_owner","state","product_category","leading_product","rtp_date","target_products","date"]
    list_filter = [("funnel", MultiSelectFieldListFilter),
                   ("date"),
                   ]
    search_fields = ["year", "nud_id", "funnel", "source", "key_focus_area", "risk",
                    "nud_level", "title", "objective", "weekly_status", "assessment_status","risk_level","nud_owner",
                    "funnel_owner","state","product_category","leading_product","rtp_date","target_products"]
    list_display_links = ["title"]
    readonly_fields = ["year", "nud_id", "funnel", "source", "key_focus_area", "risk",
                    "nud_level", "title", "objective", "weekly_status", "assessment_status","risk_level","nud_owner",
                    "funnel_owner","state","product_category","leading_product","rtp_date","target_products","date"]
    list_per_page = 20
    date_hierarchy = 'date'
    model_icon = 'fa fa-file-text-o' # fa fa-fire-extinguisher

    # configuration pages
    def get_form_layout(self):
        self.form_layout = (
            Main(
                Fieldset('',
                         Row('year', 'date',),
                         Row('nud_id', 'nud_owner'),
                         Row('risk', 'product_category'),
                         'title',
                         'objective',
                         'weekly_status',
                         css_class='unsort no_title'
                         ),

                Fieldset('',
                         Row( 'funnel', 'source'),
                         Row('key_focus_area', 'nud_level'),
                         Row('funnel_owner', 'rtp_date'),
                         css_class='unsort no_title'
                         ),
            ),
            Side(
                'state',
                'assessment_status',
                'risk_level',
                'leading_product',
                'target_products',
            )
        )
        return super(NudAdmin, self).get_form_layout()

#后台管理项目注册
xadmin.site.register(Nud_list, NudAdmin)