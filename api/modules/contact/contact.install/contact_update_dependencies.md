# contact_update_dependencies()

- **Type:** Function
- **File:** [`modules/contact/contact.install`](_file.md), lines 94–108 · [local source](../../../../source/modules/contact/contact.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install#L94-L108)
- **Module/theme:** contact
- **Implements:** [hook_update_dependencies()](../../system/system.api.php/hook_update_dependencies.md)

## Signature

```php
function contact_update_dependencies()
```

## Documentation

```text
Implements hook_update_dependencies().
```

## Code

```php
function contact_update_dependencies() {
  // contact_update_7001() relies on the {role_permission} table being updated
  // to the new format and filled with data.
  $dependencies['contact'][7001] = array(
    'system' => 7007,
  );

  // contact_update_7002() relies on the {role_permission} table having the
  // module field, which is created in user_update_7006().
  $dependencies['contact'][7002] = array(
    'user' => 7006,
  );

  return $dependencies;
}
```

---
_Drupal 7.103 · [modules/contact/contact.install](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.install) · Licensed GPL-2.0-or-later (see LICENSE)._
