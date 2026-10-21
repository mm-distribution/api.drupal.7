# text_field_validate()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 118–142 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L118-L142)
- **Module/theme:** text
- **Implements:** [hook_field_validate()](../../../field.api.php/hook_field_validate.md)

## Signature

```php
function text_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors)
```

## Documentation

```text
Implements hook_field_validate().

Possible error codes:
- 'text_value_max_length': The value exceeds the maximum length.
- 'text_summary_max_length': The summary exceeds the maximum length.
```

## Code

```php
function text_field_validate($entity_type, $entity, $field, $instance, $langcode, $items, &$errors) {
  foreach ($items as $delta => $item) {
    // @todo Length is counted separately for summary and value, so the maximum
    //   length can be exceeded very easily.
    foreach (array('value', 'summary') as $column) {
      if (!empty($item[$column])) {
        if (!empty($field['settings']['max_length']) && drupal_strlen($item[$column]) > $field['settings']['max_length']) {
          switch ($column) {
            case 'value':
              $message = t('%name: the text may not be longer than %max characters.', array('%name' => $instance['label'], '%max' => $field['settings']['max_length']));
              break;

            case 'summary':
              $message = t('%name: the summary may not be longer than %max characters.', array('%name' => $instance['label'], '%max' => $field['settings']['max_length']));
              break;
          }
          $errors[$field['field_name']][$langcode][$delta][] = array(
            'error' => "text_{$column}_length",
            'message' => $message,
          );
        }
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
