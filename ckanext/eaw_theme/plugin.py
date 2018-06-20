from collections import OrderedDict
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
from ckan.lib.plugins import DefaultTranslation
from json import loads


# This is a workaround issue  #2713
# https://github.com/ckan/ckan/issues/2713
def new_facet_dict(facet_dict, new_facets):
    for e in facet_dict:
        del facet_dict[e]
    for k, v in new_facets:
        facet_dict[k] = v
    return facet_dict

# template helper functions

def eaw_theme_get_spatial_query_default_extent():
    extent_s = tk.config.get('ckanext.eaw_theme.spatial_query_default_extent')
    try:
        extent = loads(extent_s)
    except:
        extent =  [[-40.0, -20.], [60.0, 20.]]
    return extent


class Eaw_ThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer
    def update_config(self, config_):
        tk.add_template_directory(config_, 'templates')
        tk.add_public_directory(config_, 'public')
        tk.add_resource('fanstatic/vendor/bootstrap-switch', 'bootstrap-switch')
        tk.add_resource('fanstatic', 'eaw_theme')

    # IFacets
    def dataset_facets(self, facet_dict, package_type):
         new_facets = [('organization', u'Organizations'),
                       ('groups', u'Projects'),
                       ('tags', u'Keywords'),
                       ('variables', u'Variables'),
                       ('systems', u'Systems'),
                       ('substances', u'Substances'),
                       ('taxa', u'Taxa')]
         return new_facet_dict(facet_dict, new_facets)

    def group_facets(self, facet_dict, group_type, package_type):
        new_facets =  [('organization', u'Organizations'),
                       ('tags', u'Keywords'),
                       ('variables', u'Variables'),
                       ('systems', u'Systems'),
                       ('substances', u'Substances'),
                       ('taxa', u'Taxa')]
        return new_facet_dict(facet_dict, new_facets)

    def organization_facets(self, facet_dict, organization_type, package_type):
        new_facets =  [('groups', u'Projects'),
                       ('tags', u'Keywords'),
                       ('variables', u'Variables'),
                       ('systems', u'Systems'),
                       ('substances', u'Substances'),
                       ('taxa', u'Taxa')]
        return new_facet_dict(facet_dict, new_facets)


    #ITemplateHelpers
    def get_helpers(self):
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'eaw_theme_get_spatial_query_default_extent':
                eaw_theme_get_spatial_query_default_extent}
