# node_forms()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 3781–3789 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L3781-L3789)
- **Module/theme:** node
- **Implements:** [hook_forms()](../../system/system.api.php/hook_forms.md)

## Signature

```php
function node_forms()
```

## Documentation

```text
Implements hook_forms().

All node forms share the same form handler.
```

## Code

```php
function node_forms() {
  $forms = array();
  if ($types = node_type_get_types()) {
    foreach (array_keys($types) as $type) {
      $forms[$type . '_node_form']['callback'] = 'node_form';
    }
  }
  return $forms;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
