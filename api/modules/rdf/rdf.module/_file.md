# modules/rdf/rdf.module

- **Source:** [local](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · 873 lines
- **Module/theme:** rdf

## File documentation

```text
@file
Enables semantically enriched output for Drupal sites in the form of RDFa.
```

## Functions (derived index)

- [rdf_help()](rdf_help.md) — Implements hook_help().
- [rdf_rdf_namespaces()](rdf_rdf_namespaces.md) — Implements hook_rdf_namespaces().
- [rdf_get_namespaces()](rdf_get_namespaces.md) — Returns an array of RDF namespaces defined in modules that implement hook_rdf_namespaces().
- [rdf_mapping_load()](rdf_mapping_load.md) — Returns the mapping for attributes of a given entity type/bundle pair.
- [_rdf_get_default_mapping()](_rdf_get_default_mapping.md) — Helper function to get the default RDF mapping for a given entity type.
- [_rdf_mapping_load()](_rdf_mapping_load.md) — Helper function to retrieve an RDF mapping from the database.
- [_rdf_mapping_load_multiple()](_rdf_mapping_load_multiple.md) — Helper function to retrieve a set of RDF mappings from the database.
- [rdf_mapping_save()](rdf_mapping_save.md) — Saves an RDF mapping to the database.
- [rdf_mapping_delete()](rdf_mapping_delete.md) — Deletes the mapping for the given bundle from the database.
- [rdf_rdfa_attributes()](rdf_rdfa_attributes.md) — Builds an array of RDFa attributes for a given mapping. This array will typically be passed through drupal_attributes() to create the attributes variables that are available to template files. These include $attributes, $title_attributes, $content_attributes and the field-specific $item_attributes variables. For more information, see theme_rdf_template_variable_wrapper().
- [rdf_modules_installed()](rdf_modules_installed.md) — Implements hook_modules_installed().
- [rdf_modules_uninstalled()](rdf_modules_uninstalled.md) — Implements hook_modules_uninstalled().
- [rdf_entity_info_alter()](rdf_entity_info_alter.md) — Implements hook_entity_info_alter().
- [rdf_entity_load()](rdf_entity_load.md) — Implements hook_entity_load().
- [rdf_comment_load()](rdf_comment_load.md) — Implements hook_comment_load().
- [rdf_theme()](rdf_theme.md) — Implements hook_theme().
- [rdf_process()](rdf_process.md) — Template process function for adding extra tags to hold RDFa attributes.
- [rdf_preprocess_node()](rdf_preprocess_node.md) — Implements MODULE_preprocess_HOOK().
- [rdf_preprocess_field()](rdf_preprocess_field.md) — Implements MODULE_preprocess_HOOK().
- [rdf_preprocess_user_profile()](rdf_preprocess_user_profile.md) — Implements MODULE_preprocess_HOOK().
- [rdf_preprocess_username()](rdf_preprocess_username.md) — Implements MODULE_preprocess_HOOK().
- [rdf_preprocess_comment()](rdf_preprocess_comment.md) — Implements MODULE_preprocess_HOOK().
- [rdf_preprocess_taxonomy_term()](rdf_preprocess_taxonomy_term.md) — Implements MODULE_preprocess_HOOK().
- [rdf_field_attach_view_alter()](rdf_field_attach_view_alter.md) — Implements hook_field_attach_view_alter().
- [rdf_preprocess_image()](rdf_preprocess_image.md) — Implements MODULE_preprocess_HOOK().
- [theme_rdf_template_variable_wrapper()](theme_rdf_template_variable_wrapper.md) — Returns HTML for a template variable wrapped in an HTML element with the RDF attributes.
- [theme_rdf_metadata()](theme_rdf_metadata.md) — Returns HTML for a series of empty spans for exporting RDF metadata in RDFa.

## Constants

### RDF_DEFAULT_BUNDLE

- Line 74; topics: rdf

```php
define('RDF_DEFAULT_BUNDLE', '');
```

```text
RDF bundle flag: Default bundle.

Implementations of hook_rdf_mapping() should use this constant for the
'bundle' key when defining a default set of RDF mappings for an entity type.
Each bundle will inherit the default mappings defined for the entity type
unless the bundle defines its own specific mappings.
```

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
