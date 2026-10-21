# locale_field_entity_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 429–448 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L429-L448)
- **Module/theme:** locale

## Signature

```php
function locale_field_entity_form_submit($entity_type, $form, &$form_state )
```

## Documentation

```text
Handles field language on submit for the given entity type.

Checks if Locale is registered as a translation handler and handle possible
language changes.
```

## Code

```php
function locale_field_entity_form_submit($entity_type, $form, &$form_state ) {
  if (field_has_translation_handler($entity_type, 'locale')) {
    $entity = (object) $form_state['values'];
    $current_language = entity_language($entity_type, $entity);
    list(, , $bundle) = entity_extract_ids($entity_type, $entity);

    foreach (field_info_instances($entity_type, $bundle) as $instance) {
      $field_name = $instance['field_name'];
      $field = field_info_field($field_name);
      $previous_language = $form[$field_name]['#language'];

      // Handle a possible language change: new language values are inserted,
      // previous ones are deleted.
      if ($field['translatable'] && $previous_language != $current_language) {
        $form_state['values'][$field_name][$current_language] = $entity->{$field_name}[$previous_language];
        $form_state['values'][$field_name][$previous_language] = array();
      }
    }
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
