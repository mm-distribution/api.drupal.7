# locale_field_node_form_submit()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 393–395 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L393-L395)
- **Module/theme:** locale

## Signature

```php
function locale_field_node_form_submit($form, &$form_state)
```

## Documentation

```text
Form submit handler for node_form().

This submit handler needs to run before entity_form_submit_build_entity()
is invoked by node_form_submit_build_node(), because it alters the values of
attached fields. Therefore, it cannot be a hook_node_submit() implementation.
```

## Code

```php
function locale_field_node_form_submit($form, &$form_state) {
  locale_field_entity_form_submit('node', $form, $form_state);
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
