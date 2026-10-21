# taxonomy_field_widget_form()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 1736–1752 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1736-L1752)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_widget_form()](../../field/field.api.php/hook_field_widget_form.md)

## Signature

```php
function taxonomy_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element)
```

## Documentation

```text
Implements hook_field_widget_form().
```

## Code

```php
function taxonomy_field_widget_form(&$form, &$form_state, $field, $instance, $langcode, $items, $delta, $element) {
  $tags = array();
  foreach ($items as $item) {
    $tags[$item['tid']] = isset($item['taxonomy_term']) ? $item['taxonomy_term'] : taxonomy_term_load($item['tid']);
  }

  $element += array(
    '#type' => 'textfield',
    '#default_value' => taxonomy_implode_tags($tags),
    '#autocomplete_path' => $instance['widget']['settings']['autocomplete_path'] . '/' . $field['field_name'],
    '#size' => $instance['widget']['settings']['size'],
    '#maxlength' => 1024,
    '#element_validate' => array('taxonomy_autocomplete_validate'),
  );

  return $element;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
