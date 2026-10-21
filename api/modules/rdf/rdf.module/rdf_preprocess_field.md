# rdf_preprocess_field()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 543–566 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L543-L566)
- **Module/theme:** rdf

## Signature

```php
function rdf_preprocess_field(&$variables)
```

## Documentation

```text
Implements MODULE_preprocess_HOOK().
```

## Code

```php
function rdf_preprocess_field(&$variables) {
  $element = $variables['element'];
  $mapping = rdf_mapping_load($element['#entity_type'], $element['#bundle']);
  $field_name = $element['#field_name'];

  if (!empty($mapping) && !empty($mapping[$field_name])) {
    foreach ($element['#items'] as $delta => $item) {
      $variables['item_attributes_array'][$delta] = rdf_rdfa_attributes($mapping[$field_name], $item);
      // If this field is an image, RDFa will not output correctly when the
      // image is in a containing <a> tag. If the field is a file, RDFa will
      // not output correctly if the filetype icon comes before the link to the
      // file. We correct this by adding a resource attribute to the div if
      // this field has a URI.
      if (isset($item['uri'])) {
        if (!empty($element[$delta]['#image_style'])) {
          $variables['item_attributes_array'][$delta]['resource'] = image_style_url($element[$delta]['#image_style'], $item['uri']);
        }
        else {
          $variables['item_attributes_array'][$delta]['resource'] = file_create_url($item['uri']);
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
