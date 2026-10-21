# template_process_field()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 1098–1111 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L1098-L1111)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function template_process_field(&$variables, $hook)
```

## Documentation

```text
Theme process function for theme_field() and field.tpl.php.

@see theme_field()
@see field.tpl.php
```

## Code

```php
function template_process_field(&$variables, $hook) {
  // The default theme implementation is a function, so template_process() does
  // not automatically run, so we need to flatten the classes and attributes
  // here. For best performance, only call drupal_attributes() when needed, and
  // note that template_preprocess_field() does not initialize the
  // *_attributes_array variables.
  $variables['classes'] = implode(' ', $variables['classes_array']);
  $variables['attributes'] = empty($variables['attributes_array']) ? '' : drupal_attributes($variables['attributes_array']);
  $variables['title_attributes'] = empty($variables['title_attributes_array']) ? '' : drupal_attributes($variables['title_attributes_array']);
  $variables['content_attributes'] = empty($variables['content_attributes_array']) ? '' : drupal_attributes($variables['content_attributes_array']);
  foreach ($variables['items'] as $delta => $item) {
    $variables['item_attributes'][$delta] = empty($variables['item_attributes_array'][$delta]) ? '' : drupal_attributes($variables['item_attributes_array'][$delta]);
  }
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
