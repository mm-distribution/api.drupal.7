# node_type_form_validate()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 256–279 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L256-L279)
- **Module/theme:** node

## Signature

```php
function node_type_form_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for node_type_form().

@see node_type_form_submit()
```

## Code

```php
function node_type_form_validate($form, &$form_state) {
  $type = new stdClass();
  $type->type = $form_state['values']['type'];
  $type->name = trim($form_state['values']['name']);

  // Work out what the type was before the user submitted this form
  $old_type = $form_state['values']['old_type'];

  $types = node_type_get_names();

  if (!$form_state['values']['locked']) {
    // 'theme' conflicts with theme_node_form().
    // '0' is invalid, since elsewhere we check it using empty().
    if (in_array($type->type, array('0', 'theme'))) {
      form_set_error('type', t("Invalid machine-readable name. Enter a name other than %invalid.", array('%invalid' => $type->type)));
    }
  }

  $names = array_flip($types);

  if (isset($names[$type->name]) && $names[$type->name] != $old_type) {
    form_set_error('name', t('The human-readable name %name is already taken.', array('%name' => $type->name)));
  }
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
