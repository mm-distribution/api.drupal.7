# rdf_process()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 455–480 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L455-L480)
- **Module/theme:** rdf

## Signature

```php
function rdf_process(&$variables, $hook)
```

## Documentation

```text
Template process function for adding extra tags to hold RDFa attributes.

Since template files already have built-in support for $attributes,
$title_attributes, and $content_attributes, and field templates have support
for $item_attributes, we try to leverage those as much as possible. However,
in some cases additional attributes are needed not covered by these. We deal
with those here.
```

## Code

```php
function rdf_process(&$variables, $hook) {
  // Handles attributes needed for content not covered by title, content,
  // and field items. It does this by adjusting the variable sent to the
  // template so that the template doesn't have to worry about it. See
  // theme_rdf_template_variable_wrapper().
  if (!empty($variables['rdf_template_variable_attributes_array'])) {
    foreach ($variables['rdf_template_variable_attributes_array'] as $variable_name => $attributes) {
      $context = array(
        'hook' => $hook,
        'variable_name' => $variable_name,
        'variables' => $variables,
      );
      $variables[$variable_name] = theme('rdf_template_variable_wrapper', array('content' => $variables[$variable_name], 'attributes' => $attributes, 'context' => $context));
    }
  }
  // Handles additional attributes about a template entity that for RDF parsing
  // reasons, can't be placed into that template's $attributes variable. This
  // is "meta" information that is related to particular content, so render it
  // close to that content.
  if (!empty($variables['rdf_metadata_attributes_array'])) {
    if (!isset($variables['content']['#prefix'])) {
      $variables['content']['#prefix'] = '';
    }
    $variables['content']['#prefix'] = theme('rdf_metadata', array('metadata' => $variables['rdf_metadata_attributes_array'])) . $variables['content']['#prefix'];
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
